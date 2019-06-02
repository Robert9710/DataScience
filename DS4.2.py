# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

import sklearn
from sklearn.decomposition import FactorAnalysis

from sklearn import datasets

iris=datasets.load_iris()
x=iris.data

variable_names=iris.feature_names

print(x[0:10])

factor=FactorAnalysis().fit(x)

print(pd.DataFrame(factor.components_,columns=variable_names))

