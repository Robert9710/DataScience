# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

import matplotlib.pyplot as plt
from pylab import rcParams

import seaborn as sb

'''x=range(1,10)
y=[1,2,3,4,0.5,4,3,2,1]
#plt.bar(x,y)

#plt.xlabel('you x-axis label')
#plt.ylabel('you y-axis label')

z=[1,2,3,4,0.5]
veh_type=['bicycle','motorbike','car','van','stroller']
#plt.pie(z,labels=veh_type)
#plt.show()
'''
address='mtcars.csv'
cars=pd.read_csv(address)
cars.columns=['car_name','mpg','cyl','disp','hp','drat',
              'wt','qsec','vs','am','gear','carb']

mpg=cars.mpg

fig=plt.figure()
ax=fig.add_axes([.1,.1,1,1])

mpg.plot()
'''
ax.set_xticks(range(32))

ax.set_xticklabels(cars.car_name, rotation=90, fontsize='large')
ax.set_title('Miles per galon of cars in mtcars')

ax.set_xlabel('car_names')
ax.set_ylabel('miles per galon')
'''
#plt.pie(z)
#plt.legend(veh_type,loc='best')
#plt.show()

fig=plt.figure()
ax=fig.add_axes([.1,.1,1,1])
mpg.plot()

#ax.set_xticks(range(32))

#ax.set_xticklabels(cars.car_name, rotation=90, fontsize='large')
ax.set_title('Miles per galon of cars in mtcars')

#ax.set_xlabel('car_names')
ax.set_ylabel('miles per galon')

#ax.legend(loc='best')

ax.set_ylim([0,45])

'''xy,xytext-> coordinates for arrow and text'''
ax.annotate('Toyota Corolla', xy=(19,33.9), xytext=(23,35), arrowprops=dict(facecolor='black',shrink=0.05))

#print(mpg.max())







