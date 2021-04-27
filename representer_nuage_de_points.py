#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 19 16:18:19 2020

@author: romain
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sc

S=np.array([0, 40.0, 80.0, 120, 160]) # S (en g/L)
n=np.array([1.32, 1.35, 1.38, 1.41, 1.44]) # n (sans unite)

plt.plot(S,n,'+',color='blue')

droite=sc.linregress(S,n)
coefficient=droite.slope
print("Coefficient directeur :", coefficient)
oorigine=droite.intercept
print("Ordommee a l'originr :", oorigine)

Umodele=coefficient*S+oorigine
plt.plot(S,Umodele,color='red')

plt.xlabel("S (en g/L)")
plt.ylabel("n (sans unite)")
plt.title("n = f(S)")
plt.grid()

plt.show()