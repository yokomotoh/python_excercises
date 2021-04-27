#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 16:08:01 2019
minion game
@author: yoko
"""
from collections import defaultdict 

def substring_in(str_in, score_in, string_length):
        if str_in[0] in score_in['keys']:
            #print(str_in)
#            for i in range(len(str_in),0,-1):
#                #print(str_in[0:i])
#                #score_in['words'][str_in[0:i]]=score_in['words'][str_in[0:i]]+1
#                score_in['score']+=1
            #score_in['score']+=len(str_in)
            score_in['score']+= string_length

def minion_game(string):
    # your code goes here
    consonants = "BCDFGHJKLMNPQRSTVWXYZ"
    vowels = "AEIOU"
    score1 = {'name':"Stuart",
              'keys':consonants,
              'words':defaultdict(int),
              'score':0
              }
    score2 = {'name':"Kevin",
              'keys':vowels,
              'words':defaultdict(int),
              'score':0}
    
    string_length = len(string)
    
    #print(string)
    #print(score1['keys'])
    #print(score2['keys'])
#    print("length of the string: ",len(string))
#   print("Total sum of substrings: ",sum([k for k in range(len(string)+1)]))
#    for i in range(len(string)):
    for i in range(string_length):
#        if string[i] in score1['keys']:
#            #print(string[i])
#            substring_in(string[i:],score1,string_length-i)
#        elif string[i] in score2['keys']:
#            #print(string[i])
#            substring_in(string[i:],score2,string_length-i)
        if string[i] in score1['keys']:
            score1['score']+= string_length-i
        elif string[i] in score2['keys']:
            score2['score']+= string_length-i
    
    #print(score1['name'], ":", score1['words'], score1['score'])
    #print(score2['name'], ":", score2['words'], score2['score'])
    print(score1['name'], ":", score1['score'])
#    tmp=0
#    for i in score1['words'].values():
#        tmp =tmp + i;
#    print(tmp)

    print(score2['name'], ":", score2['score'])
#    tmp=0
#    for i in score2['words'].values():
#        tmp = tmp + i;
#    print(tmp)
    
    print("sum of scores: ",score1['score']+score2['score'])
    print("missing: ",sum([k for k in range(len(string)+1)])-(score1['score']+score2['score']))
    if score1['score']>score2['score']:
        print(score1['name'], score1['score'])
    elif score1['score']<score2['score']:
        print(score2['name'], score2['score'])
    elif score1['score']==score2['score']:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)