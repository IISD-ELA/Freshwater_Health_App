#Ml Model implementation here
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
from xgboost import XGBClassifier
import matplotlib.pyplot as plt

import pickle
import numpy as np
import pandas as pd
import seaborn as sns
''' 

x = [4, 5, 10, 4, 3, 11, 14 , 6, 10, 12]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]


plt.scatter(x, y)
#plt.show()

#Turn the data into a set of points:
data = list(zip(x,y))
inertias = []

for i in range (1,11):
    kmeans = KMeans(n_clusters=i)
    kmeans.fit(data)
    inertias.append(kmeans.inertia_)

plt.plot(range(1,11), inertias, marker='o')
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia')
#plt.show()


kmeans = KMeans(n_clusters=2)
kmeans.fit(data)

plt.scatter(x, y, c=kmeans.labels_)
#plt.show()

#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
#model = XGBClassifier(random_state=0)
#model.fit(X_train, y_train)
'''

def predictHealthOfDrinkingWater():
    #prediction code here
    return np.random.rand(2)

def predictHealthOfAquaticLife():
    # prediction code here
    return np.random.rand(2)

#pickle.dump(model, open('model.pkl', 'wb'))

