#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 16:14:07 2020

@author: yoko
"""
n = 8
tmp = [['DEPEND', 'A', 'B', 'C'], ['DEPEND', 'C', 'A'], ['DEPEND', 'B', 'D'], ['INSTALL', 'A'], ['INSTALL', 'B'], ['REMOVE', 'C'], ['LIST'], ['END']]

#######

#N = int(input())
#    
#input_list = []
#n = N
#tmp = []
#for i in range(n):
#    arr = list(map(str, input().split()))
#    tmp.append(arr)


print(tmp)
  
items=[]
for i in range(n):
    if(tmp[i][0]=='DEPEND' or tmp[i][0]=='INSTALL'):
        for j in range(1,len(tmp[i])):
            items.append(tmp[i][j])
            
set_items=list(dict.fromkeys(items))
print(set_items)

dict_items={}
for k in range(len(set_items)):
    dict_items[set_items[k]]={'Installed':False,'Depend':[]}

Installed_item=[]
def Do_Install(name_item):
    print('Install: ', name_item, ':Installed: ', dict_items[name_item]['Installed'])
    if dict_items[name_item]['Installed']==False:
        Installed_item.append(name_item)
        dict_items[name_item]['Installed']=True
        for m in range(len(dict_items[name_item]['Depend'])):
            Do_Install(dict_items[name_item]['Depend'][m])
#        for l in range(len(set_items)):
#            for m in range(len(dict_items[set_items[l]]['Depend'])):
#                Do_Install(dict_items[set_items[l]]['Depend'][m])
    return Installed_item

def Remove_Install(name_item):
    print('Remove: ', name_item, ':Installed: ', dict_items[name_item]['Installed'])
    if dict_items[name_item]['Installed']==True:
        dict_items[name_item]['Installed']=False
        if name_item in Installed_item:
            Installed_item.remove(name_item)
        for p in range(len(set_items)):
            for o in range(len(dict_items[set_items[p]]['Depend'])):
                if dict_items[set_items[p]]['Depend'][o]==name_item:
                    Remove_Install(set_items[p])
    return Installed_item



for i in range(n):
    if(tmp[i][0]=='DEPEND'):
        for l in range(2,len(tmp[i])):
                dict_items[tmp[i][1]]['Depend'].append(tmp[i][l])
    elif(tmp[i][0]=='INSTALL'):
        print(Do_Install(tmp[i][1]))
    elif(tmp[i][0]=='REMOVE'):
        print(Remove_Install(tmp[i][1]))
    elif(tmp[i][0]=='LIST'):
        print(Installed_item)
    elif(tmp[i][0]=='END'):
        print('END')
        
        
        

