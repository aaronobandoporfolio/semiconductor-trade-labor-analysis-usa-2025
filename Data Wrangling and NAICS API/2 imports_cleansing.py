import pandas as pd
import numpy as np

# Read the CSV file containing trade data
df = pd.read_csv("Done//TradeData_1_21_2026_21_51_10.csv")

# Convert selected columns to numeric (floats); if conversion fails, set as NaN
for col in ["qty","altQty","netWgt","grossWgt","cifvalue","fobvalue","primaryValue"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Function to normalize quantity based on unit type
def normalize_qty(row):
    # Use altQtyUnitAbbr if available, otherwise use qtyUnitAbbr
    unit = row["altQtyUnitAbbr"] if row["altQtyUnitAbbr"] != "N/A" else row["qtyUnitAbbr"]
    qty = row["qty"]
    # If unit is "u" → keep as is
    if unit == "u":
        return qty
    # If unit is "1000u" → multiply by 1000
    elif unit == "1000u":
        return qty * 1000
    # If unit is "kg" → keep as is
    elif unit == "kg":
        return qty
    # If unit is not recognized → return NaN
    else:
        return np.nan

# Create a new column with normalized quantity
df["qty_standard"] = df.apply(normalize_qty, axis=1)

# Create a column with quantity in kilograms (use netWgt, replace NaN with 0)
df["qty_kg"] = df["netWgt"]
df['qty_kg'] = df['netWgt'].replace(np.nan, 0)

# Convert boolean column to True/False values
df["isNetWgtEstimated"] = df["isNetWgtEstimated"].astype(str).str.upper().map({"TRUE": True, "FALSE": False})

# Create a more readable column for data quality
df["data_quality"] = df["isNetWgtEstimated"].map({True:"Estimated", False:"Reported"})

# Drop rows where all critical columns are missing
critical_cols = ["reporterISO","motDesc","qty","cifvalue"]
df = df.dropna(subset=critical_cols, how="all")

# Drop redundant/irrelevant columns to streamline dataset
cols_to_drop = ['primaryValue', 'partner2Code', 'partner2ISO', 'partner2Desc', 'grossWgt', 'mosCode']
df = df.drop(columns=cols_to_drop)

# Fill missing values in numeric columns with 0
num_cols = ["qty","altQty","netWgt","cifvalue","fobvalue","qty_standard","qty_kg"]
df[num_cols] = df[num_cols].fillna(0)

# Replace missing or 'N/A' values in text columns with "Unknown"
text_cols = ["qtyUnitAbbr","altQtyUnitAbbr","motDesc","partnerDesc"]
df[text_cols] = df[text_cols].replace('N/A', 'Unknown').fillna('Unknown')

# Remove duplicate rows
df = df.drop_duplicates()

# Print statistical summary, shape, and info about the DataFrame
print(df.describe(), df.shape, df.info())

# Save the cleaned DataFrame to a new CSV file
df.to_csv('Cleaned Imports USA.csv', index=False)
