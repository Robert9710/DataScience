# -*- coding: utf-8 -*-
import numpy as np
from numpy.random import randn

np.set_printoptions(precision=2)

a=np.array([1,2,3,4,5,6])
b=np.array([[10,20,30], [40,50,60]])

np.random.seed(25)
c=36*np.random.randn(6)

d=np.arange(1,35)

"""
print(c*a)
print(c/a)
"""

aa=np.array([[2.,4.,6.],[1.,3.,5.],[10.,20.,30.]])
#print(aa)

bb=np.array([[0.,1.,2.],[3.,4.,5.],[6.,7.,8.]])
#print(bb)

"""Matrix multiplication"""
#print(np.dot(aa,bb))


























