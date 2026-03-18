import requests
import pandas as pd

url = 'https://api.census.gov/data/timeseries/intltrade/exports/naics'
years = range(2016, 2026)

all_data = []

for year in years:
    params = {
        'get': "ALL_VAL_YR,CTY_CODE,CTY_NAME,NAICS",
        'NAICS': '334',   # Electronics
        'YEAR': '2025',
        'key': 'ffdbbbe9a633e520a6da1e5a3a35df69e9e5455d'
    }
    r = requests.get(url, params=params)
    try:
        data = r.json()
        if len(data) > 1:
            df = pd.DataFrame(data[1:], columns=data[0])
            all_data.append(df)
        else:
            print(f"Error en {year}: {r.status_code}")
    except ValueError:
        print(f'Invalid response for {year}: {r.text[:200]}')

if all_data:
    final_df = pd.concat(all_data, ignore_index=True)
    print(final_df.head())
else:
    print('No data retrieved')
