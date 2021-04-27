#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 15:27:06 2019
numpy itertools.product()
@author: yoko
"""

from itertools import product

#print(list(product([1,2,3],repeat = 2)))
##[(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
#
#print(list(product([1,2,3],[3,4])))
##[(1, 3), (1, 4), (2, 3), (2, 4), (3, 3), (3, 4)]
#
#A = [[1,2,3],[3,4,5]]
#print(list(product(*A)))
##[(1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 3), (3, 4), (3, 5)]
#
#B = [[1,2,3],[3,4,5],[7,8]]
#print(list(product(*B)))
#
#
#A = [1, 2]
#B = [3, 4]
#
##AxB = [(1, 3), (1, 4), (2, 3), (2, 4)]
#print(list(product(A,B)))

input_list1 = sorted(list(map(int, input().strip().split(' '))))
input_list2 = sorted(list(map(int, input().strip().split(' '))))

for elm in list(product(input_list1,input_list2)):
    print(elm, end="")

#import numpy
#
#def arrays(arr,n,m):
#    tmp=numpy.array(arr,float)
#    return numpy.reshape(tmp,(n,m))
#
#n = int(input())
##n=0
##arr_param = input().strip().split(' ')
#
#arr=[]
#for i in range(n):
#    arr.append(list(map(float, input().strip().split(' '))))
##poly_coefficients = list(map(float, input().strip().split(' ')))
##x = float(input())
#my_array=arrays(arr, n, n)
##my_poly=numpy.array(poly_coefficients, float)
#
#
##my_array2=my_array2.transpose()
#numpy.set_printoptions(sign=' ')
##print(numpy.polyval(my_poly, x))
##print(numpy.roots(my_poly))
#print(numpy.round(numpy.linalg.det(my_array), 2))




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


