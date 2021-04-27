#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 08:15:56 2019
Validating and Parsing Email Addresses

42/115 challenges solved
Rank: 21759|Points: 685
Python
@author: yoko
"""
import re

N=int(input())
str_input=[]
for i in range(N):
    str_input.append(input())

for i in range(N):
    #print(str(bool(re.match(r'^[789]{1}[0-9]{9}$',str_input[i]))))
    if bool(re.match(r"[\w\ ]*\<[a-zA-Z0-9]{1}[a-zA-Z0-9.\-\_]*\@[a-zA-Z]*\.[a-zA-Z]{1,3}\>",str_input[i]))==True:
#    print(bool(re.match(r"(?:\<)(^\w[\w\.\-\_]*\@[a-zA-Z]*\.[a-zA-Z]{2,4})(?:\>)",str_input[i])))
        print(str_input[i])
        
#matchObj = re.search(r"(?:\b)([^\s]*\@[^\s]*\.[a-zA-Z]{2,4})(?:\b)",testString)