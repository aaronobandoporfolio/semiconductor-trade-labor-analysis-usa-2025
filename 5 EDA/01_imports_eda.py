import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency

pd.set_option('display.float_format', '{:,.2f}'.format)

# Load data
df = pd.read_csv('C:\\Users\\Aaron\\OneDrive\\Documents\\Debut projects\\Cleaned data\\Cleaned Imports USA.csv')

print(df.head(), df.info(), df.dtypes, df.shape, df.describe(include='all'))

# Convert columns to numeric
for col in ['cifvalue', 'fobvalue', 'netWgt', 'qty', 'altQty', 'refMonth', 'refYear']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Calculate value per unit
df['value_per_unit'] = df['cifvalue']/df['qty'].replace(0, np.nan)
print(df['value_per_unit'].head())

# Filter out zero values
df_clean = df[df['cifvalue'] > 0] 

# Histogram of CIF Values (Linear Scale)
ax1 = sns.histplot(df_clean['cifvalue'], bins=30)
for p in ax1.patches:
    height = p.get_height()
    if height > 0:
        ax1.text(p.get_x() + p.get_width() / 2, height, int(height),
                ha='center', va='bottom', fontsize=8, rotation=0)
plt.grid(axis='y', linestyle='--')
plt.ticklabel_format(style='plain', axis='x')
plt.show()
plt.close()

# Histogram of CIF Values (Logarithmic Scale)
ax2 = sns.histplot(df_clean['cifvalue'], bins=30, log_scale=True)
for p in ax2.patches:
    height = p.get_height()
    if height > 0:
        ax2.text(p.get_x() + p.get_width() / 2, height, int(height),
                ha='center', va='bottom', fontsize=8, rotation=0)
plt.show()
plt.close()

# Chi-square test: relationship between exporter country and CIF value category
df['ci_cat'] = pd.qcut(df['cifvalue'][df['cifvalue']>0], q=3, labels=['Low', 'Medium', 'High'])
contingency = pd.crosstab(df['reporterDesc'], df['ci_cat'])

chi2, p, dof, expected = chi2_contingency(contingency)
print('Chi-Square Statistic: ', chi2)
print('P-value: ', p)
print('Degrees of Freedom: ', dof)
print('Excepted Frequencies: ', expected)

# Heatmap of contingency table
plt.figure(figsize=(12, 8))
sns.heatmap(contingency, annot=True, fmt='d', cmap='Blues')
plt.title('Contingency Table: Exporter Country Vs CIF Category')
plt.xlabel('CIF Category')
plt.ylabel('Exporter Country')
plt.show()
plt.close()

# Boxplot: CIF value by exporter (with Malaysia)
plt.figure(figsize=(12,6))
sns.boxplot(x='reporterDesc', y='cifvalue', data=df_clean)
plt.title('Distribution of CIF Value by Exporter Country')
plt.xlabel('Exporters')
plt.ylabel('CIF')
plt.ticklabel_format(style='plain', axis='y')
plt.grid(axis='y', linestyle='--')
plt.tight_layout()
plt.show()
plt.close()

# Boxplot: CIF value by exporter (excluding Malaysia)
df_no_malaysia = df_clean[df_clean['reporterISO'] != 'MYS']
plt.figure(figsize=(12, 6))
sns.boxplot(x='reporterDesc', y='cifvalue', data=df_no_malaysia)
plt.title('Distribution of CIF Value by Exporter Country (Excluding Malaysia)')
plt.xticks(rotation=90)
plt.ticklabel_format(style='plain', axis='y')
plt.grid(axis='y', linestyle='--')
plt.show()
plt.close()

import calendar

# Create month names
df_clean = df[df['cifvalue'] > 0].copy()
df_clean['month_name'] = df_clean['refMonth'].apply(lambda x: calendar.month_abbr[int(x)])
df_no_malaysia = df_clean[df_clean['reporterISO'] != 'MYS']

# Line plot: CIF value over time by country (with Malaysia)
plt.figure(figsize=(12,8))
ax3 = sns.lineplot(x='month_name', y='cifvalue', hue='reporterDesc', data=df_clean, marker='o')

# Add labels for first, max, and last points
for line in ax3.lines:
    x_data = line.get_xdata()
    y_data = line.get_ydata()
    if len(x_data) > 0:
        ax3.text(x_data[0], y_data[0], f'{int(y_data[0]):,}',
                ha='center', va='bottom', fontsize=6, rotation=45)
        max_idx = y_data.argmax()
        ax3.text(x_data[max_idx], y_data[max_idx], f'{int(y_data[max_idx]):,}',
                ha='center', va='bottom', fontsize=6, rotation=45)
        ax3.text(x_data[-1], y_data[-1], f'{int(y_data[-1]):,}',
                ha='center', va='bottom', fontsize=6, rotation=45)

