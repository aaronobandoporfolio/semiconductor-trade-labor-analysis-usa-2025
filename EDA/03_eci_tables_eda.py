import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette('husl')

weekly_sa = pd.read_csv('C:\\Users\\Aaron\\OneDrive\\Documents\\Debut projects\\2 Cleaned data\\Employment Tables\\Table B-3a average_weekly_earnings.csv')
weekly_nsa = pd.read_csv('C:\\Users\\Aaron\\OneDrive\\Documents\\Debut projects\\2 Cleaned data\\Employment Tables\\Table B-3a average_weekly_earnings_not_seasonally_adjusted.csv')
hourly_sa = pd.read_csv('C:\\Users\\Aaron\\OneDrive\\Documents\\Debut projects\\2 Cleaned data\\Employment Tables\\Table B-3b average_hourly_earnings.csv')
hourly_nsa = pd.read_csv('C:\\Users\\Aaron\\OneDrive\\Documents\\Debut projects\\2 Cleaned data\\Employment Tables\\Table B-3b average_hourly_earnings_not_seasonally_adjusted.csv')
weekly_prod_sa = pd.read_csv('C:\\Users\\Aaron\\OneDrive\\Documents\\Debut projects\\2 Cleaned data\\Employment Tables\\Table B-8a average_weekly_earnings_production_employees.csv')
weekly_prod_nsa = pd.read_csv('C:\\Users\\Aaron\\OneDrive\\Documents\\Debut projects\\2 Cleaned data\\Employment Tables\\Table B-8a average_weekly_earnings_production_employees_not_seasonally_adjusted.csv')
hourly_prod_sa = pd.read_csv('C:\\Users\\Aaron\\OneDrive\\Documents\\Debut projects\\2 Cleaned data\\Employment Tables\\Table B-8b average_hourly_earnings_production_employees.csv')
hourly_prod_nsa = pd.read_csv('C:\\Users\\Aaron\\OneDrive\\Documents\\Debut projects\\2 Cleaned data\\Employment Tables\\Table B-8b average_hourly_earnings_production_employees_not_seasonally_adjusted.csv')


#Insight 1
def insight_1_communications_surge():
    results = []
    for idx, row in weekly_sa.iterrows():
        naics = row['NAICS Code']
        industry = row['Industry']
        dec24 = row['Dec-24']
        dec25 = row['Dec-25']
        growth = ((dec25 - dec24)/dec24)
        #Calculate YoY growth for all subsectors
        results.append({
            'Industry': industry,
            'NAICS': naics,
            'Dec-24': dec24,
            'Dec-25': dec25,
            'Growth %': growth
        })

    df_results = pd.DataFrame(results).sort_values('Growth %', ascending=False)
    print("\nWage Growth Rankings (Dec-24 to Dec-25):")
    print(df_results.to_string(index=False))
    #Key finding
    winner = df_results.iloc[0]
    print(f'\nWinner: {winner['Industry']}')
    print(f'Growth: {winner['Growth %']:.1f}%')
    print(f'Weekly Earnings: ${winner['Dec-24']:,.2f} -> ${winner['Dec-25']:,.2f}')
    print(f'Hourly Earnings: ${(winner["Dec-25"] - winner["Dec-24"]) * 52:,.0f}')

    return df_results

#Insight 2

def insight_2_premium_gap():
     #Get semiconductor device and industry average
    semi = weekly_sa[weekly_sa['NAICS Code'] == 334413].iloc[0]
    industry = weekly_sa[weekly_sa['NAICS Code'] == 334].iloc[0]
    #Calculate premium
    premium_pct = ((semi['Dec-25'] - industry['Dec-25']) / industry['Dec-25']) * 100
    premium_weekly = semi['Dec-25'] - industry['Dec-25']
    premium_annual =  premium_weekly * 52

    print(f"\nSemiconductor Device vs Industry Average (Dec-25):")
    print(f"Semiconductor Device: ${semi['Dec-25']:,.2f}/week (${semi['Dec-25']*52:,.0f}/year)")
    print(f"Industry Average: ${industry['Dec-25']:,.2f}/week (${industry['Dec-25']*52:,.0f}/year)")
    print(f"\nPremium: ${premium_weekly:,.2f}/week (${premium_annual:,.0f}/year)")
    print(f"Premium %: {premium_pct:.1f}%")
    #Track premium evolution
    premium_24 = ((semi['Dec-24'] - industry['Dec-24']) / industry['Dec-24']) * 100
    premium_25 = premium_pct
    premium_expansion = premium_25 - premium_24

    print(f"\nPremium Evolution:")
    print(f"Dec-24: {premium_24:.1f}%")
    print(f"Dec-25: {premium_25:.1f}%")
    print(f"Expansion: {premium_expansion:+.1f} percentage points")
    
    return{
        'premium_annual': premium_annual,
        'premium_pct': premium_pct,
        'premium_expansion': premium_expansion
    }

