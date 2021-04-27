#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 10:29:56 2019
Dictionaries and Maps
@author: yoko
"""

#######

N = int(input())
    
input_list = []
n = N
tmp = []
for i in range(n):
    arr = list(map(str, input().split()))
    tmp.append(arr)

tmp2 = []
input_name = []
#while True:
#    input_name = list(map(str, input().split()))
#    if input_name != []:
#        #tmp2.append(input_name)
#        tmp2=tmp2+input_name
#    else:
#        break

try:
    while True:
        input_name = str(input())
        if len(input_name) != 0:
            tmp2.append(input_name)
        else:
            break
except EOFError:
    pass

def Convert(tup, di): 
    for a, b in tup: 
        #di.setdefault(a, []).append(b) 
        di[a]=b
    return di 

dictionary={}
Convert(tmp, dictionary)

for a in tmp2:
    if a in dictionary.keys():
        print('%s = %s' %(a,dictionary[a]))
    else:
        print('Not found')
    

