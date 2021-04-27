#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 15:24:31 2019
test
@author: yoko
"""
from collections import defaultdict 
  
class Graph(): 
    def __init__(self,vertices): 
        self.graph = defaultdict(list) 
        self.V = vertices 
  
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
        #self.graph[u].add(v) 
  
    def isCyclicUtil(self, v, visited, recStack): 
  
        # Mark current node as visited and  
        # adds to recursion stack 
        visited[v] = True
        recStack[v] = True
  
        # Recur for all neighbours 
        # if any neighbour is visited and in  
        # recStack then graph is cyclic 
        for neighbour in self.graph[v]: 
            print("neighbour: ",neighbour)
            if visited[neighbour] == False: 
                print('visited: %s recStack: %s \n' %(visited,recStack))
                if self.isCyclicUtil(neighbour, visited, recStack) == True: 
                    print('neighbour "%d" has a circle' %neighbour)
                    return True
            elif recStack[neighbour] == True:
                print('neighbour "%d" has a circle' %neighbour)
                print('visited: %s recStack: %s \n' %(visited,recStack))
                return True
  
        # The node needs to be poped from  
        # recursion stack before function ends 
        recStack[v] = False
        return False
  
    # Returns true if graph is cyclic else false 
    
    def isCyclic(self, tmp): 
        #for i in self.V:
        visited=defaultdict(list) 
        recStack=defaultdict(list) 
        for i in tmp:
            visited.append(i,False)
            recStack.append(i,False)
        #visited = [False] * self.V 
        print(visited)
        
        #recStack = [False] * self.V
        print(recStack)
        #for node in range(self.V): 
        for node in self:
            if visited[node] == False:
                #print('visited: %s recStack: %s \n' %(visited,recStack))
                if self.isCyclicUtil(node,visited,recStack) == True:
                    print('node "%d" has a circle' %node)
                    return True
        return False

#######

#N = int(input())
#    
#input_list = []
#n = N
#tmp = []
#for i in range(n):
#    arr = list(map(str, input().split()))
#    tmp.append(arr)

n = 8
tmp = [['DEPEND', 'A', 'B', 'C'], ['DEPEND', 'C', 'A'], ['DEPEND', 'B', 'D'], ['INSTALL', 'A'], ['INSTALL', 'B'], ['REMOVE', 'C'], ['LIST'], ['END']]



print(tmp)
  
items=[]
for i in range(n):
    if(tmp[i][0]=='DEPEND' or tmp[i][0]=='INSTALL'):
        for j in range(1,len(tmp[i])):
            items.append(tmp[i][j])
            
set_items=list(dict.fromkeys(items))
print(set_items)




g = Graph(len(set_items))

for i in range(n):
    if (tmp[i][0]=='DEPEND'):
        print(tmp[i])
        for j in range(2,len(tmp[i])):
            g.addEdge(tmp[i][1],tmp[i][j])

print(g.graph)




#if g.isCyclic(tmp) ==1:
#    print("has a cycle")
#else:
#    print("no cycle")


installed_item=[]
def install_item(item):
    print('Installing ', item)
    installed_item.append(item)

def remove_item(item):
    print('Removing ', item)

def list_installed_item(item_list):
    for i in item_list:
        print(i)

for i in range(n):
    if(tmp[i][0]=="INSTALL"):
        #print('installing')
        install_item(tmp[i][1])
        #print(g.graph[tmp[i][1]])
        for j in g.graph[tmp[i][1]]:
            install_item(j)
    elif(tmp[i][0]=="REMOVE"):
        remove_item(tmp[i][1])
        for j in g.graph[tmp[i][1]]:
            remove_item(j)
    elif(tmp[i][0]=="LIST"):
        list_installed_item(installed_item)
    elif(tmp[i][0]=="END"):
        break       
