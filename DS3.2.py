# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from numpy.random import randn
from pandas import Series, DataFrame

import scipy
from scipy import stats

address='mtcars.csv'
cars=pd.read_csv(address)
cars.columns=['car_name','mpg','cyl','disp','hp','drat',
              'wt','qsec','vs','am','gear','carb']

#print(cars.sum())
#print(cars.sum(axis=1))

'''Finds the median value for each column'''
#print(cars.median())

'''average of each column'''
#print(cars.mean())

#print(cars.max())

mpg=cars.mpg
#print(mpg.idxmax())

'''Standard deviation'''
#print(cars.std())

'''Variance'''
#print(cars.var())

'''Count how many times a value appear'''
gear=cars.gear
#print(gear.value_counts())

'''Full statistics'''
print(cars.describe())











