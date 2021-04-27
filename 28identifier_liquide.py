#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 19 16:18:19 2020

@author: romain
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sc

i=np.array([15, 25, 35, 45, 55]) # i (en degree)
r=np.array([10, 17, 23, 29, 34]) # r (en degree)

sin_i = np.sin(np.deg2rad(i))
sin_r = np.sin(np.deg2rad(r))
print("sin(i): ",sin_i)
print("sin(r): ",sin_r)

plt.plot(sin_r,sin_i,'+',color='blue')

droite=sc.linregress(sin_r,sin_i)
coefficient=droite.slope
print("Coefficient directeur :", coefficient)
oorigine=droite.intercept
print("Ordommee a l'originr :", oorigine)

Umodele=coefficient*sin_r+oorigine
plt.plot(sin_r,Umodele,color='red')

plt.xlabel("sin(r) ")
plt.ylabel("sin(i) ")
plt.title("sin(i) = f(sin(r))")
plt.grid()

plt.show()