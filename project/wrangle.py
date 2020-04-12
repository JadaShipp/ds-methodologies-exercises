import pandas as pd 
import numpy as np 
from env import host, user, password

def get_db_url(dbname) -> str:
    url = 'mysql+pymysql://{}:{}@{}/{}'
    return url.format(user, password, host, dbname)

def get_df():
    '''
    Function produces a clean dataframe from a SQL querry 
    '''
    query = '''
    SELECT properties_2017.parcelid, propertylandusetypeid, calculatedfinishedsquarefeet, taxamount, taxvaluedollarcnt, bedroomcnt, bathroomcnt, predictions_2017.transactiondate, fips
    FROM properties_2017
    LEFT JOIN predictions_2017 ON properties_2017.parcelid=predictions_2017.parcelid
    WHERE propertylandusetypeid = 261 
	    AND (transactiondate >= '2017-05-01' AND transactiondate <= '2017-06-30')
	    AND bedroomcnt > 0
	    AND bathroomcnt > 0
    '''
    df = pd.read_sql(query, get_db_url('zillow'))
    df["County"] = df['fips'].map({6037: "Los Angeles", 6059: "Orange", 6111: "Ventura"})
    df.astype({'fips': 'str'})
    df = df.rename(columns={'calculatedfinishedsquarefeet': 'square_feet', 'taxamount':'taxes', 'fips':'FIPS', 'taxvaluedollarcnt':'home_value', 'bedroomcnt':'bedroom_count', 'bathroomcnt':'bathroom_count'})
    df = df.drop(columns=['propertylandusetypeid', 'parcelid', 'transactiondate', 'FIPS'])
    df = df.dropna()
    df["tax_rate"] = df["taxes"] / df["home_value"]
    return df
