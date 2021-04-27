#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 11:04:51 2019
itertools.combinations()
@author: vincent
"""
from itertools import combinations
from itertools import combinations_with_replacement

tmp1, tmp2 = input().split()
string = tmp1
k = int(tmp2)

i=k
tmp_list_replacement=sorted(list(combinations_with_replacement(sorted(string),i)))
tmp_list=sorted(list(combinations(sorted(string),i)))

##print(tmp_list_replacement)
#print('combinations_with_replacement')
#for j in tmp_list_replacement:
#    for k in j:
#        print(k, end='')
#    print('')
#
##print(tmp_list)
#print('combinations')
#for j in tmp_list:
#    for k in j:
#        print(k, end='')
#    print('')

for l in tmp_list_replacement:
    if l in tmp_list:
        pass
    else:
        tmp_list.append(l)
#print('adjusted')
for j in sorted(tmp_list):
    for k in j:
        print(k,end='')
    print('')