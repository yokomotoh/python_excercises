#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 17:52:24 2019

@author: vincent
"""
str_input=input()
import re
#x=re.findall(r'[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]([AEIOUaeiou][AEIOUaeiou]+)[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]', str_input)
y=list(map(lambda x: x.group(),re.finditer(r'(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])([AEIOUaeiou][AEIOUaeiou]+)(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])',str_input)))
#for i in x:
#    print(i)
#if len(x)==0:
#    print('-1')

for i in y:
    print(i)
if len(y)==0:
    print('-1')
