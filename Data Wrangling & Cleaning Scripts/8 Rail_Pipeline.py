
"""
rail_pipeline.py - FRA Form 54 (Rail Equipment Accidents) -> Power BI-ready tables
Run:  python rail_pipeline.py            (uses the path set in SRC below)
  or:  python rail_pipeline.py "C:\\path\\to\\file.csv"

Load the original CSV with pandas instead of Excel. Some narratives contain
line breaks, which can cause Excel to break the rows when saving the file.
"""

import sys
from pathlib import Path
import numpy as np
import pandas as pd

# Path to the source CSV file. Use a raw string to avoid Windows path issues.
DEFAULT_SRC = r"C:\Users\Aaron\Documents\Debut projects\2 Cleaned data\Clean_Rail_Equipment_Accident_Incident_Data_(Form_54)_20260121.csv"
SRC = Path(sys.argv[1] if len(sys.argv) > 1 else DEFAULT_SRC)
OUT = SRC.parent / "powerbi_tables"  # Output folder for the generated tables
OUT.mkdir(exist_ok=True)

# Columns needed for the analysis. Time and Other Railroad Name help identify duplicates.
KEEP = [
    "Date", "Time", "Accident Type", "Hazmat Released Cars",
    "State Abbreviation", "State Name", "County Name", "Milepost", "Latitude", "Longitude",
    "Track Type", "Track Class", "Equipment Type",
    "Equipment Damage Cost", "Track Damage Cost", "Total Damage Cost",
    "Primary Accident Cause Code", "Primary Accident Cause",
    "Total Persons Killed", "Total Persons Injured",
    "Reporting Railroad Name", "Other Railroad Name", "Maintenance Railroad Name",
    "Reporting Railroad Class", "Narrative",
]

# ---------------------------------------------------------------- 1. LOAD
# Read the header first to check which columns are available.
header = list(pd.read_csv(SRC, nrows=0).columns)
OPTIONAL = {"Time", "Other Railroad Name"}  # These columns are only needed for duplicate checks.
missing = [c for c in KEEP if c not in header]
fatal = [c for c in missing if c not in OPTIONAL]
if fatal:
    raise SystemExit(f"Missing required columns: {fatal}\nFound: {header}")

# Save the names of the columns that won't be used.
dropped = [c for c in header if c not in KEEP]
(OUT / "dropped_columns.txt").write_text("\n".join(dropped), encoding="utf-8")

# Load only the columns needed for the analysis.
df = pd.read_csv(SRC, usecols=[c for c in KEEP if c in header], low_memory=False)

# Add empty columns if optional fields are missing from the source file.
for c in missing:
    print(f"Note: optional column '{c}' not found; duplicate detection will be less precise.")
    df[c] = np.nan

df = df[KEEP].copy()

# Keep track of the original dataset size and the columns used.
qa = {"raw_rows": len(df), "columns_in_file": len(header),
      "columns_kept": len(KEEP) - len(missing), "columns_dropped": len(dropped)}

# Remove rows without a valid date.
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
qa["rows_without_date_dropped"] = int(df["Date"].isna().sum())
df = df.dropna(subset=["Date"]).copy()

# ---------------------------------------------------------------- 2. TYPES
# Convert cost, hazmat, injury, and fatality columns to numeric values.
money_cols = ["Equipment Damage Cost", "Track Damage Cost", "Total Damage Cost"]
for c in money_cols + ["Hazmat Released Cars", "Total Persons Killed", "Total Persons Injured"]:
    df[c] = pd.to_numeric(df[c].astype(str).str.replace(",", "").str.strip(), errors="coerce")

# Clean up milepost and track class values.
df["Milepost"] = pd.to_numeric(df["Milepost"].astype(str).str.strip(), errors="coerce")
df["Track Class"] = df["Track Class"].astype(str).str.strip().str.upper().replace({"NAN": "Unknown"})

# Standardize state names and clean up the accident narratives.
df["State Name"] = df["State Name"].str.title()
df["Narrative"] = df["Narrative"].fillna("").str.replace(r"\s+", " ", regex=True).str.strip()

