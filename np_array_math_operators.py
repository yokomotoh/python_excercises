#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 14:59:43 2019
numpy array math operators
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

a = arrays(arr,int(N),int(M))

arr=[]
for i in range(int(N)):
    arr.append(input().strip().split(' '))

b = arrays(arr,int(N),int(M))

#a = numpy.array([[1, 2],[3, 4]], float)
#b = numpy.array([[5, 6],[7, 8]], float)

#print(a + b)                     #[  6.   8.  10.  12.]
print(numpy.add(a, b))           #[  6.   8.  10.  12.]

#print(a - b)                     #[-4. -4. -4. -4.]
print(numpy.subtract(a, b))      #[-4. -4. -4. -4.]

#print(a * b)                     #[  5.  12.  21.  32.]
print(numpy.multiply(a, b))      #[  5.  12.  21.  32.]

print(a // b)                     #[ 0.2         0.33333333  0.42857143  0.5       ]
#print(numpy.divide(a, b))        #[ 0.2         0.33333333  0.42857143  0.5       ]

#print(a % b)                     #[ 1.  2.  3.  4.]
print(numpy.mod(a, b))           #[ 1.  2.  3.  4.]

#print(a**b)                      #[  1.00000000e+00   6.40000000e+01   2.18700000e+03   6.55360000e+04]
print(numpy.power(a, b))         #[  1.00000000e+00   6.40000000e+01   2.18700000e+03   6.55360000e+04]