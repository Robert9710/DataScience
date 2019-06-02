# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from numpy.random import randn
from pandas import Series, DataFrame
from matplotlib import rcParams

rcParams['figure.figsize']=5,4

x=range(1,10)
y=[1,2,3,4,0,4,3,2,1]

fig = plt.figure()

"""left, bottom, width, height"""
ax=fig.add_axes([.1, .1, 1, 1])

#ax.plot(x,y)

ax.set_xlim([0,9])
ax.set_ylim([0,10])

#ax.set_xticks([0,1,2,4,5,6,8,9,10])
# ax.set_yticks([0,1,2,3,4,5])

ax.plot(x)

"""Subplots"""
fig=plt.figure()
fig, (ax1, ax2) = plt.subplots(1,2)

ax1.plot(x)
ax2.plot(x,y)













