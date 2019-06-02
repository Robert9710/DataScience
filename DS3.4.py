# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from pylab import rcParams

import seaborn as sb

import scipy
from scipy.stats.stats import pearsonr

rcParams['figure.figsize']=8,4
plt.style.use('seaborn-whitegrid')

address='mtcars.csv'
cars=pd.read_csv(address)
cars.columns=['car_name','mpg','cyl','disp','hp','drat',
              'wt','qsec','vs','am','gear','carb']

sb.pairplot(cars)

x=cars[['mpg','hp','qsec','wt']]
#sb.pairplot(x)

mpg=cars['mpg']
hp=cars['hp']
qsec=cars['qsec']
wt=cars['wt']

pearsonr_coeficient, p_value=pearsonr(mpg,hp)
#print('%0.3f' % pearsonr_coeficient)

pearsonr_coeficient, p_value=pearsonr(mpg,qsec)
#print('%0.3f' % pearsonr_coeficient)

pearsonr_coeficient, p_value=pearsonr(mpg,wt)
#print('%0.3f' % pearsonr_coeficient)

corr=x.corr()
#print(corr)

sb.heatmap(corr,xticklabels=corr.columns.values
           , yticklabels=corr.columns.values)






