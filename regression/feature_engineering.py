import pandas as pd
import numpy as np
import pydataset
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.feature_selection import SelectKBest, f_regression, RFE
from sklearn.linear_model import LinearRegression
import warnings
warnings.filterwarnings("ignore")

import env
import wrangle
import split_scale


def select_kbest(X_train, y_train, k ):
    f_selector = SelectKBest(f_regression, k = k)
    f_selector.fit(X_train, y_train)
    f_selector.transform(X_train)
    f_support = f_selector.get_support()
    f_feature = X_train.loc[:,f_support].columns.tolist()
    return f_feature

def rfe(X_train, y_train, k):
    lm = LinearRegression()
    rfe = RFE(lm, k)
    rfe.fit_transform(X_train, y_train)
    mask = rfe.support_
    rfe_features = X_train.loc[:,mask].columns.tolist()
    return rfe_features