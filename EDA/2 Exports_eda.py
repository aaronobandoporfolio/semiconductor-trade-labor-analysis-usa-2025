#Import necessary libraries for data manipulation, visualization, and stats
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency

# Load the cleaned export data
#Note: Using Latin1 encoding to handle special characters in country names
df = pd.read_csv('C:\\Users\\Aaron\\OneDrive\\Documents\\Debut projects\\2 Cleaned data\\Cleaned_HS_3542_Un_Comtrade_USA_Exports.csv', encoding='Latin1')

# Initial data exploration
print(df.head())  # View first 5 rows
print(df.shape, df.describe(include='all'), df.info())  # Shape, summary stats, and data types

#check unique importing countries
print(df['partnerISO'].unique())

#Convert key columns to numeric (handling any non-numeric values)
for col in ['fobvalue','refYear', 'reporterCode']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Create histogram showing frequency distribution of export values
ax1 = sns.histplot(df['fobvalue'], bins=30)

# Add count labels on top of each bar for clarity
for p in ax1.patches:
    height = p.get_height()
    if height > 0:
        ax1.text(p.get_x() + p.get_width() / 2, height, int(height),
                ha='center', va='bottom', fontsize='8', rotation=0)

#Format the plot
plt.grid(axis='y', linestyle='--')  # Add horizontal gridlines
plt.ticklabel_format(style='plain', axis='x')  # Display x-axis numbers without scientific notation
plt.show()
plt.close()

# Create categorical variable by splitting FOB values into 3 equal-sized groups
df['fob_cat'] = pd.qcut(df['fobvalue'], q=3, labels=['Low', 'Medium', 'High'])

# Build contingency table: rows = countries, columns = FOB categories
contingency = pd.crosstab(df['partnerISO'], df['fob_cat'])

# Perform chi-square test to see if country and export value category are independent
chi2, p, dof, expected = chi2_contingency(contingency)

#Print test results
print('Chi-Square Statistic: ', chi2)
print('P-value: ', p)
print('Degrees of Freedom: ', dof)
print('Expected Frequencies: ', expected)

# The Results:
# Chi-Square Statistic: 1431.93
# - This is EXTREMELY high, suggesting a massive difference between 
#   observed and expected frequencies

# P-value: 5.14e-153 (basically 0.0000...153 zeros...0514)
# - This is astronomically small (way below the typical 0.05 threshold)
# - It means there's virtually no chance these results happened by random chance
# - We can confidently REJECT the null hypothesis

# Degrees of Freedom: 282
# - This comes from (rows - 1) × (columns - 1)
# - Suggests we're testing 95 rows × 3 columns of categorical data

# Expected Frequencies:
# - These are the frequencies we'd expect if the variables were independent
# - The actual observed data must be VERY different from these expected values
# - Most expected frequencies are around 0.33, 1.0, 2.0, or 3.33

# Bottom Line:
# There is a HIGHLY SIGNIFICANT relationship between the variables being tested.
# Whatever pattern exists in the data is NOT due to random chance.

# Chi-Square Test Results
# Chi-Square Statistic: 1431.926727695031
# P-value: 5.140167911772863e-153
# Degrees of Freedom: 282

