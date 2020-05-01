import pandas as pd 
import env



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
    return

# def handle_missing_values(df, prop_required_column, prop_required_row)