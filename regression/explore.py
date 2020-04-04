import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def plot_variable_pairs(df, hue=None):
    g = sns.pairplot(df, hue=hue, kind="reg", diag_kind="kde", plot_kws={'line_kws':{'color':'green'}, 'scatter_kws': {'alpha': 0.7}})
    g.fig.suptitle("Scatterplot with Regression for Continuous Variables")
    plt.show()

def months_to_years(df_plus_train):
        df["tenure_years"] = (df_plus_train['tenure'] // 12)
        return df

def plot_categorical_and_continous_vars(categorical_var, continuous_var, df):
    sns.catplot(y=categorical_var, x=continuous_var, data=df) 
    sns.catplot(x=categorical_var, kind="count", palette="ch:.25", data=df)
    sns.catplot(x=categorical_var, y=continuous_var, kind="box", data=df)
    sns.catplot(x=categorical_var, y=continuous_var, kind="violin", bw=.15, cut=0, data=df)