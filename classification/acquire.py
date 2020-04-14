import pandas as pd 
import seaborn as sns
import numpy as np
from pydataset import data
from env import host, user, password

def get_db_url(dbname) -> str:
    url = 'mysql+pymysql://{}:{}@{}/{}'
    return url.format(user, password, host, dbname)

def get_titanic_data():
    query = '''
    SELECT *
    FROM passengers
    '''
    titanic_df = pd.read_sql(query, get_db_url('titanic_db'))
    return titanic_df 


def get_iris_data():
    query = '''
    SELECT species_id, species_name, sepal_length, sepal_width, petal_length, petal_width
    FROM measurements
    JOIN species
    USING(species_id)
    '''
    iris_df = pd.read_sql(query, get_db_url('iris_db'))
    return iris_df