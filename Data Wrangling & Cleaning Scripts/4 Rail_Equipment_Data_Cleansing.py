import pandas as pd
import numpy as np

# Read the CSV file containing rail equipment accident/incident data
df = pd.read_csv('C:\\Users\\Aaron\\OneDrive\\Documents\\Debut projects\\Done\\Rail_Equipment_Accident_Incident_Data_(Form_54)_20260121.csv')

# Convert the 'Date' column to datetime format (invalid values become NaT)
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Keep only rows where the date is between Jan 1, 2024 and Jan 1, 2026
df = df[(df['Date'] >= '1/1/2024') & (df['Date'] <= '1/1/2026')]

# Reset the index after filtering
df = df.reset_index(drop=True)

# Define columns that are not needed and should be removed
cols_to_drop = [
    'Accident Number', 'Other Accident Number', 'Maintenance Accident Number',
    'Division', 'Division Code', 'Other Railroad Code', 'Accident Type Code',
    'Visibility Code', 'Weather Condition Code', 'Track Type Code',
    'Train Direction Code', 'Equipment Type Code', 'Signalization Code',
    'Method of Operation Code', 'Adjunct Code 1', 'Adjunct Code 2', 'Adjunct Code 3',
    'Remote Control Locomotive Code', 'First Car Initials', 'First Car Number',
    'First Car Position', 'Causing Car Initials', 'Causing Car Number',
    'Causing Car Position', 'Hours Engineers On Duty', 'Minutes Engineers On Duty',
    'Hours Conductors On Duty', 'Minutes Conductors On Duty', 'PDF Link',
    'Incident Key', 'Report Key', 'Special Study 1', 'Special Study 2',
    'County Code', 'State Code', 'Temperature', 'Visibility', 'Weather Condition',
    'Other Accident Month', 'Grade Crossing ID'
]

# Drop the unnecessary columns from the DataFrame
df = df.drop(columns=cols_to_drop)

# Temporarily fill missing values with the string 'NaN'
df = df.fillna('NaN')

# Replace the string 'NaN' back with actual np.nan values
df.replace('NaN', np.nan, inplace=True)

# Print the shape (rows, columns) of the DataFrame
print(df.shape)

# Print the data types of each column
print(df.dtypes)

# Save the cleaned DataFrame to a new CSV file
df.to_csv('Clean_Rail_Equipment_Accident_Incident_Data_(Form_54)_20260121.csv', index=False)