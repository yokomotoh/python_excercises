#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 14:59:48 2019
Hex Color Code
@author: yoko
"""

import re

N=int(input())
str_input=[]
for i in range(N):
    str_input.append(input())

for i in range(N):
    #print(str(bool(re.match(r'^[789]{1}[0-9]{9}$',str_input[i]))))
#    color_value=re.findall(r"(?:\:){1}[\w\d\s\-\_\(\)\[\]\{\}\,\.\']*(\#[0-9A-Fa-f]{6}|\#[0-9A-Fa-f]{3})",str_input[i])
    colon_place=re.search(r"(?:\:)",str_input[i])
    if colon_place:
        color_value=re.findall(r"(\#[0-9A-Fa-f]{6}|\#[0-9A-Fa-f]{3})",str_input[i][colon_place.end():])
        if bool(color_value)==True:
#    print(bool(re.match(r"(?:\<)(^\w[\w\.\-\_]*\@[a-zA-Z]*\.[a-zA-Z]{2,4})(?:\>)",str_input[i])))
                for x in color_value: print(str(x))
    else:
        pass
#matchObj = re.search(r"(?:\b)([^\s]*\@[^\s]*\.[a-zA-Z]{2,4})(?:\b)",testString)