#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 11:58:08 2019
compress the string
@author: yoko
"""

#from collections import defaultdict

string = input()

#char=defaultdict(int)
#for element in string:
#    char[element]=char[element]+1
#
#print(char)

compress_str=[]
compress_str.append({string[0]:1})
for i in range(1,len(string)):
    if string[i-1]==string[i]:
        for key, value in compress_str[-1].items(): 
            compress_str[-1][string[i]]+=1
            #print(value)
        #print(compress_str[-1])
    else:
        compress_str.append({string[i]:1})

for tmp in compress_str:
    for key, value in tmp.items():
        print('(%d, %d) ' %(value,int(key)), end='')