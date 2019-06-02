# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import sklearn
from sklearn.cluster import AgglomerativeClustering

import sklearn.metrics as sm

import scipy
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.cluster.hierarchy import fcluster
from scipy.cluster.hierarchy import cophenet
from scipy.spatial.distance import pdist

from pylab import rcParams
import seaborn as sb

np.set_printoptions(precision=4,suppress=True)
plt.figure(figsize=(15,8))
plt.style.use('seaborn-whitegrid')


address='mtcars.csv'
cars=pd.read_csv(address)
cars.columns=['car_name','mpg','cyl','disp','hp','drat',
              'wt','qsec','vs','am','gear','carb']

x=cars.ix[:,(1,3,4,6)].values
y=cars.iloc[:,(9)].values

z=linkage(x, 'ward')
'''dendrogram(z,truncate_mode='lastp',p=12,
           leaf_rotation=45.,leaf_font_size=15.,
           show_contracted=True)

plt.title('Truncated Hierarchical Clustering Dendrogram')
plt.xlabel('Cluster Size')
plt.ylabel('Distance')
plt.xticks(fontsize='20')
plt.yticks(fontsize='20')
plt.axhline(y=500)
plt.axhline(y=150)
#plt.show()
'''
k=2

Hclustering=AgglomerativeClustering(n_clusters=k,
                                    affinity='manhattan',
                                    linkage='average')
Hclustering.fit(x)

print(sm.accuracy_score(y, Hclustering.labels_))


