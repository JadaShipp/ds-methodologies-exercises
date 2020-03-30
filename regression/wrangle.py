import pandas as pd 
import numpy as np 
from env import get_db_url

def wrangle_telco():
    telco_churn_url = get_db_url('telco_churn')
    query = '''
    SELECT * 
    FROM customers
    '''

    customers = pd.read_sql(query, telco_churn_url)

    query = '''
    SELECT * 
    FROM contract_types
    '''

    contract_types = pd.read_sql(query, telco_churn_url)

    df = customers.merge(contract_types, left_on = 'contract_type_id', right_on = 'contract_type_id')
    df = df[["customer_id", "monthly_charges", "tenure", "total_charges", "contract_type"]]
    df = df[df.contract_type == 'Two year']
    df.total_charges = df.total_charges.str.strip()
    df = df[df.total_charges != ""]
    df.total_charges = df.total_charges.astype(float)
    return df