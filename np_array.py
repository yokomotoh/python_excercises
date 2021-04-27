#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 14:22:25 2019
numpy arrays
@author: yoko
"""

import numpy

def arrays(arr):
    tmp=numpy.array(arr,float)
    return numpy.flip(tmp,0)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)