import pandas as pd
import env
import seaborn as sns
import acquire
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, MinMaxScaler
import warnings
warnings.filterwarnings("ignore")



def drop_iris_columns(iris_df):
    iris_df = iris_df.drop(columns=['species_id'])
    return iris_df
def rename_colums(iris_df):
    iris_df = iris_df.rename(columns={'species_name': 'species'})
    return iris_df

def label_encode_species(train, test):
    encoder = LabelEncoder()
    encoder.fit(train.species)
    
    train.encoded = encoder.transform(train.species)
    test.encoded = encoder.transform(test.species)
    
    train_array = np.array(train.encoded).reshape(len(train.encoded),1)
    test_array = np.array(test.encoded).reshape(len(test.encoded),1)
    
    cols = ['encoded_' + train.columns[0]]
    train = pd.concat([
        train,
        pd.DataFrame(train_array, columns = cols, index=train.index)
    ], axis=1)

    test = pd.concat([
        test,
        pd.DataFrame(test_array, columns = cols, index=test.index)
    ], axis=1)
    
    return train, test
def prep_iris(iris_df):
    iris_df = drop_iris_columns(iris_df)
    iris_df = rename_colums(iris_df)
    train, test = train_test_split(iris_df, random_state=123, train_size=.8)
    return label_encode_species(train,test)


def drop_titanic_columns(titanic_df):
    titanic_df = titanic_df.drop(columns=['deck', 'class', 'embarked','passenger_id'])
    return titanic_df
def fill_embark_town_na(train, test):
    train.embark_town = train.embark_town.fillna('Southampton')
    test.embark_town = test.embark_town.fillna('Southampton')
    return train, test
def encode_embark_town(train, test):
    encoder = LabelEncoder()
    encoder.fit(train.embark_town)

    train.encoded = encoder.transform(train.embark_town)
    test.encoded = encoder.transform(test.embark_town)

    train_array = np.array(train.encoded).reshape(len(train.encoded),1)
    test_array = np.array(test.encoded).reshape(len(test.encoded),1)
    
    cols = ['encoded_' + train.columns[7]]
    train = pd.concat([
        train,
        pd.DataFrame(train_array, columns = cols, index=train.index)
    ], axis=1)

    test = pd.concat([
        test,
        pd.DataFrame(test_array, columns = cols, index=test.index)
    ], axis=1)
    return train, test
def impute_age(train, test):
    imputer = SimpleImputer(strategy='mean')
    imputer.fit(train[['age']])
    train.age = imputer.transform(train[['age']])
    test.age = imputer.transform(test[['age']])
    return train, test

def scale_age(train, test):
    scaler = MinMaxScaler()
    scaler.fit(train[['age']])
    train.age = scaler.transform(train[['age']])
    test.age = scaler.transform(test[['age']])
    return train, test

def scale_fare(train,test):
    scaler = MinMaxScaler()
    scaler.fit(train[['fare']])
    train.fare = scaler.transform(train[['fare']])
    test.fare = scaler.transform(test[['fare']])
    return train, test

def prep_titanic(titanic_df):
    titanic_df = drop_titanic_columns(titanic_df)
        
    train, test = train_test_split(titanic_df, train_size=.80, random_state=123)
    
    train, test = fill_embark_town_na(train, test)
    
    train, test = encode_embark_town(train, test)
    
    train, test = impute_age(train, test)
    train, test = scale_age(train, test)
    train, test = scale_fare(train,test)
    return train, test