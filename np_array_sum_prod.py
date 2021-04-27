#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 15:27:06 2019
numpy array sum and prod
@author: yoko
"""

import numpy

def arrays(arr,n,m):
    tmp=numpy.array(arr,int)
    return numpy.reshape(tmp,(n,m))

N, M= input().split(' ')
#arr_param = input().strip().split(' ')

#print(list(map(int, arr_param))) 
#print(numpy.zeros(list(map(int, arr_param)), dtype=numpy.int))
#print(numpy.ones(list(map(int, arr_param)), dtype=numpy.int))   

#print(numpy.zeros((int(N),int(M),int(L)), dtype = numpy.int))
#print(numpy.ones((int(N),int(M),int(L)), dtype = numpy.int))
arr=[]
#arr2=[]
for i in range(int(N)):
    arr.append(list(map(int, input().strip().split(' '))))
#arr = list(map(int, arr))
#print(numpy.sum(arr, axis = 0))
print(numpy.prod(numpy.sum(arr, axis = 0), axis = None))
#for i in range(int(M)):
#    arr2.append(input().strip().split(' '))
#result1 = arrays(arr1,int(N),int(P))
#result2 = arrays(arr2,int(M),int(P))
##print(result1)
##print(result2)
#print(numpy.concatenate((result1,result2),axis=0))
