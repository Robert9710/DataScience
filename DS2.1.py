# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from numpy.random import randn
from pandas import Series, DataFrame

import matplotlib.pyplot as plt
from matplotlib import rcParams
import seaborn as sb

rcParams['figure.figsize']= 10,8
sb.set_style('whitegrid')

x = range(1,10)
y = [1,2,3,4,0,4,3,2,1]

#plt.plot(x,y)

address = 'mtcars.csv'
cars=pd.read_csv(address)
cars.columns=['car_name','mpg','cyl','disp','hp','drat',
              'wt','qsec','vs','am','gear','carb']

mpg = cars['mpg']
#mpg.plot()

df=cars[['cyl','wt','mpg']]
#df.plot()

#plt.bar(x,y)

#mpg.plot(kind='bar')

#mpg.plot(kind='barh')

x=[1,2,3,4,0.5]

#plt.pie(x)
#plt.show()

#plt.savefig('pie_chart.png')
#plt.show()



