#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 15:02:11 2019
swap case
@author: vincent
"""

def swap_case(s):
    tmp = ''
    #print(s,'\n');
    for i in range(len(s)):
        #print(s[i], '\n')
        if (s[i].isupper())==True:
            tmp += (s[i].lower())
        elif (s[i].islower())==True:
            tmp += (s[i].upper())
        else:
            tmp += (s[i])
    #print(tmp,'\n')
    return tmp


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)