#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 11:49:37 2019
text wrap
@author: yoko
"""

import textwrap

def wrap(string, max_width):
    
    wrapper = textwrap.TextWrapper(width=max_width) 
  
    #word_list = wrapper.wrap(text=string) 
    word_list = wrapper.fill(text=string)       
    return word_list

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
    #print(*result, sep = "\n") 
    
#    # Print each line. 
#    for element in result: 
#        print(element) 