# Expected Frequencies Array:
# [[0.33368421 0.33263158 0.33368421]
#  [1.33473684 1.33052632 1.33473684]
#  [1.00105263 0.99789474 1.00105263]
#  [0.66736842 0.66526316 0.66736842]
#  [1.00105263 0.99789474 1.00105263]
#  [3.33684211 3.32631579 3.33684211]
#  [0.66736842 0.66526316 0.66736842]
#  [1.33473684 1.33052632 1.33473684]
#  [3.33684211 3.32631579 3.33684211]
#  [3.33684211 3.32631579 3.33684211]
#  [0.33368421 0.33263158 0.33368421]
#  [1.66842105 1.66315789 1.66842105]
#  [2.33578947 2.32842105 2.33578947]
#  [1.00105263 0.99789474 1.00105263]
#  [3.00315789 2.99368421 3.00315789]
#  [3.33684211 3.32631579 3.33684211]
#  [0.66736842 0.66526316 0.66736842]
#  [2.33578947 2.32842105 2.33578947]
#  [3.33684211 3.32631579 3.33684211]
#  [0.66736842 0.66526316 0.66736842]
#  [3.33684211 3.32631579 3.33684211]
#  [0.33368421 0.33263158 0.33368421]
#  [3.33684211 3.32631579 3.33684211]
#  [0.66736842 0.66526316 0.66736842]
#  [3.33684211 3.32631579 3.33684211]
#  [3.00315789 2.99368421 3.00315789]
#  [3.33684211 3.32631579 3.33684211]
#  [3.33684211 3.32631579 3.33684211]
#  [3.33684211 3.32631579 3.33684211]
#  [2.33578947 2.32842105 2.33578947]
#  [3.33684211 3.32631579 3.33684211]
#  [0.33368421 0.33263158 0.33368421]
#  [3.33684211 3.32631579 3.33684211]
#  [3.33684211 3.32631579 3.33684211]
#  [2.00210526 1.99578947 2.00210526]
#  [1.00105263 0.99789474 1.00105263]
#  [3.33684211 3.32631579 3.33684211]
#  [3.33684211 3.32631579 3.33684211]
#  [0.33368421 0.33263158 0.33368421]
#  [3.33684211 3.32631579 3.33684211]
#  [3.33684211 3.32631579 3.33684211]
#  [2.66947368 2.66105263 2.66947368]
#  [3.33684211 3.32631579 3.33684211]
#  [1.33473684 1.33052632 1.33473684]
#  [3.33684211 3.32631579 3.33684211]
#  [0.33368421 0.33263158 0.33368421]
#  [0.66736842 0.66526316 0.66736842]
#  [0.33368421 0.33263158 0.33368421]
#  [3.33684211 3.32631579 3.33684211]
#  [3.33684211 3.32631579 3.33684211]
#  [0.33368421 0.33263158 0.33368421]
#  [3.33684211 3.32631579 3.33684211]
#  [3.33684211 3.32631579 3.33684211]
#  [1.33473684 1.33052632 1.33473684]
#  [3.33684211 3.32631579 3.33684211]
#  [2.00210526 1.99578947 2.00210526]
#  [0.33368421 0.33263158 0.33368421]
#  [3.33684211 3.32631579 3.33684211]
#  [3.33684211 3.32631579 3.33684211]
#  [1.33473684 1.33052632 1.33473684]
#  [3.33684211 3.32631579 3.33684211]
#  [3.33684211 3.32631579 3.33684211]
#  [1.66842105 1.66315789 1.66842105]
#  [3.33684211 3.32631579 3.33684211]
#  [3.33684211 3.32631579 3.33684211]
#  [3.33684211 3.32631579 3.33684211]
#  [2.00210526 1.99578947 2.00210526]
#  [3.33684211 3.32631579 3.33684211]
#  [1.00105263 0.99789474 1.00105263]
#  [2.00210526 1.99578947 2.00210526]
#  [1.00105263 0.99789474 1.00105263]
#  [3.00315789 2.99368421 3.00315789]
#  [0.33368421 0.33263158 0.33368421]
#  [3.33684211 3.32631579 3.33684211]
#  [1.66842105 1.66315789 1.66842105]
#  [0.33368421 0.33263158 0.33368421]
#  [3.33684211 3.32631579 3.33684211]
#  [2.66947368 2.66105263 2.66947368]
#  [0.33368421 0.33263158 0.33368421]
#  [0.33368421 0.33263158 0.33368421]
#  [3.33684211 3.32631579 3.33684211]
#  [0.66736842 0.66526316 0.66736842]
#  [3.00315789 2.99368421 3.00315789]
#  [1.66842105 1.66315789 1.66842105]
#  [3.33684211 3.32631579 3.33684211]
#  [0.33368421 0.33263158 0.33368421]
#  [1.66842105 1.66315789 1.66842105]
#  [1.66842105 1.66315789 1.66842105]
#  [0.66736842 0.66526316 0.66736842]
#  [3.33684211 3.32631579 3.33684211]
#  [3.33684211 3.32631579 3.33684211]
#  [3.33684211 3.32631579 3.33684211]
#  [2.00210526 1.99578947 2.00210526]
#  [1.00105263 0.99789474 1.00105263]
#  [3.33684211 3.32631579 3.33684211]
#  [2.00210526 1.99578947 2.00210526]
#  [3.33684211 3.32631579 3.33684211]
#  [1.33473684 1.33052632 1.33473684]
#  [3.33684211 3.32631579 3.33684211]
#  [0.33368421 0.33263158 0.33368421]
#  [3.33684211 3.32631579 3.33684211]
#  [3.33684211 3.32631579 3.33684211]
#  [3.33684211 3.32631579 3.33684211]
#  [3.33684211 3.32631579 3.33684211]
#  [3.33684211 3.32631579 3.33684211]
#  [3.33684211 3.32631579 3.33684211]
#  [3.33684211 3.32631579 3.33684211]
#  [0.66736842 0.66526316 0.66736842]
#  [0.33368421 0.33263158 0.33368421]
#  [1.00105263 0.99789474 1.00105263]
#  [0.33368421 0.33263158 0.33368421]
#  [3.33684211 3.32631579 3.33684211]
#  [0.33368421 0.33263158 0.33368421]
#  [3.33684211 3.32631579 3.33684211]
#  [3.33684211 3.32631579 3.33684211]
#  [1.00105263 0.99789474 1.00105263]
#  [3.33684211 3.32631579 3.33684211]
#  [3.33684211 3.32631579 3.33684211]
#  [3.33684211 3.32631579 3.33684211]
#  [3.33684211 3.32631579 3.33684211]
#  [3.33684211 3.32631579 3.33684211]
#  [3.33684211 3.32631579 3.33684211]
#  [1.33473684 1.33052632 1.33473684]
#  [0.66736842 0.66526316 0.66736842]
#  [3.33684211 3.32631579 3.33684211]
#  [3.33684211 3.32631579 3.33684211]
#  [3.33684211 3.32631579 3.33684211]
#  [3.00315789 2.99368421 3.00315789]
#  [2.33578947 2.32842105 2.33578947]
#  [1.00105263 0.99789474 1.00105263]
#  [3.33684211 3.32631579 3.33684211]
#  [0.66736842 0.66526316 0.66736842]
#  [3.33684211 3.32631579 3.33684211]
#  [3.33684211 3.32631579 3.33684211]
#  [3.33684211 3.32631579 3.33684211]
#  [3.33684211 3.32631579 3.33684211]
#  [1.00105263 0.99789474 1.00105263]
#  [0.66736842 0.66526316 0.66736842]
#  [2.66947368 2.66105263 2.66947368]
#  [3.33684211 3.32631579 3.33684211]
#  [0.33368421 0.33263158 0.33368421]
#  [1.00105263 0.99789474 1.00105263]]


