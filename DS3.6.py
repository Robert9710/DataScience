# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import scipy

import matplotlib.pyplot as plt
from matplotlib import rcParams
import seaborn as sb

import sklearn
from sklearn import preprocessing
from sklearn.preprocessing import scale

rcParams['figure.figsize']=14, 7
plt.style.use('seaborn-whitegrid')

address='mtcars.csv'
cars=pd.read_csv(address)
cars.columns=['car_name','mpg','cyl','disp','hp','drat',
              'wt','qsec','vs','am','gear','carb']

mpg=cars.mpg
#plt.plot(mpg)

#print(cars[['mpg']].describe())

'''Normalize'''
mpg_matrix=mpg.values.reshape(-1,1)
scaled=preprocessing.MinMaxScaler()
scaled_mpg=scaled.fit_transform(mpg_matrix)
#plt.plot(scaled_mpg)

'''Standardize'''
standardized_mpg=scale(mpg,axis=0,with_mean=False,with_std=False)
#plt.plot(standardized_mpg)
standardized_mpg=scale(mpg)
plt.plot(standardized_mpg)







