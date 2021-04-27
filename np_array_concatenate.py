#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 15:27:06 2019
numpy array concatenate
@author: yoko
"""

import numpy

def arrays(arr,n,m):
    tmp=numpy.array(arr,int)
    return numpy.reshape(tmp,(n,m))

N, M, P = input().split(' ')
arr1=[]
arr2=[]
for i in range(int(N)):
    arr1.append(input().strip().split(' '))
for i in range(int(M)):
    arr2.append(input().strip().split(' '))
result1 = arrays(arr1,int(N),int(P))
result2 = arrays(arr2,int(M),int(P))
#print(result1)
#print(result2)
print(numpy.concatenate((result1,result2),axis=0))
