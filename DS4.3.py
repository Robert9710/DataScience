# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import pylab as plt
import seaborn as sb
from IPython.display import Image
from IPython.core.display import HTML
from pylab import rcParams

import sklearn
from sklearn import decomposition
from sklearn.decomposition import PCA

from sklearn import datasets

rcParams['figure.figsize']=5,4
sb.set_style('whitegrid')

iris=datasets.load_iris()
x=iris.data
variable_names=iris.feature_names

pca=decomposition.PCA()
iris_pca=pca.fit_transform(x)

print(pca.explained_variance_ratio_)

print(pca.explained_variance_ratio_.sum())

comps=pd.DataFrame(pca.components_, columns=variable_names)
print(comps)

sb.heatmap(comps)







