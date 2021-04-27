#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 15:27:06 2019
numpy array eye and identity
@author: yoko
"""

import numpy

def arrays(arr,n,m):
    tmp=numpy.array(arr,int)
    return numpy.reshape(tmp,(n,m))

N, M = input().split(' ')
numpy.set_printoptions(sign=' ')
#print(numpy.identity(3))
print(numpy.eye(int(N), int(M), k = 0))
#arr=[]
#for i in range(int(N)):
#    arr.append(input().strip().split(' '))
#
#result = arrays(arr,int(N),int(M))
#print(result.transpose())
#print(result.flatten())