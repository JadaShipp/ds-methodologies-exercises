import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, QuantileTransformer, PowerTransformer, RobustScaler, MinMaxScaler

def split_data(df, train_pct=0.75, seed=123):
    train, test = train_test_split(df, train_size=train_pct, random_state=seed)
    return train, test


def min_max_scaler(X_train, X_test):
    """Transforms features by scaling each feature to a given range.
       Takes in X_train and X_test,
       Returns the scaler and X_train_scaled and X_test_scaled within range.
       Sensitive to outliers.
    """
    scaler = (MinMaxScaler(copy=True, 
                           feature_range=(0,1))
                          .fit(X_train))
    X_train_scaled = (pd.DataFrame(scaler.transform(X_train), 
                      columns=X_train.columns, 
                      index=X_train.index))
    X_test_scaled = (pd.DataFrame(scaler.transform(X_test), 
                     columns=X_test.columns,
                     index=X_test.index))
    return scaler, X_train_scaled, X_test_scaled