#Extract all country names from the contingency table index
Countries = contingency.index.tolist()

#Loop through countries in groups of 10 to create manageable heatmaps
for i in range(0, len(Countries), 10):
    group = Countries[i:i+10]  # Select 10 countries at a time
    subset = contingency.loc[group]  # Filter contingency table for this group
    
    #Create heatmap visualization
    plt.figure(figsize=(12, 6))
    sns.heatmap(subset, annot=True, fmt='d', cmap='Greens')  # annot=True shows values, fmt='d' for integers
    plt.title('Contingency Table: Importer Country Vs FOB Category')
    plt.xlabel('FOB Category')
    plt.ylabel('Importer Country')
    plt.show()
    plt.close()


#Full list of all importing countries (142 total)
Countries_list = [
    'Antigua and Barbuda', 'Argentina', 'Australia', 'Austria', 'Bahrain',
    'Bangladesh', 'Armenia', 'Barbados', 'Belgium', 'Bermuda', 'Bolivia', 'Brazil',
    'Bulgaria', 'Canada', 'Cayman Isds', 'Sri Lanka', 'Chile', 'China', 'Colombia',
    'Costa Rica', 'Croatia', 'Czechia', 'Denmark', 'Dominican Republic', 'Ecuador',
    'El Salvador', 'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Guatemala',
    'Guyana', 'Honduras', 'China, Hong Kong', 'Hungary', 'Indonesia', 'Iraq',
    'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Kazakhstan', 'South Korea',
    'Kuwait', 'Latvia', 'Lithuania', 'Luxembourg', 'Malawi', 'Malaysia', 'Malta',
    'Mexico', 'Other Asia, nes', 'Namibia', 'Nepal', 'Netherlands', 'Curaçao',
    'New Zealand', 'Nicaragua', 'Norway', 'Panama', 'Paraguay', 'Peru',
    'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Rwanda',
    'St. Kitts and Nevis', 'Saint Lucia', 'Saudi Arabia', 'Senegal', 'Serbia',
    'India', 'Singapore', 'Slovakia', 'Viet Nam', 'Slovenia', 'South Africa',
    'Spain', 'Sweden', 'Switzerland', 'Thailand', 'Trinidad and Tobago',
    'United Arab Emirates', 'Tunisia', 'Türkiye', 'Ukraine', 'Egypt',
    'United Kingdom', 'Uruguay', 'Uzbekistan', 'Venezuela', 'Zambia',
    'Bosnia Herzegovina', 'Cambodia', 'Djibouti', 'Jordan', 'Kenya', 'Mali',
    'Mauritius', 'Oman', 'Sint Maarten', 'Turks and Caicos Isds', 'Uganda',
    'Cyprus', 'Equatorial Guinea', 'Iceland', 'Morocco', 'Aruba', 'Vanuatu',
    'Nigeria', 'Russian Federation', 'Eswatini', 'North Macedonia', 'Bahamas',
    'Grenada', 'Kyrgyzstan', 'China, Macao', 'Mongolia', 'Brunei Darussalam',
    'Congo', 'Madagascar', 'Pakistan', 'San Marino', 'Albania', 'Lebanon',
    'FS Micronesia', 'Papua New Guinea', 'Algeria', 'Angola', 'Belize', 'Anguilla',
    'St. Vincent and the Grenadineses', 'Georgia', 'Yemen', 'Azerbaijan',
    'Ethiopia', 'Liberia', 'Haiti']


