#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 16:24:02 2019
Mutations
@author: vincent
"""

def mutate_string(string, position, character):

    l = list(string)
    l[position] = character
    string = ''.join(l)
    return string



if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)