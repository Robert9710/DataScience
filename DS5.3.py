# -*- coding: utf-8 -*-
import pandas as pd
import sklearn
from sklearn.cluster import DBSCAN
from collections import Counter
import matplotlib.pyplot as plt
from pylab import rcParams
import seaborn as sb

rcParams['figure.figsize']=10,8
sb.set_style('whitegrid')

data=df.iloc[:,0:4].values
target=df.iloc[:,4].values

print(data)

#print(df[:5])

'''Maximum distance of 0.8 between 2 samples
to be considered in the same neighbourhood
and a minimum of 19 samples to be 
considered a core point'''
model=DBSCAN(eps=0.8, min_samples=19).fit(data)

#print(model)


outliers_df=pd.DataFrame(data)

'''See how many data points are being
assigned to each label'''
print(Counter(model.labels_))

print(outliers_df[model.labels_==-1])

fig=plt.figure()
ax=fig.add_axes([.1,.1,1,1])

colors=model.labels_

ax.scatter(data[:,2],data[:,1],c=colors, s=120)
ax.set_xlabel('Petal Length')
ax.set_ylabel('Sepal Width')
plt.title('DBScan for Outlier Detection')








