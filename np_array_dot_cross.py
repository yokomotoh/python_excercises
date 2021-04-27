#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 15:27:06 2019
numpy array mean var std
@author: yoko
"""

import numpy

def arrays(arr,n,m):
    tmp=numpy.array(arr,int)
    return numpy.reshape(tmp,(n,m))

n = int(input())
#arr_param = input().strip().split(' ')

arr=[]
for i in range(n):
    arr.append(list(map(int, input().strip().split(' '))))
#arr = list(map(int, arr))
my_array1=arrays(arr, n, n)

arr=[]
for i in range(n):
    arr.append(list(map(int, input().strip().split(' '))))
#arr = list(map(int, arr))
my_array2=arrays(arr, n, n)
my_array2=my_array2.transpose()

my_array3=[]
for i in range(n):
    for j in range(n):
        my_array3.append(numpy.dot(my_array1[i],my_array2[j]))

my_array3=arrays(my_array3,n,n)

numpy.set_printoptions(sign=' ')
print(my_array3)

#print(numpy.mean(my_array, axis = 0))        #Output : [ 2.  3.]
#print(numpy.mean(my_array, axis = 1))        #Output : [ 1.5  3.5]
#print(numpy.mean(my_array, axis = None))     #Output : 2.5
#print(numpy.mean(my_array))                  #Output : 2.5

#print(numpy.var(my_array, axis = 0))         #Output : [ 1.  1.]
#print(numpy.var(my_array, axis = 1))         #Output : [ 0.25  0.25]
#print(numpy.var(my_array, axis = None))      #Output : 1.25
#print(numpy.var(my_array))                   #Output : 1.25

#print(numpy.std(my_array, axis = 0))         #Output : [ 1.  1.]
#print(numpy.std(my_array, axis = 1))         #Output : [ 0.5  0.5]
#print(round(numpy.std(my_array, axis = None), 12))      #Output : 1.11803398875
#print(numpy.std(my_array))                   #Output : 1.11803398875


