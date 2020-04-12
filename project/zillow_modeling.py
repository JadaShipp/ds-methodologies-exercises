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


def select_rfe(X, y, k):
    lm = LinearRegression()
    rfe = RFE(lm, k)
    rfe.fit_transform(X, y)
    mask = rfe.support_
    rfe_features = X.loc[:,mask].columns.tolist()
    return rfe_features