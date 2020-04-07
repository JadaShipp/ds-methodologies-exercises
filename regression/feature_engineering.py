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


def select_kbest(X, y, k ):
    f_selector = SelectKBest(f_regression, k = k)
    f_selector.fit(X, y)
    f_selector.transform(X)
    f_support = f_selector.get_support()
    f_feature = X.loc[:,f_support].columns.tolist()
    return f_feature

def select_rfe(X, y, k):
    lm = LinearRegression()
    rfe = RFE(lm, k)
    rfe.fit_transform(X, y)
    mask = rfe.support_
    rfe_features = X.loc[:,mask].columns.tolist()
    return rfe_features