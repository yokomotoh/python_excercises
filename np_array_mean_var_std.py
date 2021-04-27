#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 15:27:06 2019
numpy array mean var std
@author: yoko
"""

import numpy

def arrays(arr,n,m):
    tmp=numpy.array(arr,float)
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
    arr.append(list(map(float, input().strip().split(' '))))
#arr = list(map(int, arr))
my_array=arrays(arr, int(N),int(M))

numpy.set_printoptions(sign=' ')
#print(my_array)

#print(numpy.mean(my_array, axis = 0))        #Output : [ 2.  3.]
print(numpy.mean(my_array, axis = 1))        #Output : [ 1.5  3.5]
#print(numpy.mean(my_array, axis = None))     #Output : 2.5
#print(numpy.mean(my_array))                  #Output : 2.5

print(numpy.var(my_array, axis = 0))         #Output : [ 1.  1.]
#print(numpy.var(my_array, axis = 1))         #Output : [ 0.25  0.25]
#print(numpy.var(my_array, axis = None))      #Output : 1.25
#print(numpy.var(my_array))                   #Output : 1.25

#print(numpy.std(my_array, axis = 0))         #Output : [ 1.  1.]
#print(numpy.std(my_array, axis = 1))         #Output : [ 0.5  0.5]
print(round(numpy.std(my_array, axis = None), 12))      #Output : 1.11803398875
#print(numpy.std(my_array))                   #Output : 1.11803398875


