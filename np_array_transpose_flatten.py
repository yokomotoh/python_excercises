#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 15:27:06 2019
numpy array Transpose and Flatten
@author: yoko
"""

import numpy

def arrays(arr,n,m):
    tmp=numpy.array(arr,int)
    return numpy.reshape(tmp,(n,m))

N, M = input().split(' ')
arr=[]
for i in range(int(N)):
    arr.append(input().strip().split(' '))

result = arrays(arr,int(N),int(M))
print(result.transpose())
print(result.flatten())