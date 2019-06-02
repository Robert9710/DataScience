# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

from pandas import Series, DataFrame

address = 'mtcars.csv'
cars=pd.read_csv(address)
cars.columns=['car_name','mpg','cyl','disp','hp','drat',
              'wt','qsec','vs','am','gear','carb']
print(cars.head())

cars_groups = cars.groupby(cars['cyl'])
print(cars_groups.mean())