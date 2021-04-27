#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 08:47:39 2019
merge the tools
@author: yoko
"""

def merge_the_tools(string, k):
    # your code goes here
    seg=len(string)//k
    subsegment = []

#   #expression of set(non ordered) -->false
#    for i in range(seg):
#        subsegment.append(set())
#        for j in range(k):
#            subsegment[i].add(string[i*k+j])
#    for k in subsegment:
#        for l in k:
#            print(l, end='')
#        print('')
    
    for i in range(seg):
        subsegment.append([string[i*k+0]])
        for j in range(1,k):
            if string[i*k+j] in set(subsegment[i]):
                pass
                #print("string[i*k+j]= ", string[i*k+j])
            else:
                subsegment[i].append(string[i*k+j])
            #print(subsegment)
    #print(subsegment)
    for k in subsegment:
        for l in k:
            print(l, end='')
        print('')
        
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)