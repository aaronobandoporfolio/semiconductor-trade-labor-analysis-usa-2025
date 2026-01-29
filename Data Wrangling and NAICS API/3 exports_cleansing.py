import pandas as pd
import numpy as np

df = pd.read_csv('C:\\Users\\Aaron\\OneDrive\\Documents\\Debut projects\\HS 3542 Un Comtrade USA Exports.csv')

for col in ['partnerCode', 'cmdCode', 'qty', 'qtyUnitCode', 'altQtyUnitCode', 'altQty', 'fobvalue', 'primaryValue']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

cols_to_drop = ['flowCode', 'partner2Code', 'partner2ISO', 'mosCode', 'motCode', 'netWgt', 'grossWgt', 'legacyEstimationFlag', 'cifvalue', 'primaryValue', 'altQtyUnitCode', 'altQtyUnitAbbr', 'altQty']
df = df.drop(columns=cols_to_drop)

df.to_csv('Cleaned_HS_3542_Un_Comtrade_USA_Exports.csv', index=False)