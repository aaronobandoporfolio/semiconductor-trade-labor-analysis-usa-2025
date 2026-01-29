import pandas as pd
import numpy as np

# Read the CSV file containing Quarterly Census of Employment and Wages data
df = pd.read_csv('C:\\Users\\Aaron\\OneDrive\\Documents\\Debut projects\\Quarterly Census of Employment and Wages.csv')

# Display the first 5 rows to quickly inspect the data
print(df.head())

# Define columns that are not needed and should be removed
cols_to_drop = ['agglvl_code', 'size_code', 'disclosure_code',
                'lq_disclosure_code', 'oty_disclosure_code', 'industry_code']

# Drop the unnecessary columns from the DataFrame
df = df.drop(columns=cols_to_drop)

# Print the data types of each column to check consistency
print(df.dtypes)

# Print the number of duplicated rows in the dataset
print(df.duplicated().sum())

# Save the cleaned DataFrame to a new CSV file
df.to_csv('Cleaned Quarterly Census of Employment and Wages.csv', index=False)