# ---------------------------------------------------------------- 3. DERIVED FIELDS
# Extract the year and month for time-based analysis.
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.to_period("M").dt.to_timestamp()

# Group accident causes into broader categories.
cause_map = {"H": "Human factors", "T": "Track", "E": "Equipment",
             "S": "Signal & communication", "M": "Miscellaneous"}
df["Cause Group"] = df["Primary Accident Cause Code"].str[0].map(cause_map).fillna("Unknown")

# Group accident types into categories that are easier to compare.
def accident_group(t):
    if t == "Derailment": return "Derailment"
    if t in ("Hwy-rail crossing", "RR grade crossing"): return "Crossing"
    if "collision" in str(t).lower(): return "Collision"
    if t in ("Fire/violent rupture", "Explosion-detonation"): return "Fire / explosion"
    return "Other"

df["Accident Group"] = df["Accident Type"].map(accident_group)

# Group equipment types for the analysis.
def equipment_group(t):
    t = str(t)
    if t in ("Freight Train", "Cut of cars", "Single Car"): return "Freight"
    if t == "Yard/switching": return "Yard / switching"
    if any(k in t for k in ("Passenger", "Commuter", "EMU")): return "Passenger / commuter"
    return "Other (MoW, light loco...)"

df["Equipment Group"] = df["Equipment Type"].map(equipment_group)

# Separate the four border states from the rest of the country.
BORDER = {"TX", "NM", "AZ", "CA"}
df["Border State"] = np.where(df["State Abbreviation"].isin(BORDER), "Border state (TX, NM, AZ, CA)", "Rest of U.S.")

# Identify incidents on main lines versus other tracks.
df["Mainline"] = np.where(df["Track Type"] == "Main", "Main line", "Yard / industry / siding")

# Group incidents by total damage cost.
bins = [-1, 10_000, 50_000, 250_000, 1_000_000, np.inf]
labels = ["< $10K", "$10K-50K", "$50K-250K", "$250K-1M", ">= $1M"]
df["Severity Bucket"] = pd.cut(df["Total Damage Cost"], bins=bins, labels=labels).astype(str)

# Flag incidents with at least $10 million in damage.
df["Mega Event (>= $10M)"] = np.where(df["Total Damage Cost"] >= 10_000_000, "Yes", "No")

# ---------------------------------------------------------------- 4. DUPLICATE REPORTS
# Some incidents are reported by multiple railroads. Flag them instead of removing them
# so both the full report count and the unique incident count can be analyzed.
key = ["Date", "Time", "State Abbreviation", "County Name", "Milepost", "Accident Type", "Total Damage Cost"]
g = df.groupby(key, dropna=False)

# Count the reports and railroads associated with each incident.
df["Reports In Event"] = g["Date"].transform("size")
df["Railroads In Event"] = g["Reporting Railroad Name"].transform("nunique")

# Mark the first report for each incident.
df["Is Primary Report"] = (~df.duplicated(key)).astype(int)

# Label each incident based on how many reports it has.
df["Duplicate Type"] = np.select(
    [df["Reports In Event"] == 1, df["Railroads In Event"] > 1],
    ["Single report", "Joint report (several railroads)"],
    default="Repeat report (same railroad)",
)

# Calculate the duplicate counts and compare costs across both views.
qa["duplicate_rows_flagged"] = int((df["Is Primary Report"] == 0).sum())
qa["cost_all_reports"] = float(df["Total Damage Cost"].sum())
qa["cost_unique_events"] = float(df.loc[df["Is Primary Report"] == 1, "Total Damage Cost"].sum())

# ---------------------------------------------------------------- 5. EXPORT FACT TABLE
# Remove fields used only for duplicate checks and assign an ID to each row.
fact = df.drop(columns=["Time", "Other Railroad Name"]).reset_index(drop=True)
fact.insert(0, "Incident ID", fact.index + 1)
fact.to_csv(OUT / "fact_incidents.csv", index=False, encoding="utf-8-sig")

