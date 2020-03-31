import pandas as pd 
import numpy as np 
from env import host, user, password

def get_db_url(dbname) -> str:
    url = 'mysql+pymysql://{}:{}@{}/{}'
    return url.format(user, password, host, dbname)

def get_telco_customer_table():
    query = '''
    SELECT * 
    FROM customers
    '''
    customers = pd.read_sql(query, get_db_url('telco_churn'))
    return customers

def get_telco_contract_type_table():
    query = '''
    SELECT * 
    FROM contract_types
    '''
    contract_types = pd.read_sql(query, get_db_url('telco_churn'))
    return contract_types


def wrangle_telco():
    customers = get_telco_customer_table()
    contract_types = get_telco_contract_type_table()
    df = customers.merge(contract_types, left_on = 'contract_type_id', right_on = 'contract_type_id')
    df = df[["customer_id", "monthly_charges", "tenure", "total_charges", "contract_type"]]
    df = df[df.contract_type == 'Two year']
    df.total_charges = df.total_charges.str.strip()
    df = df[df.total_charges != ""]
    df.total_charges = df.total_charges.astype(float)
    return df