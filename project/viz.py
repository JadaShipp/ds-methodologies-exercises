import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import wrangle



def plot_distributions():

    df = wrangle.get_df()

    filt = df['County'] == 'Los Angeles'
    LAC = df[filt]
    LAC = LAC[['County', 'tax_rate']]
    a = LAC.tax_rate

    filt2 = df['County'] == 'Orange'
    OC = df[filt2]
    OC = LAC[['County', 'tax_rate']]
    b = OC.tax_rate
    
    filt3 = df['County'] == 'Ventura'
    VC = df[filt3]
    VC = LAC[['tax_rate']]
    c = VC.tax_rate

    f, axes = plt.subplots(1, 3, figsize=(14, 5), sharex=True)
    sns.despine(left=True)
    
    ax1 = sns.distplot(a, kde=True, color="m", ax=axes[0])
    ax2 = sns.distplot(b, kde=True, color="b", ax=axes[1])
    ax3 = sns.distplot(c, kde=True, color="g", ax=axes[2])

    ax1.title.set_text('LA County')
    ax2.title.set_text('Orange County')
    ax3.title.set_text('Ventura County')

    ax1.set_ylabel('Number of Homes')
    ax2.set_ylabel('Number of Homes')
    ax3.set_ylabel('Number of Homes')


    plt.xlim(0, 0.2)
    plt.subplots_adjust(bottom=10, top = 12, left = 5, right = 6)
    return f
