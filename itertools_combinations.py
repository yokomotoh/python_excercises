#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 11:04:51 2019
itertools.combinations()
@author: vincent
"""

from itertools import combinations

tmp1, tmp2 = input().split()
string = tmp1
k = int(tmp2)

for i in range(1,k+1):
    tmp_list=sorted(list(combinations(sorted(string),i)))
    #print(tmp_list)
    for j in tmp_list:
        for k in j:
            print(k, end='')
        print('')