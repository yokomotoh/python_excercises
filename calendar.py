#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 15:27:06 2019
numpy calendar
@author: yoko
"""


import calendar

#print(calendar.TextCalendar(firstweekday=6).formatyear(2109))


weekday=["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]

m,d,y = input().strip().split(' ')
print(weekday[calendar.weekday(int(y),int(m),int(d))])

