from pickle import TRUE
import pandas as pd
import numpy as np

# data 
data = {'startdate':['05/06/2022'],
        'enddate':['06/04/2022'],
        'startexch':['670.91'],
        'endexch':['690.89']
        }

# data = {'startdate':['06/05/2022','04/06/2022','03/07/2022','01/08/2022','30/08/2022','28/09/2022','27/10/2022','25/11/2022'],
#         'enddate':['04/06/2022','03/07/2022','01/08/2022','30/08/2022','28/09/2022','27/10/2022','25/11/2022','24/12/2022'],
#         'startexch':[670,91],
#         'endexch':[690,89]
#         }

# Create dataframe

df = pd.DataFrame(data)
df['startdate'] = pd.to_datetime(df['startdate'], infer_datetime_format=True)
df['enddate'] = pd.to_datetime(df['enddate'], infer_datetime_format=True)
df = df.astype({"startexch": float}, errors='raise')
df = df.astype({"endexch": float}, errors='raise')
print(df)

# Create calculated fields

df['days'] = df['enddate'].sub(df['startdate'], axis=0)
df['delta'] = df['endexch'] - df['startexch']
