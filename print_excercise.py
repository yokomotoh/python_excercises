#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 22:05:55 2019
excercise
@author: yoko
"""

#n = int(input())
#
#for i in range(n):
#    print(i+1, end='')
#    
"""
"""
    
    
n = int(input())
arr = map(int, input().split())
x=[]
score = defaultdict(int) 
for s in arr:
    score[s] += 1
    x.append(s)

#print(score)
#print(x)
x.sort(reverse=True)
#print(x)

no1= x[0]
for i in range(len(x)):
    if x[i]<no1:
        print(x[i])
        break

"""
"""
def sortSecond(val): 
    return val[1]  

def sortFirst(val):
    return val[0]

python_student = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    python_student.append([name, score])

print(python_student)
python_student.sort(key = sortSecond)
print(python_student)
nolast = python_student[0][1]
for i in range(len(python_student)):
    if python_student[i][1]>nolast:
        nosecond=python_student[i][1]
        break

python_student.sort(key = sortFirst)
print(python_student)
for i in range(len(python_student)):
    if python_student[i][1]==nosecond:
        print(python_student[i][0])


"""
"""

n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

sum_elm = 0.0
for elm in student_marks[query_name]:
    sum_elm += elm

#print(sum_elm/3)
print("%.2f" % round(sum_elm/3, 3))

"""
"""

for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    #print('case: %d' %i)
    #print([str(i) for i in (list(range(1,i+1))+list(range(i-1,0,-1)))])
    #print(int("".join([str(i) for i in (list(range(1,i+1))+list(range(i-1,0,-1)))])))
    #print((list(range(1,i+1))+list(range(i-1,0,-1))))
    #for j in (list(range(1,i+1))+list(range(i-1,0,-1))+['\n']): print(j,end="")
    ##l=list(range(1,i+1))+list(range(i-1,0,-1)); print(*l,sep="")
    from functools import reduce; print(reduce(lambda x,y: 10*x+y, (list(range(1,i+1))+list(range(i-1,0,-1)))))
"""
"""

statesAndCapitals = { 
                     'Gujarat' : 'Gandhinagar', 
                     'Maharashtra' : 'Mumbai', 
                     'Rajasthan' : 'Jaipur', 
                     'Bihar' : 'Patna'
                    } 
                      
print('List Of given states:\n') 
  
# Iterating over keys 
for state in statesAndCapitals: 
    print(state) 

for capital in statesAndCapitals.values():
    print(capital)

for state, capital in statesAndCapitals.items():
    print(state, " : ", capital)

print(statesAndCapitals['Rajasthan'])

for state in statesAndCapitals:
    if statesAndCapitals[state]=='Patna':
        print(state)
        
for state, capital in statesAndCapitals.items():
    if capital =='Patna': print(state)
        

"""
"""

n = int(input())
arr = list(map(str, input().split()))
k = int(input())

#from itertools import compress, product
#
#def combinations(items):
#    return ( set(compress(items,mask)) for mask in product(*[[0,1]]*len(items)) )
#
#list(tuple(combinations(range(4))))

tmp_arr = arr.copy()

from itertools import combinations 
  
# Get all combinations of [1, 2, 3, 4] 
# and length 2 
seed = []
for i in range(n):
    seed.append(i+1)
    
#print(seed)
    
comb = combinations(seed, k) 
  
# Print the obtained combinations 
#for i in list(comb): 
#    print(i) 

tmp = list(comb)
#print(len(tmp))

cont_a=0
for i in tmp:
    for j in range(k):
        #print(i)
        #print(j)
        #print(i[j])
        if tmp_arr[i[j]-1]=='a':
            cont_a = cont_a +1
            break

#print(cont_a)
#print(tmp)
print("%.4f" % (cont_a/len(tmp)))
            
"""
"""

if __name__ == '__main__':
    N = int(input())
    
    input_list = []
    n = N
    tmp = []
    for i in range(n):
        arr = list(map(str, input().split()))
        tmp.append(arr)
        
    for i in range(n):
        if(tmp[i][0]=="insert"):
                    input_list.insert(int(tmp[i][1]), int(tmp[i][2]))
        elif(tmp[i][0]=="print"):
                    print(input_list)
        elif(tmp[i][0]=="remove"):
                    input_list.remove(int(tmp[i][1]))
        elif(tmp[i][0]=="append"):
                    input_list.append(int(tmp[i][1]))
        elif(tmp[i][0]=="sort"):
                    input_list.sort()
        elif(tmp[i][0]=="pop"):
                    input_list.pop()
        elif(tmp[i][0]=="reverse"):
                    input_list.reverse()
        

"""
"""

def findNumber(arr, k):
    print(arr)
    for i in range(len(arr)):
        if arr[i]==k:
            return "YES"
        else:
            return "NO"

if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    k = int(input().strip())

    res = findNumber(arr, k)

    print(res)
 #   fptr.write(res + '\n')

"""
"""

def oddNumbers(l, r):
    tmp = []
    for i in range(l,r+1):
        #print(i)
        if i%2==1:
            tmp.append(i)
            #print(tmp)
    return tmp

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    r = int(input().strip())

    res = oddNumbers(l, r)

    print(res)
    #fptr.write('\n'.join(map(str, res)))
    #fptr.write('\n')

    #fptr.close()


"""
"""

arr_count = int(input().strip())

arr = []

for _ in range(arr_count):
    arr_item = str(input().strip())
    arr.append(arr_item)
        
print(arr)
"""
"""

N = int(input())
    
input_list = []
n = N
tmp = []
for i in range(n):
    arr = list(map(str, input().split()))
    tmp.append(arr)

print(tmp)

for i in range(n):
    if(tmp[i][0]=="DEPEND"):
                    input_list.insert(int(tmp[i][1]), int(tmp[i][2]))
        elif(tmp[i][0]=="INSTALL"):
                    print(input_list)
        elif(tmp[i][0]=="remove"):
                    input_list.remove(int(tmp[i][1]))
        elif(tmp[i][0]=="append"):
                    input_list.append(int(tmp[i][1]))
        elif(tmp[i][0]=="sort"):
                    input_list.sort()
        elif(tmp[i][0]=="pop"):
                    input_list.pop()
        elif(tmp[i][0]=="reverse"):
                    input_list.reverse()
        
