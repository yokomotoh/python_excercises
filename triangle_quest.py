#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 12:49:20 2019
Triangle Quest
@author: yoko
"""

for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
#    print(sum(i*(10**j) for j in range(i)))
    print(sum(list(map(lambda x: i*(10**x), range(i)))))