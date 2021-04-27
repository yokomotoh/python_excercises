#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 12:52:16 2019
DefaultDict
@author: yoko
"""

from collections import defaultdict

d = defaultdict(list)

#d['a'].append(1)
#d['a'].append(2)
#d['b'].append(3)
#d['a'].append(4)
#d['b'].append(5)

input_nm = []
input_nm = list(map(int, input().split()))
n = input_nm[0]
m = input_nm[1]


for i in range(n):
    d[str(input())].append(i+1)

tmp = []
for i in range(m):
    tmp.append(str(input()))

for j in tmp:
    if j in d:
        for k in d[j]:
            print('%d ' %k, end='')
        print('\n', end='')
    else:
        print('-1 \n', end='')
#for i in d.items():
#    print(i)

#for j in d:
#    print(d[j])
