import pandas as pd
import numpy as np

df = pd.read_csv('C:\\Users\\Aaron\\OneDrive\\Documents\\Debut projects\\Quarterly Census of Employment and Wages.csv')

print(df.head())

cols_to_drop = ['agglvl_code', 'size_code', 'disclosure_code', 'lq_disclosure_code', 'oty_disclosure_code', 'industry_code']

df = df.drop(columns=cols_to_drop)

print(df.dtypes)
print(df.duplicated().sum())

df.to_csv('Cleaned Quarterly Census of Employment and Wages.csv', index=False)