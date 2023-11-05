# -*- coding: utf-8 -*-
"""final.ipynb


This model was developed using DBSCAN.
The clusting result can be downloaded using the code

The other model in model_2 was developerd using KMeans
How ever based on the results we adopted the KMeans algorightm for clustering

and used the decision tree algorithim for a supervised learning and prediction

"""

from xgboost.sklearn import XGBRegressor
from xgboost.training import train
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
from sklearn.preprocessing import RobustScaler
from scipy.cluster.hierarchy import dendrogram, linkage,cut_tree
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from xgboost import XGBClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

#data = pd.read_csv('../datasets/model.csv')
data_scaled = pd.read_csv('../datasets/model.csv')
# data.head()
# #data.drop('S/N', axis = 1, inplace = True)
#
# #creating a function to change the date for modelling
# def date_transform(data):
#     base_line  = pd.to_datetime('2015-01-01')
#     new_date = data['ACTIVITY_START_DATE'].apply((lambda x: pd.to_datetime(x) - base_line))
#     data['ACTIVITY_START_DATE'] = new_date.dt.days
#     return data
# #data = date_transform(data)
# #data.head()
#
# #changing the categorical data into numerical values
# features = [col for col in data.columns if data[col].dtype == 'object'
#     and data[col].nunique() == 5]
# def cat_value(data):
#     return pd.get_dummies(data)
# cat_data = data[features]
# data.drop(features, axis = 1, inplace = True)
# #call the function
# cat_values = cat_value(cat_data)
# data = pd.concat([data,cat_values], axis = 1)
# data.head()
# data_1 = data[data["TREATMENT"] == 1]
# data_0 = data[data["TREATMENT"] == 0]
# #creating a function to convert the missing values to median
# def missing_values(train_dataset):
#     #changing null values to the modal scores
#     imputer = SimpleImputer(strategy='mean')
#     imputer.fit(train_dataset)
#     train_data = pd.DataFrame(imputer.transform(train_dataset))
#     train_data.columns = train_dataset.columns
#     return train_data
# missing_values(data_1)
# missing_values(data_0)
#
# outlier_counts = {}
# #function to check outliers using interquartile range
# lower_bound = 0
# upper_bound = 0
# def check_outliers(train_data, data_set):
#     outliers = []
#     count = 0
#     dates = []
#     outlier_counts = {}
#     q1 = train_data.quantile(0.25)
#     q3 = train_data.quantile(0.75)
#     iqr = q3 - q1
#     lower_bound = q1 - (1.5 * iqr)
#     upper_bound = q3 + (1.5 * iqr)
#     for x in range(len(train_data)):
#         outlier_counts = {}
#
#         if (train_data[x] < lower_bound) or (train_data[x] > upper_bound):
#             outliers.append(train_data[x])
#             count += 1
#             dates.append(data_set.loc[x])
#     return outliers,dates
# #calling the outliers function
# def calling_outliers(data):
#     alk = {}
#     for i in data.columns:
#         alk = check_outliers(data[i],data["ACTIVITY_START_DATE"])
#         length = len(alk[0])
#         if len(alk[0]) !=0:
#             alk =dict(zip(alk[0], alk[1]))
#
# #separating the data to fertilized and non fertilized
# data_0 = data[data["TREATMENT"] == 0]
# data_1 = data[data["TREATMENT"] == 1]
#
# data_columns = data_0.columns
# #scaling the dataset to prepare for modelling
# min_max = MinMaxScaler(feature_range=(0.1,1))
# data_scaled = pd.DataFrame(min_max.fit_transform(data_0), columns = data_columns)
#
# #running the DBSCAN algorithm to know which eps to use
# labels = {}
# label =  []
# outlier_percent = []
#
# def dbscan_model(data):
#     for i in np.linspace(0.01, 3):
#         db = DBSCAN(eps=i, min_samples=78)
#         db.fit(data)
#         label_db = db.labels_
#         labels[i] = labels
#         label.append(label_db)
#         perc_outliers = 100 * np.sum(db.labels_ == -1) / len(db.labels_)
#         outlier_percent.append(perc_outliers)
#     return labels, label
#
# db = DBSCAN(eps =0.8, min_samples = 78)
# data_0['clusters'] = db.fit_predict(data_scaled)

#creating a function using the choosen eps
def final_prediction(
                     CHLA,ALK,TDP,TDN,K,MG,SRSI,MN,CL,FE,SO4,DOC,NO3,
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
        'NO2': NO2, 'PARTC': PARTC,'SECCHI_DEPTHS': SECCHI_DEPTHS,
        'MEAN_DAILY_DISCHARGE': MEAN_DAILY_DISCHARGE
    }

    single_data = pd.DataFrame(data, index = [0])
    min_max = MinMaxScaler(feature_range=(0.1, 1))
    single_prediction = pd.concat([data_scaled, single_data], axis=0)
    single_data = pd.DataFrame(min_max.fit_transform(single_prediction), columns=single_prediction.columns)
    db = DBSCAN(eps=0.2, min_samples=50)
    prediction = db.fit_predict(single_data)
    single_prediction['clusters'] = pd.DataFrame(prediction)
    return single_prediction.iloc[-1, -1]

# #data_0.drop(["TREATMENT","SITE", "ACTIVITY_START_DATE"], axis=1, inplace=
# to test the prediction model
result = final_prediction(
CHLA=1.65,
ALK=18,
TDP=6,
TDN=511,
K=0.04,
MG=0.61,
SRSI=4.77,
MN=0,
CL=0.12,
FE=0.41,
SO4=2.16,
DOC=1840,
NO3=5,
PARTN=0,
NA=1.01,
COND=22,
NH3=17,
DIC=304,
PARTP=2,
PH=4.86,
CA=1.99,
NO2=2,
PARTC=296,
SECCHI_DEPTHS=4.25,
MEAN_DAILY_DISCHARGE=0.01)

print(result)