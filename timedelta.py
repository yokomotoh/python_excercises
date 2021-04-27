#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 15:27:06 2019
numpy Time Delta
@author: yoko
"""


#import calendar
#
##print(calendar.TextCalendar(firstweekday=6).formatyear(2109))
#
#
#weekday=["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
#
#m,d,y = input().strip().split(' ')
#print(weekday[calendar.weekday(int(y),int(m),int(d))])

#import datetime
#datetime_object = datetime.datetime.now()
#print(datetime_object)
#
#from datetime import datetime
##datetime(year, month, day)
#a = datetime(2019, 11, 22)
#print(a)
## datetime(year, month, day, hour, minute, second, microsecond)
#b = datetime(2019, 11, 22, 23, 55, 59, 342380)
#print(b)
#
#c = datetime(2019, 11, 22, 8, 55, 59, 342380)
#print("year =", c.year)
#print("month =", c.month)
#print("hour =", c.hour)
#print("minute =", c.minute)
#print("timestamp =", c.timestamp())


from datetime import datetime, date
t1 = date(year = 2015, month = 5, day = 10)
t2 = date(year = 2017, month = 12, day = 23)
t3 = t1 - t2
print("t3 =", t3)
print("type of t3 =", type(t3)) 
#t4 = datetime(year = 2015, month = 5, day = 10, hour = 13 -7, minute = 54, second = 36)
t5 = datetime(year = 2015, month = 5, day = 10, hour = 13, minute = 54, second = 36)
#t6 = t4 - t5
#print("t6 =", abs(t6.total_seconds()))
#print("type of t6 =", type(t6))  
t7 = datetime(year = 2015, month = 5, day = 2, hour = 19, minute = 54, second = 36)
t8 = datetime(year = 2015, month = 5, day = 1, hour = 13, minute = 54, second = 36)
t9 = t7 - t8
print("t9 =", abs(t9.total_seconds()))
print("type of t9 =", type(t9))  
#from datetime import time
from datetime import timedelta
t10 = (-1)*timedelta(hours = 7, minutes = 0)
print("t5-t10", t5-t10)
t6= t5-(t5-t10)
print("t5-(t5-t10)=", abs(t6.total_seconds()))
t11 = (1)*timedelta(hours = 5, minutes = 30)
#t12 = timedelta(days = 4, hours = 11, minutes = 4, seconds = 54)
t13 = t7 - t11
print("t13 =", t13)
print("t8 =", t8)
t14 = t13 - t8
print("t14 =", abs(t14.total_seconds()))


import re

Weekday1=[]
Day1=[]
Month1=[]
Year1=[]
Time1=[]
TimeZone1=[]
Weekday2=[]
Day2=[]
Month2=[]
Year2=[]
Time2=[]
TimeZone2=[]
Hour1 = []
Minute1 = []
Second1=[]
Hour2 = []
Minute2 = []
Second2=[]
Delta1=[]
Delta2=[]
T = int(input())

for i in range(T):
    t1 = input()
    t2 = input()
    t11,t12,t13,t14,t15,t16 = t1.strip().split(' ')
    t21,t22,t23,t24,t25,t26 = t2.strip().split(' ')
    Weekday1.append(t11)
    Day1.append(t12)
    Month1.append(t13)
    Year1.append(t14)
    Time1.append(t15)
    TimeZone1.append(t16)
    Weekday2.append(t21)
    Day2.append(t22)
    Month2.append(t23)
    Year2.append(t24)
    Time2.append(t25)
    TimeZone2.append(t26)

for i in range(T):
    HMS1 = re.search(r"([0-9]+)(?:\:)([0-9]+)(?:\:)([0-9]+)",Time1[i])
    print(HMS1.group(1))
    Hour1.append(HMS1.group(1))
    Minute1.append(HMS1.group(2))
    Second1.append(HMS1.group(3))
    HMS2 = re.search(r"([0-9]+)(?:\:)([0-9]+)(?:\:)([0-9]+)",Time2[i])
    Hour2.append(HMS2.group(1))
    Minute2.append(HMS2.group(2))
    Second2.append(HMS2.group(3))
#    if TimeZone1[i][0]=="-":
#        Delta1[i]['plusminus']= -1
#    elif TimeZone1[i][0]=="+":
#        Delta1[i]['plusminus']= +1
#    Delta1[i]['hour']= int(TimeZone1[i][1])*10+int(TimeZone1[i][2])
#    Delta1[i]['minute'] = int(TimeZone1[i][3])*10+int(TimeZone1[i][4])
#    if TimeZone2[i][0]=="-":
#        Delta2[i]['plusminus']= -1
#    elif TimeZone2[i][0]=="+":
#        Delta2[i]['plusminus']= +1
#    Delta2[i]['hour']= int(TimeZone2[i][1])*10+int(TimeZone2[i][2])
#    Delta2[i]['minute'] = int(TimeZone2[i][3])*10+int(TimeZone2[i][4])
    if TimeZone1[i][0]=="-":
        Delta1.append({'plusminus':-1,
                       'hour':int(TimeZone1[i][1])*10+int(TimeZone1[i][2]),
                       'minute':int(TimeZone1[i][3])*10+int(TimeZone1[i][4])})
    elif TimeZone1[i][0]=="+":
        Delta1.append({'plusminus':+1,
                       'hour':int(TimeZone1[i][1])*10+int(TimeZone1[i][2]),
                       'minute':int(TimeZone1[i][3])*10+int(TimeZone1[i][4])})
    if TimeZone2[i][0]=="-":
        Delta2.append({'plusminus':-1,
                       'hour':int(TimeZone2[i][1])*10+int(TimeZone2[i][2]),
                       'minute':int(TimeZone2[i][3])*10+int(TimeZone2[i][4])})
    elif TimeZone2[i][0]=="+":
        Delta2.append({'plusminus':+1,
                       'hour':int(TimeZone2[i][1])*10+int(TimeZone2[i][2]),
                       'minute':int(TimeZone2[i][3])*10+int(TimeZone2[i][4])})
    
MonthNum={'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}


from datetime import datetime, date, timedelta
for i in range(T):
    tt1 = datetime(year = int(Year1[i]), month = MonthNum[Month1[i]], day = int(Day1[i]), hour = int(Hour1[i]), minute = int(Minute1[i]), second = int(Second1[i]))
    tt2 = datetime(year = int(Year2[i]), month = MonthNum[Month2[i]], day = int(Day2[i]), hour = int(Hour2[i]), minute = int(Minute2[i]), second = int(Second2[i]))
    tt3 = tt1 - tt2
    print("tt3 =", tt3)
    print("tt3 (total_seconds)=", abs(tt3.total_seconds()))
    print("type of tt3 =", type(tt3))
    tt1delta=Delta1[i]['plusminus']*timedelta(hours = Delta1[i]['hour'], minutes = Delta1[i]['minute'])
    tt2delta=Delta2[i]['plusminus']*timedelta(hours = Delta2[i]['hour'], minutes = Delta2[i]['minute'])
    print("tt1-tt1delta =", tt1-tt1delta)
    print("tt2-tt2delta =", tt2-tt2delta)
    DD = (tt1-tt1delta) - (tt2-tt2delta)
    print("delta tt1 tt2 =",abs(DD.total_seconds()))
    
#t4 = datetime(year = 2015, month = 5, day = 10, hour = 13 -7, minute = 54, second = 36)
t5 = datetime(year = 2015, month = 5, day = 10, hour = 13, minute = 54, second = 36)
#t6 = t4 - t5
#print("t6 =", abs(t6.total_seconds()))
#print("type of t6 =", type(t6))  
t7 = datetime(year = 2015, month = 5, day = 2, hour = 19, minute = 54, second = 36)
t8 = datetime(year = 2015, month = 5, day = 1, hour = 13, minute = 54, second = 36)
t9 = t7 - t8
print("t9 =", abs(t9.total_seconds()))
print("type of t9 =", type(t9))  
#from datetime import time
from datetime import timedelta
t10 = (-1)*timedelta(hours = 7, minutes = 0)
print("t5-t10", t5-t10)
t6= t5-(t5-t10)
print("t5-(t5-t10)=", abs(t6.total_seconds()))
t11 = (1)*timedelta(hours = 5, minutes = 30)
#t12 = timedelta(days = 4, hours = 11, minutes = 4, seconds = 54)
t13 = t7 - t11
print("t13 =", t13)
print("t8 =", t8)
t14 = t13 - t8
print("t14 =", abs(t14.total_seconds()))