plt.title('CIF Value Over Time by Exporter Country')
plt.ticklabel_format(style='plain', axis='y')
plt.grid(axis='y', linestyle='--')
plt.xlabel('Months (2025)')
plt.ylabel('CIF')
plt.show()
plt.close()

# Line plot: CIF value over time (excluding Malaysia)
plt.figure(figsize=(12,8))
ax4 = sns.lineplot(x='month_name', y='cifvalue', hue='reporterDesc', data=df_no_malaysia, marker='o')

for line in ax4.lines:
    x_data = line.get_xdata()
    y_data = line.get_ydata()
    if len(x_data) > 0:
        ax4.text(x_data[0], y_data[0], f'{int(y_data[0]):,}',
                ha='center', va='bottom', fontsize=6, rotation=45)
        max_idx = y_data.argmax()
        ax4.text(x_data[max_idx], y_data[max_idx], f'{int(y_data[max_idx]):,}',
                ha='center', va='bottom', fontsize=6, rotation=45)
        ax4.text(x_data[-1], y_data[-1], f'{int(y_data[-1]):,}',
                ha='center', va='bottom', fontsize=6, rotation=45)

plt.title('CIF Value Trend Over Time (Excluding Malaysia)')
plt.xticks(rotation=45)
plt.ticklabel_format(style='plain', axis='y')
plt.grid(axis='y', linestyle='--')
plt.xlabel('Months (2025)')
plt.ylabel('CIF')
plt.show()
plt.close()

# Line plot: Focus on Malaysia, Japan, and Hong Kong
df_focus = df_clean[df_clean['reporterISO'].isin(['MYS','JPN','HKG'])]

plt.figure(figsize=(12, 8))
ax5 = sns.lineplot(x='month_name', y='cifvalue', hue='reporterDesc', data=df_focus, marker='o')

for line in ax5.lines:
    x_data = line.get_xdata()
    y_data = line.get_ydata()
    if len(x_data) > 0:
        ax5.text(x_data[0], y_data[0], f'{int(y_data[0]):,}',
                ha='center', va='bottom', fontsize=6, rotation=45)
        max_idx = y_data.argmax()
        ax5.text(x_data[max_idx], y_data[max_idx], f'{int(y_data[max_idx]):,}',
                ha='center', va='bottom', fontsize=6, rotation=45)
        ax5.text(x_data[-1], y_data[-1], f'{int(y_data[-1]):,}',
                ha='center', va='bottom', fontsize=6, rotation=45)

plt.title('CIF Value Over Time: Malaysia vs Japan vs Hong Kong')
plt.xticks(rotation=45)
plt.ticklabel_format(style='plain', axis='y')
plt.grid(axis='y', linestyle='--')
plt.xlabel('Months (2025)')
plt.ylabel('CIF')
plt.show()
plt.close()

# Bar plot: CIF value by country and mode of transport
plt.figure(figsize=(12, 6))
transport_values = df_clean.groupby(['reporterDesc', 'motDesc'], dropna=True)['cifvalue'].sum().reset_index()
transport_values = transport_values[transport_values['motDesc'].notna()]
transport_values = transport_values[transport_values['motDesc'] != 'TOTAL MOT']

ax6 = sns.barplot(x='reporterDesc', y='cifvalue', hue='motDesc', data=transport_values)

for p in ax6.patches:
    height = p.get_height()
    if height > 0:
        ax6.text(p.get_x() + p.get_width() / 2, height, f'{int(height):,}',
                ha='center', va='bottom', fontsize=8, rotation=0)

plt.ticklabel_format(style='plain', axis='y')
plt.grid(axis='y', linestyle='--')
plt.xticks(rotation=90)
plt.title('CIF Value by Exporter Country and Mode of Transport')
plt.show()
plt.close()

# Bar plot: Mode of transport (excluding Malaysia, TOTAL MOT only)
plt.figure(figsize=(14, 7))
transport_values_no_mys = (
    df_clean[df_clean['reporterISO'] != 'MYS']
    .groupby(['reporterDesc', 'motDesc'], dropna=True)['cifvalue']
    .sum()
    .reset_index()
)
transport_values_no_mys = transport_values_no_mys[transport_values_no_mys['motDesc'].notna()]
transport_values_no_mys = transport_values_no_mys[transport_values_no_mys['motDesc'] == 'TOTAL MOT']

ax7 = sns.barplot(x='reporterDesc', y='cifvalue', hue='motDesc', data=transport_values_no_mys)
for p in ax7.patches:
    height = p.get_height()
    if height > 0:
        ax7.text(p.get_x() + p.get_width() / 2, height, f'{int(height):,}',
                ha='center', va='bottom', fontsize=8, rotation=0)

