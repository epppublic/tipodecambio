from pickle import TRUE
import pandas as pd
import numpy as np

def getcolones(do):
    data = {'startdate':['05/06/2022','06/04/2022','07/03/2022','08/01/2022','08/30/2022','09/28/2022','10/27/2022','11/25/2022'],
        'enddate':['06/04/2022','07/03/2022','08/01/2022','08/30/2022','09/28/2022','10/27/2022','11/25/2022','12/24/2022'],
        'startexch':['670.91','690.89','711.47','732.65','754.47','776.94','800.08','823.9'],
        'endexch':['690.89','711.47','732.65','754.47','776.94','800.08','823.9','848.44']
        }

    # Create dataframe
    df = pd.DataFrame(data)
    df['startdate'] = pd.to_datetime(df['startdate'], infer_datetime_format=True)
    df['enddate'] = pd.to_datetime(df['enddate'], infer_datetime_format=True)
    df = df.astype({"startexch": float}, errors='raise')
    df = df.astype({"endexch": float}, errors='raise')
    # Create calculated fields
    df['days'] = df['enddate'].sub(df['startdate'], axis=0)
    df['delta'] = df['endexch'] - df['startexch']

    newcolones12 = do * df['endexch'].iloc[7]
    newcolones3 = do * df['endexch'].iloc[3]

    return newcolones12, newcolones3

getcolones(1500)