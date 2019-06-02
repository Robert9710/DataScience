# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import sklearn
from sklearn import datasets
import matplotlib.pyplot as plt
from pylab import rcParams

rcParams['figure.figsize']=5,4

df=pd.read_csv(filepath_or_buffer='iris.data.csv',header=None,sep=',')
df.columns=['Sepal Length','Sepal Width','Petal Length','Petal Width','Species']

x=df.iloc[:,0:4].values
y=df.iloc[:,4].values

#print(df[:5])

df.boxplot(return_type='dict')
plt.plot()

Sepal_width=x[:,1]
iris_outliers=Sepal_width>4
print(df[iris_outliers])

Sepal_width=x[:,1]
iris_outliers=Sepal_width<2.05
print(df[iris_outliers])

pd.options.display.float_format='{:.1f}'.format
x_df=pd.DataFrame(x)
print(x_df.describe())






