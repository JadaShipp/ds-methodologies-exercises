import pandas as pd
import numpy as np 
import scipy
from sklearn.metrics import accuracy_score, precision_score, recall_score,  classification_report
import warnings
warnings.filterwarnings("ignore")



# def apply_metrics(df):
#     model1_accuracy = accuracy_score(df.actual, df.model1, normalize=True)
#     print(f' First model accuracy is {model1_accuracy: .2%}')
#     model1_precision = precision_score(df.actual, df.model1, pos_label = 'dog')
#     print(f' First model precision is {model1_precision: .2%}')
#     model1_recall = recall_score(df.actual, df.model1, pos_label = 'dog')
#     print(f' First model recall is {model1_recall: .2%}')
#     target_names = ['cat', 'dog']
#     class_report1 = classification_report(df.actual, df.model1, target_names=target_names)
#     print(f'First model Classification report: {class_report1}')
#     return model1_accuracy, model1_precision, model1_recall, class_report1

def accuracy(df):
    model_accuracy = accuracy_score(df.actual, df.model1, normalize=True)
    return print(f' Model accuracy is {model_accuracy: .2%}')
def precision(df, label):
    model_precision = precision_score(df.actual, df.model1, pos_label = label)
    return print(f' Model precision is {model_precision: .2%}')
def recall(df, label):
    model_recall = recall_score(df.actual, df.model1, pos_label = label)
    return print(f' Model recall is {model_recall: .2%}')
def class_report(df,targets):
    return print(classification_report(df.actual, df.model1, target_names=targets))
    

def apply_metrics(df, label, targets):
    model_accuracy = accuracy(df)
    model_precision = precision(df, label)
    model_recall = recall(df, label)
    class_report(df,targets)
    return model_accuracy, model_precision, model_recall, class_report
    
    
