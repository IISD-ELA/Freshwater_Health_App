'''


The first model was developed using DSCAN. found in model.py
The clusting result can be downloaded using the code

This model in model_2 was developed using KMeans
How ever based on the results we adopted the KMeans algorightm for clustering
the outputs for the DBSCAN and KMeans for the clustering are in the datasets/model and model_2 csv respectively
and used the decision tree algorithim for a supervised learning and prediction

'''

import pandas as pd
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split


data_0 = pd.read_csv('../datasets/model_2.csv')
min_max = MinMaxScaler(feature_range=(0.1, 1))
data_scaled = pd.DataFrame(min_max.fit_transform(data_0), columns=data_0.columns)
kmeans = KMeans(n_clusters=5, init='k-means++', random_state=2, n_init=10)
data_0['clusters'] = kmeans.fit_predict(data_scaled)

# algorithm
y = data_0['clusters']
data_0 = data_0.drop('clusters', axis=1)
train_data, test_data, train_labels, test_labels = train_test_split(data_0, y, test_size=0.1)
model = DecisionTreeClassifier(max_depth=6)
model.fit(train_data, train_labels)

def prediction(CHLA,ALK,TDP,TDN,K,MG,SRSI,MN,CL,FE,SO4,DOC,NO3,
               PARTN,NA,COND,NH3,DIC,PARTP,PH,CA,NO2,PARTC,SECCHI_DEPTHS,
               MEAN_DAILY_DISCHARGE):
    data = {
        'CHLA': CHLA, 'ALK': ALK,
        'TDP': TDP, 'TDN': TDN, 'K': K, 'MG': MG,
        'SRSI': SRSI, 'MN': MN, 'CL': CL,
        'FE': FE, 'SO4': SO4, 'DOC': DOC,
        'NO3': NO3, 'PARTN': PARTN, 'NA': NA,
        'COND': COND, 'NH3': NH3, 'DIC': DIC,
        'PARTP': PARTP, 'PH': PH, 'CA': CA,
        'NO2': NO2, 'PARTC': PARTC, 'SECCHI_DEPTHS': SECCHI_DEPTHS,
        'MEAN_DAILY_DISCHARGE': MEAN_DAILY_DISCHARGE
    }
    single_data = pd.DataFrame(data, index=[0])
    prediction = model.predict(single_data)
    return prediction

with open('model_2.pkl', 'wb') as file:
    pickle.dump(model, file)

# Test the prediction
# result = prediction(
# CHLA=1.65,
# ALK=18,
# TDP=6,
# TDN=511,
# K=0.04,
# MG=0.61,
# SRSI=4.77,
# MN=0,
# CL=0.12,
# FE=0.41,
# SO4=2.16,
# DOC=1840,
# NO3=5,
# PARTN=0,
# NA=1.01,
# COND=22,
# NH3=17,
# DIC=304,
# PARTP=2,
# PH=4.86,
# CA=1.99,
# NO2=2,
# PARTC=296,
# SECCHI_DEPTHS=4.25,
# MEAN_DAILY_DISCHARGE=0.01)
#
# print(result)