#Insight 3, find lowest growth sectors
def insight_3_stagnation_risk():
    #Find lowest growth sectors
    growth_data = []
    for idx, row in weekly_sa.iterrows():
        dec24 = row['Dec-24']
        dec25 = row['Dec-25']
        growth = ((dec25 - dec24) / dec24) * 100

        growth_data.append({
            'industry': row['Industry'],
            'Growth %': growth,
            'Dec-25 Weekly': dec25
        })

    df_growth = pd.DataFrame(growth_data).sort_values('Growth %')
    print('\nLowest Growth Sectors:')
    print(df_growth.head().to_string(index=False))

    #Calculate inflation gap
    inflation_rate = 3.5 #approximate 2024-2025 inflation
    print(f'WARNING: Sectots below {inflation_rate}% growth are losing real purchasing power')

    underperformers = df_growth[df_growth['Growth %'] < inflation_rate]
    print(f'\n{len(underperformers)} out of {len(df_growth)} sectors are below inflation')

    return df_growth


#Insights 4
def insight_4_skills_premium():
    #broader category 3344 (has production data)
    naics = 3344

    all_emp = weekly_sa[weekly_sa['NAICS Code'] == naics].iloc[0]
    prod = weekly_prod_sa[weekly_prod_sa['NAICS Code'] == naics].iloc[0]
    #Calculate premium for both years
    premium_24 = ((all_emp['Dec-24'] - prod['Dec-24']) / prod['Dec-24']) * 100
    premium_25 = ((all_emp['Dec-25'] - prod['Dec-25']) / prod['Dec-25']) * 100

    gap_24 = all_emp['Dec-24'] - prod['Dec-24']
    gap_25 = all_emp['Dec-25'] - prod['Dec-25']

    print(f"\nSemiconductor & Components (NAICS 3344):")
    print(f"\nDec-24:")
    print(f"All Employees: ${all_emp['Dec-24']:,.2f}")
    print(f"Production: ${prod['Dec-24']:,.2f}")
    print(f"Skills Premium: ${gap_24:,.2f} ({premium_24:.1f}%)")    
    print(f"\n  Dec-25:")
    print(f"All Employees: ${all_emp['Dec-25']:,.2f}")
    print(f"Production: ${prod['Dec-25']:,.2f}")
    print(f"Skills Premium: ${gap_25:,.2f} ({premium_25:.1f}%)")

    #The paradox
    premium_change = premium_25 - premium_24
    print(f'\n Paradox: Skills premium {('widened' if premium_change > 0 else 'NARROWED')} by {abs(premium_change):.1f} percentage points')

    #Calculate individual growth rates
    all_emp_growth = ((all_emp['Dec-25'] - all_emp['Dec-24']) / all_emp['Dec-24']) * 100
    prod_growth = ((prod['Dec-25'] - prod['Dec-24']) / prod['Dec-24']) * 100

    print(f"\nWage Growth Breakdown:")
    print(f"All Employees: {all_emp_growth:+.1f}%")
    print(f"Production: {prod_growth:+.1f}%")
    print(f"Difference: {all_emp_growth - prod_growth:+.1f} percentage points")

    if prod_growth > all_emp_growth:
        print(f"\nInsight: Production workers are catching up!")
        print(f"Possible reasons:")
        print(f"1.Labor shortage in manufacturing")
        print(f"2.Union negotiations")
        print(f"3.Retention bonuses for factory workers")

    return {
        'premium_24': premium_24,
        'premium_25': premium_25,
        'premium_change': premium_change
    }


