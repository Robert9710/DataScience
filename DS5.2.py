# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
from pylab import rcParams
import seaborn as sb

rcParams['figure.figsize']=10,8
sb.set_style('whitegrid')

df=pd.read_csv(filepath_or_buffer='iris.data.csv',header=None,sep=',')
df.columns=['Sepal Length','Sepal Width','Petal Length','Petal Width','Species']

data=df.iloc[:,0:4].values
target=df.iloc[:,4].values

print(df[:5])

sb.boxplot(x='Species',y='Sepal Length', data=df, palette='hls')

sb.pairplot(df, hue='Species', palette='hls')













