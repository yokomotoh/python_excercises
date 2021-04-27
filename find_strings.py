#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 16:33:26 2019
find a string
@author: yoko
"""

def same_strings(string1, string2):
    #print("%s : %s" %(string1, string2))
    for j in range(len(string2)):
        if string1[j]!=string2[j]:
            #print("%s <> %s" %(string1[j],string2[j]))
            return False
            break
    return True    
    

def count_substring(string, sub_string):
    cnt = 0
    tmp = len(sub_string)    
    for i in range(len(string)-tmp+1):
        if same_strings(string[i:i+tmp],sub_string)==True:
            #print('true')
            cnt=cnt+1
            #print(cnt)
    return cnt

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)