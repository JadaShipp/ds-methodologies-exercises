import pandas as pd
import numpy as np 
import scipy
from sklearn.metrics import accuracy_score, precision_score, recall_score,  classification_report
import warnings
warnings.filterwarnings("ignore")



def apply_metrics(df):
    model1_accuracy = accuracy_score(df.actual, df.model1, normalize=True)
    print(f' First model accuracy is {model1_accuracy: .2%}')
    model1_precision = precision_score(df.actual, df.model1, pos_label = 'dog')
    print(f' First model precision is {model1_precision: .2%}')
    model1_recall = recall_score(df.actual, df.model1, pos_label = 'dog')
    print(f' First model recall is {model1_recall: .2%}')
    target_names = ['cat', 'dog']
    class_report1 = classification_report(df.actual, df.model1, target_names=target_names)
    print(f'First model Classification report: {class_report1}')
    return model1_accuracy, model1_precision, model1_recall, class_report1