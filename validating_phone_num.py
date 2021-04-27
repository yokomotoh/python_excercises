#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 16:05:31 2019
Validating phone numbers
@author: yoko
"""
import re

N=int(input())
str_input=[]
for i in range(N):
    str_input.append(input())

for i in range(N):
    #print(str(bool(re.match(r'^[789]{1}[0-9]{9}$',str_input[i]))))
    if bool(re.match(r'^([789]{1}[0-9]{9})$',str_input[i]))==True:
        print('YES')
    else:
        print('NO')
