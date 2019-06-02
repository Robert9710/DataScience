# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from pylab import rcParams

import seaborn as sb

import scipy
from scipy.stats import spearmanr

rcParams['figure.figsize']=14, 7
plt.style.use('seaborn-whitegrid')

address='mtcars.csv'
cars=pd.read_csv(address)
cars.columns=['car_name','mpg','cyl','disp','hp','drat',
              'wt','qsec','vs','am','gear','carb']

#sb.pairplot(cars)

x=cars[['cyl','vs','am','gear']]
#sb.pairplot(x)

cyl=cars['cyl']
vs=cars['vs']
am=cars['am']
gear=cars['gear']

spearmanr_coefficient, p_value=spearmanr(cyl,vs)
print('%0.3f' % spearmanr_coefficient)

spearmanr_coefficient, p_value=spearmanr(cyl,am)
print('%0.3f' % spearmanr_coefficient)

spearmanr_coefficient, p_value=spearmanr(cyl,gear)
print('%0.3f' % spearmanr_coefficient)

'''Chi-square test'''
table=pd.crosstab(cyl,am)

'''p>0.5=>valus are independent''' 
from scipy.stats import chi2_contingency
chi2,p,dof,expected=chi2_contingency(table.values)
print('%0.3f %0.3f'% (chi2,p))

table=pd.crosstab(cyl,cars['vs'])
chi2,p,dof,expected=chi2_contingency(table.values)
print('%0.3f %0.3f'% (chi2,p))

table=pd.crosstab(cyl,cars['gear'])
chi2,p,dof,expected=chi2_contingency(table.values)
print('%0.3f %0.3f'% (chi2,p))



