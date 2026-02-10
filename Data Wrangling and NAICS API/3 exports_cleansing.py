import pandas as pd
import numpy as np

# Read the CSV file containing USA export trade data
df = pd.read_csv("C:\\Users\\Aaron\\OneDrive\\Documents\\Debut projects\\1 Done\\HS 3542 Un Comtrade USA Exports.csv", encoding='Latin1')

# Convert selected columns to numeric values (if conversion fails, set as NaN)
for col in ['partnerCode', 'cmdCode', 'qty', 'qtyUnitCode', 'altQtyUnitCode', 'altQty', 'fobvalue', 'primaryValue']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Define columns that are not needed and should be removed
cols_to_drop = [
    'flowCode', 'partner2Code', 'partner2ISO', 'mosCode', 'motCode',
    'netWgt','period','grossWgt', 'legacyEstimationFlag', 'cifvalue',
    'primaryValue', 'altQtyUnitCode', 'altQtyUnitAbbr', 'altQty', 
    'isAltQtyEstimated', 'motDesc', 'customsDesc', 'isGrossWgtEstimated', 
    'isNetWgtEstimated', 'qty', 'qtyUnitCode', 'isAggregate', 
    'cmdCode', 'partnerCode', 'reporterISO', 'isReported',
    'partner2Desc', 'isQtyEstimated'
]


# Drop the unnecessary columns from the DataFrame
df = df.drop(columns=cols_to_drop)

df = df.loc[df['partnerISO'] != 'World']

df['reporterDesc'] = df['reporterDesc'].replace('USA', 'United States')

# Save the cleaned DataFrame to a new CSV file
df.to_csv('Cleaned_HS_3542_Un_Comtrade_USA_Exports.csv', index=False)

