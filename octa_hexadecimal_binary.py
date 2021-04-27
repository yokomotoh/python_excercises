#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 09:41:17 2019
intn octa hexadecimal binary
@author: vincent
"""

def print_formatted(number):
    # your code goes here
    for i in range(n):
        #print(i+1, ' ', end='')
        #print('{:{align}{width}}'.format(i+1, align='^', width=len(bin(n+1).lstrip("0b").rstrip("L"))), ' ', end='')
        #print(oct(i+1).lstrip("0o").rstrip("L"), ' ', end='')
        #print(hex(i+1).lstrip("0x").rstrip("L").upper(), ' ', end='')
        #print(bin(i+1).lstrip("0b").rstrip("L"))
        print('{:{align}{width}} {:{align}{width}} {:{align}{width}} {:{align}{width}}'.format(
                i+1, 
                oct(i+1).lstrip("0o"),#.rstrip("L"), 
                hex(i+1).lstrip("0x").upper(),#.rstrip("L").upper(), 
                bin(i+1).lstrip("0b"),#.rstrip("L"), 
                align='>', 
                width=len(bin(n).lstrip("0b"))))#.rstrip("L"))))
    #print(len(bin(n).lstrip("0b").rstrip("L")))
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)