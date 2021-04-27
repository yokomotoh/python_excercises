#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 11:51:07 2019
Validating Roman Numerals
@author: yoko
"""

regex_pattern = r'^(M{0,3}(CM){0,1}(C{0,1}D{0,1}|(?<!CD)D{0,1}C{0,3})(XC){0,1}(X{0,1}L{0,1}|(?<!XL)L{0,1}X{0,3})(IX){0,1}(I{0,1}V{0,1}|(?<!IV)(V{0,1}I{0,3})))$'	# Do not delete 'r'.
#roman_char={'I':1,
#            'V':5,
#            'X':10,
#            'L':50,
#            'C':100,
#            'D':500,
#            'M':1000}

import re
print(str(bool(re.match(regex_pattern, input()))))