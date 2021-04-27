#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 15:54:36 2019
String split join
@author: vincent
"""

def split_and_join(line):
    # write your code here
    tmp_split = ""
    tmp_split = line.split(" ")
    #print(tmp_split)
    tmp_join = ""
    tmp_join = "-".join(tmp_split)
    #print(tmp_join)
    return tmp_join
    
    
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)