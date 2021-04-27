#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 15:27:06 2019
numpy array linear algebra: determinant, eigenvalue eigenvector, inverse
@author: yoko
"""


import numpy

def arrays(arr,n,m):
    tmp=numpy.array(arr,float)
    return numpy.reshape(tmp,(n,m))

n = int(input())
#n=0
#arr_param = input().strip().split(' ')

arr=[]
for i in range(n):
    arr.append(list(map(float, input().strip().split(' '))))
#poly_coefficients = list(map(float, input().strip().split(' ')))
#x = float(input())
my_array=arrays(arr, n, n)
#my_poly=numpy.array(poly_coefficients, float)


#my_array2=my_array2.transpose()
numpy.set_printoptions(sign=' ')
#print(numpy.polyval(my_poly, x))
#print(numpy.roots(my_poly))
print(numpy.round(numpy.linalg.det(my_array), 2))




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


