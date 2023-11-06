'''
Data preprocessing

'''


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

data = pd.read_csv("../datasets/data.csv")
data.head()
data.drop('S/N', axis=1, inplace=True)


# creating a function to change the date for modelling
def date_transform(data):
    base_line = pd.to_datetime('2015-01-01')
    new_date = data['ACTIVITY_START_DATE'].apply((lambda x: pd.to_datetime(x) - base_line))
    data['ACTIVITY_START_DATE'] = new_date.dt.days
    return data


data = date_transform(data)
data.head()

# changing the categorical data into numerical values
features = [col for col in data.columns if data[col].dtype == 'object'
            and data[col].nunique() == 5]


def cat_value(data):
    return pd.get_dummies(data)


cat_data = data[features]
data.drop(features, axis=1, inplace=True)
# call the function
cat_values = cat_value(cat_data)
data = pd.concat([data, cat_values], axis=1)
data.head()
data_1 = data[data["TREATMENT"] == 1]
data_0 = data[data["TREATMENT"] == 0]

#creating a function to convert the missing values to median
def missing_values(train_dataset):
    #changing null values to the modal scores
    imputer = SimpleImputer(strategy='mean')
    imputer.fit(train_dataset)
    train_data = pd.DataFrame(imputer.transform(train_dataset))
    train_data.columns = train_dataset.columns
    return train_data
missing_values(data_1)
missing_values(data_0)

outlier_counts = {}
#function to check outliers using interquartile range
lower_bound = 0
upper_bound = 0
def check_outliers(train_data, data_set):
    outliers = []
    count = 0
    dates = []
    outlier_counts = {}
    q1 = train_data.quantile(0.25)
    q3 = train_data.quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - (1.5 * iqr)
    upper_bound = q3 + (1.5 * iqr)
    for x in range(len(train_data)):
        outlier_counts = {}

        if (train_data[x] < lower_bound) or (train_data[x] > upper_bound):
            outliers.append(train_data[x])
            count += 1
            dates.append(data_set.loc[x])
    return outliers,dates
#calling the outliers function
def calling_outliers(data):
    alk = {}
    for i in data.columns:
        alk = check_outliers(data[i],data["ACTIVITY_START_DATE"])
        length = len(alk[0])
        if len(alk[0]) !=0:
            alk =dict(zip(alk[0], alk[1]))