#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 10:08:13 2019
Regex Substitution
@author: yoko
"""

import re

#html = """
#<head>
#<title>HTML</title>
#</head>
#<object type="application/x-flash" 
#  width="0" height="0">
#  <!-- <param name="movie"  value="your-file.swf" /> -->
#  <param name="quality" value="high"/>
#</object>
#"""
#
#print(re.sub("(<!--.*?-->)", "", html)) #remove comment

N=int(input())
str_input=[]
for i in range(N):
    str_input.append(input())
for i in range(N):
    tmp_substr=re.search('#',str_input[i])
    if tmp_substr!=None:
        tmp=re.sub(r'(?<= )(&&)(?= )', "and", str_input[i][:tmp_substr.start()])
        tmp2=re.sub(r'(?<= )(\|\|)(?= )', "or", tmp)
        tmp2 = tmp2+str_input[i][tmp_substr.start():]
    #str_input[i] == r'(?#\s+)':
    else:
        tmp=re.sub(r'(?<= )(&&)(?= )', "and", str_input[i])
        tmp2=re.sub(r'(?<= )(\|\|)(?= )', "or", tmp)
    print(tmp2)
