#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 17:43:04 2019

@author: vincent
"""



if __name__ == '__main__':
    s = input()
    #print(s)
    truefalse = False
    for i in range(len(s)):
        if s[i].isalnum()==True:
            truefalse = True
            #print('True')
            break
        else:
            pass
    print(truefalse)
    #print(s)
    truefalse = False
    for i in range(len(s)):
        if s[i].isalpha()==True:
            truefalse = True
            #print('True')
            break
        else:
            pass
    print(truefalse)
    #print(s)
    truefalse = False
    for i in range(len(s)):
        if s[i].isdigit()==True:
            truefalse = True
            #print('True')
            break
        else:
            pass
    print(truefalse)
    #print(s)
    truefalse = False
    for i in range(len(s)):
        if s[i].islower()==True:
            truefalse = True
            #print('True')
            break
        else:
            pass
    print(truefalse)
    #print(s)
    truefalse = False
    for i in range(len(s)):
        if s[i].isupper()==True:
            truefalse = True
            #print('True')
            break
        else:
            pass
    print(truefalse)   
