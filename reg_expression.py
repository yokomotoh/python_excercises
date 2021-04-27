#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 15:29:16 2019
regular_expression
@author: yoko
"""


#regex_pattern = r'\d+'	# Do not delete 'r'.

import re
#print("\n".join(re.split(regex_pattern, input())))
str_input=input()

#x = re.findall(r"\w+", str_input)

x = re.findall(r"[a-zA-Z0-9]+", str_input)
#print("The first white-space character is located in position:", x.start()) 
#print(x)

tmp=''
eof=False
for i in x:
    for j in range(len(i)-1):
        if i[j]==i[j+1]:
            tmp = i[j]
            eof=True
            break
    if eof==True:
        break
if eof==False:
    print('-1')
else:
    print(tmp)
#for i in range(x.start(),len(str_input)-1):
#    if str_input[i]==str_input[i+1]:
#        print(str_input[i])
#        break
#    

#import re
#m = re.match(r'(\w+)@(\w+)\.(\w+)','username@hackerrank.com')
#m.groups()