# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

from pandas import Series, DataFrame

"""Series"""
series_obj=Series(np.arange(8), index=['row 1','row 2','row 3','row 4','row 5','row 6','row 7','row 8'])
print(series_obj)

print(series_obj['row 7'])

print(series_obj[[0,7]])

"""Create and display a table"""
np.random.seed(25)
DF_obj=DataFrame(np.random.rand(36).reshape((6,6)),
                 index=['row 1','row 2','row 3','row 4','row 5','row 6'],
                 columns=['column 1','column 2','column 3','column 4','column 5','column 6'])
print(DF_obj)
print()

"""Display specific rows and columns from table"""
print(DF_obj.loc[['row 2', 'row 5'], ['column 5', 'column 2']])
print()

"""Slicing"""
print(series_obj['row 3':'row 7'])

print(DF_obj<.2)
print()

print(series_obj[series_obj>6])
print()

series_obj['row 1','row 5', 'row 8']=8
print(series_obj)
