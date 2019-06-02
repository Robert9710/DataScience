# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
from sklearn.cluster import KMeans
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import scale
import sklearn.metrics as sm
from sklearn import datasets
from sklearn.metrics import confusion_matrix, classification_report

plt.figure(figsize=(12,7))

iris=datasets.load_iris()

x=scale(iris.data)
y=pd.DataFrame(iris.target)
variable_names=iris.feature_names
#print(x[0:10,])

clustering=KMeans(n_clusters=3, random_state=5)

print(clustering.fit(x))

iris_df=pd.DataFrame(iris.data)
iris_df.columns=['Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width']
y.columns=['Targets']

color_theme=np.array(['darkgray', 'lightsalmon', 'powderblue'])
'''
plt.subplot(1,2,1)
plt.scatter(x=iris_df.Petal_Length, y=iris_df.Petal_Width, c=color_theme[iris.target], s=50)
plt.title('Ground Truth Classification')

plt.subplot(1,2,2)
plt.scatter(x=iris_df.Petal_Length, y=iris_df.Petal_Width, c=color_theme[clustering.labels_], s=50)
plt.title('KMeans Classification')
'''
relabel=np.choose(clustering.labels_, [2,0,1]).astype(np.int64)

plt.subplot(1,2,1)
plt.scatter(x=iris_df.Petal_Length, y=iris_df.Petal_Width, c=color_theme[iris.target], s=50)
plt.title('Ground Truth Classification')

plt.subplot(1,2,2)
plt.scatter(x=iris_df.Petal_Length, y=iris_df.Petal_Width, c=color_theme[relabel], s=50)
plt.title('KMeans Classification')

print(classification_report(y,relabel))


