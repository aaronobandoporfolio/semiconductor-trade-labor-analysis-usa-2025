import pandas as pd

df = pd.read_csv('C:\\Users\\Aaron\\OneDrive\\Documents\\Debut projects\\Occupational Employment and Wage Statistics (OEWS).txt', sep='\t')
print(df.head())

col_to_drop = 'footnote_codes'
df = df.drop(columns=col_to_drop)

print(df.duplicated().sum())

df.to_csv('Clean Occupational Employment and Wage Statistics (OEWS).txt', sep='\t', index=False)