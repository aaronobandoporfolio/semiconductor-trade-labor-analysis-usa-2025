import pandas as pd
import numpy as np

df = pd.read_csv('C:\\Users\\Aaron\\OneDrive\\Documents\\Debut projects\\Done\\Rail_Equipment_Accident_Incident_Data_(Form_54)_20260121.csv')

df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

df = df[(df['Date'] >= '1/1/2024') & (df['Date'] <= '1/1/2026')]
df = df.reset_index(drop=True)

cols_to_drop = ['Accident Number', 'Other Accident Number', 'Maintenance Accident Number', 'Division', 'Division Code', 'Other Railroad Code', 'Accident Type Code', 'Visibility Code', 'Weather Condition Code', 'Track Type Code', 'Train Direction Code', 'Equipment Type Code', 'Signalization Code', 'Method of Operation Code', 'Adjunct Code 1', 'Adjunct Code 2', 'Adjunct Code 3', 'Remote Control Locomotive Code', 'First Car Initials', 'First Car Number', 'First Car Position', 'Causing Car Initials', 'Causing Car Number', 'Causing Car Position', 'Hours Engineers On Duty', 'Minutes Engineers On Duty', 'Hours Conductors On Duty', 'Minutes Conductors On Duty', 'PDF Link', 'Incident Key', 'Report Key', 'Special Study 1', 'Special Study 2', 'County Code', 'State Code', 'Temperature', 'Visibility', 'Weather Condition', 'Other Accident Month', 'Grade Crossing ID']
df = df.drop(columns=cols_to_drop)

df = df.fillna('NaN')
df.replace('NaN', np.nan, inplace=True)

print(df.shape)
print(df.dtypes)

df.to_csv('Clean_Rail_Equipment_Accident_Incident_Data_(Form_54)_20260121.csv', index=False)