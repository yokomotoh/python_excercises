#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 19:07:41 2019
Re.start() & Re.end()
@author: vincent
"""

str_input=input()
sub_str_input=input()

import re
#x=re.findall(r'[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]([AEIOUaeiou][AEIOUaeiou]+)[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]', str_input)
#x=re.findall(sub_str_input, str_input)
#y=list(map(lambda x: x.group(),re.finditer(r'(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])([AEIOUaeiou][AEIOUaeiou]+)(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])',str_input)))
#y=list(map(lambda x: x.group(),re.finditer(sub_str_input, str_input)))


def search_substring(str1, str2, start_str2):
    #if len(str1)<=len(str2)-start_str2:
        tmp1= re.search(str1, str2[start_str2:])
        if tmp1==None:
            return(-1, -1)
        else:
#        elif start_str2 >= tmp1.start()+start_str2:
            #print(start_str2)
            #print(tmp1.start(),tmp1.end())
            #print("(%d, %d)" %(tmp1.start()+start_str2, tmp1.end()+start_str2))
            return((tmp1.start()+start_str2, tmp1.end()+start_str2-1))
            #search_substring(str1,str2,tmp1.start()+1)

#for i in x:
#    print(i)
#if len(x)==0:
#    print('-1')
#print(x.start(),x.end())

def tuple_small(tuple1,tuple2):
    for i1 in tuple1:
        for i2 in tuple2:
            if i1<i2:
                pass
            else:
                return False
    return True

tmp=(-2, -2)
for i in range(len(str_input)-len(sub_str_input)):
    tmp2=search_substring(sub_str_input, str_input, i)
    if tmp<tmp2:
        print(tmp2)
        tmp=tmp2
    

#for i in y:
#    print(i)
#if len(y)==0:
#    print('-1')