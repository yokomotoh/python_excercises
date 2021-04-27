#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 14:28:07 2019
re.split()
@author: yoko
"""

regex_pattern = r'\W+'	# Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))
#print(re.split(regex_pattern, input()))

# =============================================================================
# str_list=re.split(regex_pattern, input())
# tmp=''
# for i in str_list:
#     if(i!=',' and i!='.' and i!=''):
#         tmp=tmp+i
#     else:
#         print(tmp)
#         tmp=''
# =============================================================================
