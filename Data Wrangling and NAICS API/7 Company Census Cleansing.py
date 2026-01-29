import pandas as pd
import numpy as np

# low_memory=False ensures pandas scans entire columns before assigning dtypes, avoids DtypeWarning from mixed types
df = pd.read_csv('C:\\Users\\Aaron\\OneDrive\\Documents\\Debut projects\\Company_Census_File_20260121.csv', low_memory=False)

cols_to_drop = ['MCS150_DATE', 'ADD_DATE', 'MCS150_UPDATE_CODE_ID', 'DUN_BRADSTREET_NO', 'PHONE', 'FAX', 'CELL_PHONE', 'COMPANY_OFFICER_1', 'COMPANY_OFFICER_2', 'MAIL_NATIONALITY_INDICATOR', 'PHY_NATIONALITY_INDICATOR', 'PHY_BARRIO', 'MAIL_BARRIO', 'DOCKET1PREFIX', 'DOCKET2PREFIX', 'DOCKET3PREFIX', 'DOCKET1_STATUS_CODE', 'DOCKET2_STATUS_CODE', 'DOCKET3_STATUS_CODE',"OWNTRUCK","OWNTRACT","OWNTRAIL","OWNCOACH","OWNSCHOOL_1_8","OWNSCHOOL_9_15","OWNSCHOOL_16","OWNBUS_16","OWNVAN_1_8","OWNVAN_9_15","OWNLIMO_1_8","OWNLIMO_9_15","OWNLIMO_16","TRMTRUCK","TRMTRACT","TRMTRAIL","TRMCOACH","TRMSCHOOL_1_8","TRMSCHOOL_9_15","TRMSCHOOL_16","TRMBUS_16","TRMVAN_1_8","TRMVAN_9_15","TRMLIMO_1_8","TRMLIMO_9_15","TRMLIMO_16","TRPTRUCK","TRPTRACT","TRPTRAIL","TRPCOACH","TRPSCHOOL_1_8","TRPSCHOOL_9_15","TRPSCHOOL_16","TRPBUS_16","TRPVAN_1_8","TRPVAN_9_15","TRPLIMO_1_8","TRPLIMO_9_15","TRPLIMO_16", 'EMAIL_ADDRESS', 'CARRIER_MAILING_STREET', 'CARRIER_MAILING_STATE', 'CARRIER_MAILING_CITY', 'CARRIER_MAILING_COUNTRY', 'CARRIER_MAILING_ZIP', 'CARRIER_MAILING_CNTY', 'CARRIER_MAILING_UND_DATE', 'POINTNUM', 'REVIEW_ID', 'REVIEW_TYPE', 'DRIVER_INTER_TOTAL', 'REVIEW_DATE', 'UNDELIV_PHY']
df = df.drop(columns=cols_to_drop)

df = df.fillna('NaN')

print(df.dtypes)

# Downcast integers
df_int = df.select_dtypes(include=['int64'])
df[df_int.columns] = df_int.apply(pd.to_numeric, downcast='integer')

# Downcast floats
df_float = df.select_dtypes(include=['float64'])
df[df_float.columns] = df_float.apply(pd.to_numeric, downcast='float')

cargo_cols = [col for col in df.columns if col.startswith("CRGO_")]
df[cargo_cols] = df[cargo_cols].astype("category")

df.replace('NaN', np.nan, inplace=True)

# - If you want it back as a DataFrame (so you can save/export cleanly), you can wrap it like this:
print(df[['DOT_NUMBER']].duplicated().sum())

print(df.describe(include='all'))
print(df.dtypes)
print(df.info(memory_usage='deep'))

df.to_csv('Cleaned_Company_Census_File_20260121.csv', index=False)

