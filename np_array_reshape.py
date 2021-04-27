#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 15:19:57 2019
numpy array reshape
@author: vincent
"""

import numpy

def arrays(arr):
    tmp=numpy.array(arr,int)
    return numpy.reshape(tmp,(3,3))

arr = input().strip().split(' ')
result = arrays(arr)
print(result)