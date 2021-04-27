#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 16:21:59 2019
Detect Cycle in a Directed Graph
@author: yoko
"""

# Python program to detect cycle  
# in a graph 
  
from collections import defaultdict 
  
class Graph(): 
    def __init__(self,vertices): 
        self.graph = defaultdict(list) 
        self.V = vertices 
  
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
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
                    return True
            elif recStack[neighbour] == True:
                print('visited: %s recStack: %s \n' %(visited,recStack))
                return True
  
        # The node needs to be poped from  
        # recursion stack before function ends 
        recStack[v] = False
        return False
  
    # Returns true if graph is cyclic else false 
    def isCyclic(self): 
        visited = [False] * self.V 
        #print(visited)
        recStack = [False] * self.V
        #print(recStack)
        for node in range(self.V): 
            if visited[node] == False:
                print('visited: %s recStack: %s \n' %(visited,recStack))
                if self.isCyclicUtil(node,visited,recStack) == True:
                
                    return True
        return False
  
#g = Graph(4) 
#g.addEdge(0, 1) 
#g.addEdge(0, 2) 
#g.addEdge(1, 2) 
#g.addEdge(2, 0) 
#g.addEdge(2, 3) 
#g.addEdge(3, 3) 
#
#print(g.graph)
#
#if g.isCyclic() == 1: 
#    print("Graph has a cycle")
#else: 
#    print("Graph has no cycle")
#  

h = Graph(4)
h.addEdge(0, 1)
h.addEdge(1, 2)
h.addEdge(2, 0)
h.addEdge(1, 0)
print(h.graph)
if h.isCyclic() ==1:
    print("has a cycle")
else:
    print("no cycle")