#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 13:35:46 2019
capitalize
@author: yoko
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.

def capital(s):
     s[0].upper
def solve(s):
#    s1, s2  = s.split()
#    #print(s1[0].upper(), s2[0].upper())
#    #print(s1[1:(len(s1))],s2[1:(len(s2))])
#    tmp2 = s2[0].upper()+s2[1:(len(s2))]
#    tmp1 = s1[0].upper()+s1[1:(len(s1))]
#    return tmp1+' '+tmp2
#    

#    tmp_split = ""
#    tmp_split = s.split()
#    tmp=""
#    #print(tmp_split)
#    for i in range(len(tmp_split)):
#        tmp+=tmp_split[i][0].upper()
#        for j in range(1,len(tmp_split[i])):
#            tmp+=tmp_split[i][j]
#        tmp+=' '
#    return tmp

    tmp=""
    for i in range(0,len(s)):
        if s[i]==" ":
            tmp+=s[i]
        else:
            if (i==0 or s[i-1]==" "):
                tmp+=s[i].upper()
            else:
                tmp+=s[i]
    return tmp

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    print(result)
    #fptr.write(result + '\n')

    #fptr.close()