# Create a calendar table for Power BI date analysis.
cal = pd.DataFrame({"Date": pd.date_range(df["Date"].min(), df["Date"].max())})
cal["Year"], cal["Month"], cal["Month Name"] = cal["Date"].dt.year, cal["Date"].dt.month, cal["Date"].dt.strftime("%b")
cal["Month Start"] = cal["Date"].dt.to_period("M").dt.to_timestamp()
cal.to_csv(OUT / "dim_date.csv", index=False)

# ---------------------------------------------------------------- 6. HYPOTHESIS TABLES (unique events only)
# Use only the first report for each incident to avoid counting duplicates.
ev = df[df["Is Primary Report"] == 1].copy()
total_n, total_cost = len(ev), ev["Total Damage Cost"].sum()

# Summarize incident counts, costs, and casualties for each group.
def summarize(frame, by):
    out = frame.groupby(by).agg(
        incidents=("Date", "size"),
        total_cost=("Total Damage Cost", "sum"),
        median_cost=("Total Damage Cost", "median"),
        killed=("Total Persons Killed", "sum"),
        injured=("Total Persons Injured", "sum"),
    ).reset_index()
    out["share_of_incidents"] = out["incidents"] / frame.shape[0]
    out["share_of_cost"] = out["total_cost"] / frame["Total Damage Cost"].sum()
    return out.sort_values("total_cost", ascending=False)

# H1 - Compare incident frequency and damage costs across accident groups.
summarize(ev, "Accident Group").to_csv(OUT / "h1_severity_by_accident_group.csv", index=False)

# H2 - Check how much of the total damage cost comes from the most expensive incidents.
s = ev["Total Damage Cost"].sort_values(ascending=False).reset_index(drop=True)
pareto = pd.DataFrame({"rank_pct": (s.index + 1) / len(s), "cum_cost_share": s.cumsum() / s.sum()})

# Export a smaller version of the Pareto curve for easier use in Power BI.
pd.concat([pareto.iloc[:: max(1, len(pareto) // 200)], pareto.tail(1)]).drop_duplicates() \
  .to_csv(OUT / "h2_pareto_curve.csv", index=False)

# Calculate the share of total damage costs accounted for by the top incidents.
top = {f"top_{p}pct_share_of_cost": s.head(max(1, int(len(s) * p / 100))).sum() / s.sum() for p in (1, 5, 10, 20)}
pd.DataFrame([top]).to_csv(OUT / "h2_concentration_summary.csv", index=False)

# H3 - Compare cause groups and the most expensive individual causes.
summarize(ev, "Cause Group").to_csv(OUT / "h3_cause_groups.csv", index=False)
summarize(ev, "Primary Accident Cause").head(15).to_csv(OUT / "h3_top_causes_by_cost.csv", index=False)

# H4 - Compare border states with the rest of the U.S. and break results down by state.
summarize(ev, "Border State").to_csv(OUT / "h4_border_vs_rest.csv", index=False)
summarize(ev, ["State Name", "State Abbreviation"]).sort_values("incidents", ascending=False).to_csv(OUT / "h4_by_state.csv", index=False)

# Export additional tables for equipment, track type, and monthly trends.
summarize(ev, "Equipment Group").to_csv(OUT / "ctx_by_equipment_group.csv", index=False)
summarize(ev, "Mainline").to_csv(OUT / "ctx_main_vs_yard.csv", index=False)

# Keep the monthly results in chronological order.
m = summarize(ev, "Month").sort_values("Month")
m.to_csv(OUT / "ctx_monthly_trend.csv", index=False)  # 2025 ends in October, so compare months instead of annual totals.

# ---------------------------------------------------------------- 7. QA REPORT
# Save a few final checks on the cleaned data and unique incidents.
qa.update({"clean_rows": len(df), "unique_events": total_n,
           "median_cost_unique": float(ev["Total Damage Cost"].median()),
           "mean_cost_unique": float(ev["Total Damage Cost"].mean())})

pd.Series(qa).to_csv(OUT / "qa_log.csv", header=["value"])

# Print the QA results and duplicate report breakdown.
print(pd.Series(qa).to_string())
print("\nDuplicate types:\n", df.loc[df["Is Primary Report"] == 0, "Duplicate Type"].value_counts().to_string())
print("\nTables written to:", OUT.resolve())
