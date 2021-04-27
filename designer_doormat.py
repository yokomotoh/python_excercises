#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 09:05:17 2019
Designer door mat
@author: yoko
"""

if __name__ == '__main__':
 
    n, m = input().split()
    N, M = int(n), int(m)    
    mid = 3
    for i in range(0,(N-1)//2):
        j = (M-mid*(i*2+1))//2
        #for j in range(0,(M-(i+1))/2):
        print('-'*j, end='')
        print('.|.'*(i*2+1), end='')
        print('-'*j)
    k = (M-7)//2
    print('-'*k, end='')
    print('WELCOME', end='')
    print('-'*k)
    for i in range((N-1)//2, 0, -1):
        j = (M-mid*((i-1)*2+1))//2
        #for j in range(0,(M-(i+1))/2):
        print('-'*j, end='')
        print('.|.'*((i-1)*2+1), end='')
        print('-'*j)