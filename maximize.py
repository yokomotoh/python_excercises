#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 14:55:21 2019
Maximize It
@author: yoko
"""
def func(x):
    return x**2


# =============================================================================
# K=6
# M=767
# input_list=[[2, 488512261, 423332742],
# [2, 625040505, 443232774],
# [1, 4553600],
# [4, 92134264, 617699202, 124100179, 337650738],
# [2, 778493847, 932097163],
# [5, 489894997, 496724555, 693361712, 935903331, 518538304]]
# =============================================================================
 
# =============================================================================
# K=7 
# M=952
# input_list=[[6, 386364143, 56297585, 479292050, 782778989, 177771725, 945191156],
# [7, 458982242, 957774948, 25202756, 357554307, 248513713, 506622954, 769577156],
# [3, 109432676, 494972174, 914814315],
# [1, 49979276],
# [2, 491584479, 103564062],
# [1, 25883738],
# [1, 460971693]]
# =============================================================================




k, m = input().split()
K = int(k)
M = int(m)
  
input_list = []
# N=[]
# for i in range(K):
#     input_list.append(list(map(int, input().split())))
#     N.append(len(input_list[i]))
# 
# =============================================================================

N=[]
for i in range(K):
    input_list.append(list(map(int, input().split())))
    N.append(input_list[i][0])
    input_list[i].pop(0)

#for i in range(K):
#     N.append(len(input_list[i]))

#from itertools import combinations
#from itertools import combinations_with_replacement

#tmp1, tmp2 = input().split()
#string = tmp1
#k = int(tmp2)

combination_N = []
for i in range(K):
    tmp_list=[]
    for j in range(N[i]):
        tmp_list.append(j)
    combination_N.append(tmp_list)

#print(combination_N)

def make_combination_N(list_sub,list_sub_rest):
    #print(list_sub)
    #print(list_sub_rest)
    tmp=[]
    for i in range(len(list_sub)):
        for j in range(len(list_sub_rest)):
            #print(i, j)
            #print(list_sub[i], list_sub_rest[j])
            tmp.append(list_sub[i]+[list_sub_rest[j]])
            
        #print(tmp)
    return tmp

list_tmp=[]
list_tmp=make_combination_N([[]],combination_N[0])
#print(list_tmp)
for i in range(1,K):
    list_tmp=make_combination_N(list_tmp,combination_N[i])
    #print(list_tmp)
#print(list_tmp)


def key_to_value(key,value_list):
    return value_list[key]

def key_list_to_value(key_list,value_list):
    tmp=[]
    for i in range(len(key_list)):
        #print(key_list[i], key_to_value(key_list[i],value_list[i]))
        tmp.append(key_to_value(key_list[i],value_list[i]))
    #print(tmp)
    return tmp

fx=[]
result_tmp_max = 0
for i in range(len(list_tmp)):
    sum_tmp=0
    #print(list_tmp[i],input_list)
    result_tmp=0
    x=key_list_to_value(list_tmp[i],input_list)
    for j in range(K):
            sum_tmp=sum_tmp + func(x[j])
    result_tmp = sum_tmp % M
    if result_tmp_max < result_tmp:
        result_tmp_max=result_tmp
        #print(i, " : ", x)
        #print(sum_tmp)
        #print(result_tmp)
    fx.append( sum_tmp % M)
#print(max(fx))
print(result_tmp_max)
#print(fx.index(max(fx)))

#for i in range(len(list_tmp)):
#    if fx[i]>=943:
#        print(i," : ",list_tmp[i], fx[i])