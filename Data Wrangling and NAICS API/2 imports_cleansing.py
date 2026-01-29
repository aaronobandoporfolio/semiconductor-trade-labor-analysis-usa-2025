import pandas as pd
import numpy as np

df = pd.read_csv("TradeData_1_21_2026_21_51_10.csv")

# Convertir columnas numéricas
for col in ["qty","altQty","netWgt","grossWgt","cifvalue","fobvalue","primaryValue"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Normalizar qty
def normalize_qty(row):
    unit = row["altQtyUnitAbbr"] if row["altQtyUnitAbbr"] != "N/A" else row["qtyUnitAbbr"]
    qty = row["qty"]
    if unit == "u":
        return qty
    elif unit == "1000u":
        return qty * 1000
    elif unit == "kg":
        return qty
    else:
        return np.nan

df["qty_standard"] = df.apply(normalize_qty, axis=1)
df["qty_kg"] = df["netWgt"]
df['qty_kg'] = df['netWgt'].replace(np.nan, 0)

# Convertir booleanos
df["isNetWgtEstimated"] = df["isNetWgtEstimated"].astype(str).str.upper().map({"TRUE": True, "FALSE": False})
df["data_quality"] = df["isNetWgtEstimated"].map({True:"Estimated", False:"Reported"})

# Limpieza selectiva
critical_cols = ["reporterISO","motDesc","qty","cifvalue"]
df = df.dropna(subset=critical_cols, how="all")

# Rellenar solo numéricas
num_cols = ["qty","altQty","netWgt","grossWgt","cifvalue","fobvalue","primaryValue","qty_standard","qty_kg"]
df[num_cols] = df[num_cols].fillna(0)

text_cols = ["qtyUnitAbbr","altQtyUnitAbbr","motDesc","partnerDesc"]
df[text_cols] = df[text_cols].replace('N/A', 'Unknown').fillna('Unknown')

df = df.drop_duplicates()

print(df.describe(), df.shape, df.info())

df.to_csv('Cleaned Imports USA.csv', index=False)