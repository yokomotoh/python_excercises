#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 12:03:52 2019
alphabet rangoli
@author: yoko
"""

size = 0

alphabet="abcdefghijklmnopqrstuvwxyz"

#def print_core(num_line, size):
#    for i in range(0,num_line+1,1):
#        print_alphabet(i, size - i)

def print_alphabet(num_line, size):
    for k in range(num_line):
        print("%s-" %alphabet[size-1-k], end='')
    for l in range(num_line,0,-1):
        print("%s-" %alphabet[size-1-l], end='')
    print(alphabet[size-1], end='')


def print_rangoli(size):
    # your code goes here

    for j in range(size):
        print('--'*(size-j-1),end='')
        print_alphabet(j,size)
        print('--'*(size-j-1))
    for j in range(size-1,0,-1):
        print('--'*(size-j),end='')
        print_alphabet(j-1,size)
        print('--'*(size-j))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)