#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 14:59:43 2019
numpy array Floor, Ceil and Rint
@author: yoko
"""

import numpy

#def arrays(arr,n,m):
#    tmp=numpy.array(arr,int)
#    return numpy.reshape(tmp,(n,m))
#
#N, M = input().split(' ')
#
#arr=[]
#for i in range(int(N)):

arr = input().strip().split(' ')
arr = list(map(float, arr)) 

numpy.set_printoptions(sign=' ')
print(numpy.floor(arr))
print(numpy.ceil(arr))
print(numpy.rint(arr))
