# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

import matplotlib.pyplot as plt
from pylab import rcParams

import seaborn as sb

rcParams['figure.figsize']=5,4
sb.set_style('whitegrid')

x= range(1,10)
y=[1,2,3,4,0.5,4,3,2,1]

#plt.bar(x,y)

wide=[0.5,0.5,0.5,0.9,0.9,0.9,0.5,0.5,0.5]
color=['salmon']
#plt.bar(x,y, width=wide,color=color,align='center')

address='mtcars.csv'
cars=pd.read_csv(address)
cars.columns=['car_name','mpg','cyl','disp','hp','drat',
              'wt','qsec','vs','am','gear','carb']

df = cars[['cyl','mpg','wt']]
#df.plot()

color_theme=['darkgray','lightsalmon','powderblue']
#df.plot(color=color_theme)

z=[1,2,3,4,0.5]
#plt.pie(z)
#plt.show()

color_theme=['#A9A9A9','#FFA07A','#B0E0E6','#FFE3C4','#BDB643']
#plt.pie(z,colors=color_theme)
#plt.show()

x1=range(0,10)
y1=[10,9,8,7,6,5,4,3,2,1]

#plt.plot(x,y)
#plt.plot(x1,y1)

#plt.plot(x,y, ls='steps',lw=5)
#plt.plot(x1,y1,ls='--',lw=10)

plt.plot(x,y,marker='1',mew=20)
plt.plot(x1,y1,marker='+',mew=15)