# Open file to save boxplot statistics
with open('boxplt_stats.txt', 'w') as f:
    # Process countries in groups of 10
    for i in range(0, len(Countries_list), 10):
        group = Countries_list[i:i+10]  # Current group of 10 countries
        subset = df[df['partnerISO'].isin(group)]  # Filter data for these countries
        
        # Skip if no data exists for this group
        if subset.empty:
            continue
        
        # Create boxplot showing FOB value distribution for each country
        plt.figure(figsize=(12, 6))
        sns.boxplot(x='partnerISO', y='fobvalue', data=subset)
        plt.title('Distribution of FOB by Importer Country')
        plt.xlabel('Importer')
        plt.ylabel('FOB')
        plt.ticklabel_format(style='plain', axis='y')  #Avoid scientific notation
        plt.grid(axis='y', linestyle='--')
        plt.tight_layout()
        plt.show()
        plt.close()

        # Calculate detailed statistics for each country in the group
        stats = {}
        for country in group:
            values = subset.loc[subset['partnerISO'] == country, 'fobvalue']
            
            if values.empty:
                continue
            
            # Calculate boxplot statistics manually
            q1 = np.percentile(values, 25)  #First quartile (25th percentile)
            q2 = np.percentile(values, 50)  #Median (50th percentile)
            q3 = np.percentile(values, 75)  #Third quartile (75th percentile)
            iqr = q3 - q1  #Interquartile range
            
            # Whiskers extend to 1.5*IQR from quartiles
            lower_whisker = values[values >= (q1 - 1.5 * iqr)].min()
            upper_whisker = values[values <= (q3 + 1.5 * iqr)].max()
            
            #Identify outliers (values beyond whiskers)
            outliers = values[(values < (q1 - 1.5 * iqr)) | (values > (q3 + 1.5 * iqr))]

            #Store stats in dictionary
            stats[country] = {
                'count': len(values),
                'Q1': q1,
                'Median': q2,
                'Q3': q3,
                'Lower Whisker': lower_whisker,
                'Upper Whisker': upper_whisker,
                'Outliers': outliers.tolist()
            }
        
        # Print stats to console
        print(f'\nGroup {i//10 + 1} boxplot stats:\n')
        for country, s in stats.items():
            print(country, s)

        # Write stats to file
        f.write(f'\nGroup {i//10 + 1} ({group})\n')
        for country, s in stats.items():
            f.write(f'{country}: {s}\n')
        f.write('\n' + '-'*60 + '\n')