#insight 5
def insight_5_recent_acceleration():
    naics = 334413 #semiconductor device
    semi = weekly_sa[weekly_sa['NAICS Code'] == naics].iloc[0]
    
    #Calculate different period growth
    dec24_to_oct25 = ((semi['Oct-25'] - semi['Dec-24']) / semi['Dec-24']) * 100
    oct25_to_dec25 = ((semi['Dec-25'] - semi['Oct-25']) / semi['Oct-25']) * 100
    full_year = ((semi['Dec-25'] - semi['Dec-24']) / semi['Dec-24']) * 100

    print(f"\nSemiconductor Device Manufacturing - Growth Timing:")
    print(f"Dec-24: ${semi['Dec-24']:,.2f}")
    print(f"Oct-25: ${semi['Oct-25']:,.2f}")
    print(f"Dec-25: ${semi['Dec-25']:,.2f}")
    print(f"\nGrowth Breakdown:")
    print(f"Dec-24 → Oct-25 (10 months): {dec24_to_oct25:+.1f}%")
    print(f"Oct-25 → Dec-25 (2 months): {oct25_to_dec25:+.1f}%")
    print(f"Full Year: {full_year:+.1f}%")

    #Annualized rates
    oct_dec_annualized = (oct25_to_dec25 / 2) * 12
    print(f"\nAnnualized Rates:")
    print(f"First 10 months: {(dec24_to_oct25 / 10) * 12:+.1f}%")
    print(f"Last 2 months: {oct_dec_annualized:+.1f}%")
    print(f"\nInsight: {'Most' if dec24_to_oct25 > oct25_to_dec25 else 'Recent'} growth happened {'early in year' if dec24_to_oct25 > oct25_to_dec25 else 'in Q4 2025'}")

    return {
        'q4_growth': oct25_to_dec25,
        'full_year': full_year
    }


#Last insight
def insight_6_real_vs_nominal():
    inflation_rate = 3.5 #approximate 2024-2025

    for idx, row in weekly_sa.iterrows():
        industry = row['Industry']
        dec24 = row['Dec-24']
        dec25 = row['Dec-25']

        nominal_growth = ((dec25 - dec24) / dec24) * 100
        real_growth = nominal_growth - inflation_rate

        real_indicator = 'True' if real_growth > 0 else 'False'

        print(f"{real_indicator} {industry[:60]}")
        print(f"Nominal: {nominal_growth:+.1f}% | Real: {real_growth:+.1f}%")
        print()

#Run all insights
growth_rankings = insight_1_communications_surge()
premium_data = insight_2_premium_gap()
stagnation_data = insight_3_stagnation_risk()
skills_data = insight_4_skills_premium()
acceleration_data = insight_5_recent_acceleration()
real_vs_nominal_data = insight_6_real_vs_nominal()


output_dir = "C:\\Users\\Aaron\\OneDrive\\Documents\\Debut projects\\2 Cleaned data\\Employment Tables\\Findings"

#Insight 1 already a dataFrame
growth_rankings.to_csv(output_dir + 'insight_1_wage_growth_rankings.csv', index=False)
#Insight 2 dict -> DataFrame
pd.DataFrame([premium_data]).to_csv(output_dir + 'insight_2_semiconductor_premium.csv', index=False)
#Insight 3 already a DataFrame
stagnation_data.to_csv(output_dir + 'insight_3_stagnation_risk.csv', index=False)
# Insight 4 dict -> DataFrame
pd.DataFrame([skills_data]).to_csv(output_dir + 'insight_4_skills_premium.csv', index=False)
# Insight 5 dict -> DataFrame
pd.DataFrame([acceleration_data]).to_csv(output_dir + 'insight_5_recent_acceleration.csv', index=False)

#Insight 6 rebuild as DataFrame (function currently only prints)
inflation_rate = 3.5
real_vs_nominal_rows = []
for idx, row in weekly_sa.iterrows():
    nominal = ((row['Dec-25'] - row['Dec-24']) / row['Dec-24']) * 100
    real = nominal - inflation_rate
    real_vs_nominal_rows.append({
        'Industry': row['Industry'],
        'NAICS Code': row['NAICS Code'],
        'Dec-24': row['Dec-24'],
        'Dec-25': row['Dec-25'],
        'Nominal Growth %': round(nominal, 2),
        'Real Growth %': round(real, 2),
        'Real Wage Gain': real > 0
    })
pd.DataFrame(real_vs_nominal_rows).to_csv(output_dir + 'insight_6_real_vs_nominal.csv', index=False)