plt.ticklabel_format(style='plain', axis='y')
plt.grid(axis='y', linestyle='--')
plt.xticks(rotation=90)
plt.title('CIF Value by Exporter Country and Mode of Transport (Excluding Malaysia)', fontsize=12, fontweight='bold')
plt.tight_layout()
plt.show()
plt.close()

# Create date column for time series
df_clean['Year'] = df_clean['period'].astype(str).str[:4].astype(int)
df_clean['Month'] = df_clean['period'].astype(str).str[4:].astype(int)
df_clean['Date'] = pd.to_datetime(df_clean[['Year','Month']].assign(DAY=1))

# Area chart: Monthly contribution percentage by country
monthly_totals = df_clean.groupby(['Date','reporterDesc'])['cifvalue'].sum().reset_index()
pivot_data = monthly_totals.pivot(index='Date', columns='reporterDesc', values='cifvalue').fillna(0)
pivot_data_pct = pivot_data.div(pivot_data.sum(axis=1), axis=0)

plt.figure(figsize=(12,6))
ax8 = pivot_data_pct.plot.area(ax=plt.gca(), cmap='tab20')

# Label final values
for col in pivot_data_pct.columns:
    y = pivot_data_pct[col].values
    if len(y) > 0 and y[-1] > 0.01:
        plt.text(pivot_data_pct.index[-1], y[-1], f'{col}: {y[-1]*100:.1f}%',
                ha='left', va='center', fontsize=8)

ax8.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: f'{y*100:.0f}%'))

plt.title('Relative Contribution to CIF Imports by Country (Monthly)', fontsize=14, fontweight='bold')
plt.xlabel('Month')
plt.ylabel('Share of CIF Imports (%)')
plt.grid(axis='y', linestyle='--')
plt.legend(title='Country', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# Pie charts: Monthly contribution by country (with Malaysia)
monthly_totals = df_clean.groupby(['Date', 'reporterDesc'])['cifvalue'].sum().reset_index()

for d in monthly_totals['Date'].unique():
    subset = monthly_totals[monthly_totals['Date']==d].copy()
    total = subset['cifvalue'].sum()
    subset['share'] = subset['cifvalue'] / total
    # Group small contributors (<2%) into "Others"
    big = subset[subset['share'] >= 0.02]
    small = subset[subset['share'] < 0.02]
    if not small.empty:
        others = pd.DataFrame({'reporterDesc':['Others'],'cifvalue':[small['cifvalue'].sum()]})
        subset = pd.concat([big[['reporterDesc','cifvalue']], others])

    plt.figure(figsize=(8,8))
    wedges, texts, autotexts = plt.pie(
        subset['cifvalue'],
        labels=subset['reporterDesc'],
        autopct='%1.1f%%',
        startangle=140,
        counterclock=False,
        wedgeprops={'edgecolor':'white','linewidth':2},
        textprops={'fontsize':9},
        pctdistance=0.85
    )
    centre_circle = plt.Circle((0,0),0.70,fc='white')  # Create donut chart
    plt.gca().add_artist(centre_circle)
    plt.title(f'Contribution to Total CIF Imports - {d.strftime("%b %Y")}', fontsize=12, fontweight='bold')
    plt.tight_layout()
    plt.show()
    plt.close()

# Pie charts: Monthly contribution by country (excluding Malaysia)
monthly_totals_no_mys = df_clean[df_clean['reporterISO'] != 'MYS'].groupby(['Date', 'reporterDesc'])['cifvalue'].sum().reset_index()

for d in monthly_totals_no_mys['Date'].unique():
    subset = monthly_totals_no_mys[monthly_totals_no_mys['Date']==d].copy()
    total = subset['cifvalue'].sum()
    subset['share'] = subset['cifvalue'] / total
    big = subset[subset['share'] >= 0.02]
    small = subset[subset['share'] < 0.02]
    if not small.empty:
        others = pd.DataFrame({'reporterDesc':['Others'],'cifvalue':[small['cifvalue'].sum()]})
        subset = pd.concat([big[['reporterDesc','cifvalue']], others])

    plt.figure(figsize=(8,8))
    wedges, texts, autotexts = plt.pie(
        subset['cifvalue'],
        labels=subset['reporterDesc'],
        autopct='%1.1f%%',
        startangle=140,
        counterclock=False,
        wedgeprops={'edgecolor':'white','linewidth':2},
        textprops={'fontsize':9},
        pctdistance=0.85
    )
    centre_circle = plt.Circle((0,0),0.70,fc='white')
    plt.gca().add_artist(centre_circle)
    plt.title(f'Contribution to Total CIF Imports (Excluding Malaysia) - {d.strftime("%b %Y")}', fontsize=12, fontweight='bold')
    plt.tight_layout()
    plt.show()
    plt.close()