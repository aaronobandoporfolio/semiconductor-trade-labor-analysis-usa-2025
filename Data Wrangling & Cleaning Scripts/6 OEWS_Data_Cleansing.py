import pandas as pd

# Read the OEWS dataset from a tab-delimited text file
df = pd.read_csv('C:\\Users\\Aaron\\OneDrive\\Documents\\Debut projects\\Occupational Employment and Wage Statistics (OEWS).txt', sep='\t')

# Display the first 5 rows to quickly inspect the data
print(df.head())

# Define the column to drop (not needed for analysis)
col_to_drop = 'footnote_codes'

# Remove the unnecessary column from the DataFrame
df = df.drop(columns=col_to_drop)

# Print the number of duplicated rows in the dataset
print(df.duplicated().sum())

# Save the cleaned DataFrame back to a tab-delimited text file
df.to_csv('Clean Occupational Employment and Wage Statistics (OEWS).txt', sep='\t', index=False)