# Open file to save line plot statistics
with open("lineplot_stats.txt", "w") as f:
    # Process countries in groups of 10
    for i in range(0, len(Countries_list), 10):
        group = Countries_list[i:i+10]  #Current group of 10 countries
        subset = df[df['partnerISO'].isin(group)]  #Filter data for these countries

        # Skip if no data exists for this group
        if subset.empty:
            print(f"Skipping Group {i//10 + 1}: no data")
            continue

        # Create line plot showing FOB trends over months
        plt.figure(figsize=(12, 6))
        ax = sns.lineplot(x='refMonth', y='fobvalue', hue='partnerISO', data=subset)

        #Calculate time series statistics for each country
        stats = {}
        for country in group:
            country_data = subset[subset['partnerISO'] == country]

            if country_data.empty:
                continue

            #Sort by month to ensure chronological order
            country_data = country_data.sort_values("refMonth")

            #Create dictionary of month-to-value mappings
            month_values = {
                str(m): int(v)
                for m, v in zip(country_data["refMonth"], country_data["fobvalue"])
                if v > 0  #Only include non-zero values
            }

            if not month_values:
                continue

            # Store key time series stats
            stats[country] = {
                "first": int(country_data["fobvalue"].iloc[0]),  # First month value
                "max": int(country_data["fobvalue"].max()),      #Maximum value
                "last": int(country_data["fobvalue"].iloc[-1]),  # Last month value
                "per_month": month_values                        # All monthly values
            }

        # Annotate key points on each line (first, max, last)
        for line in ax.lines:
            x_data = line.get_xdata()
            y_data = line.get_ydata()
            
            if len(x_data) > 0:
                # Label first point
                ax.text(x_data[0], y_data[0], f'{int(y_data[0]):,}',
                        ha='center', va='bottom', fontsize=6, rotation=45)
                
                # Label maximum point
                max_idx = y_data.argmax()
                ax.text(x_data[max_idx], y_data[max_idx], f'{int(y_data[max_idx]):,}',
                        ha='center', va='bottom', fontsize=6, rotation=45)
                
                # Label last point
                ax.text(x_data[-1], y_data[-1], f'{int(y_data[-1]):,}',
                        ha='center', va='bottom', fontsize=6, rotation=45)

        #Format and display plot
        plt.title(f'FOB Value Over Time By Importer Country (Group {i//10 + 1})')
        plt.ticklabel_format(style='plain', axis='y')  # Avoid scientific notation
        plt.grid(axis='y', linestyle='--')
        plt.xlabel('Month')
        plt.ylabel('FOB')
        plt.tight_layout()
        plt.show()
        plt.close()

        #Print stats to console
        print(f"\nGroup {i//10 + 1} lineplot stats:")
        for country, s in stats.items():
            print(country)
            print("  First:", s["first"])
            print("  Max:", s["max"])
            print("  Last:", s["last"])
            print("  Per month:", s["per_month"])

        #write stats to file
        f.write(f"\nGroup {i//10 + 1} ({group})\n")
        for country, s in stats.items():
            f.write(f"{country}\n")
            f.write(f"  First: {s['first']}\n")
            f.write(f"  Max: {s['max']}\n")
            f.write(f"  Last: {s['last']}\n")
            f.write("  Per month:\n")
            for month, val in s["per_month"].items():
                f.write(f"    {month}: {val}\n")
        f.write("\n" + "-"*60 + "\n")