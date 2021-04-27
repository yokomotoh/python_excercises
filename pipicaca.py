#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 17:32:12 2020

@author: vincent
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sc

#Valeurs experimentales
I=np.array ([0.0250, 0.050, 0.075, 0.100, 0.125, 0.150])
U=np.array([1.48, 1.46, 1.43, 1.41, 1.38, 1.35])

#Representation d'un nuage de points
plt.plot(I,U,'o',color='green')

#Modelisation du graphique
droite=sc.linregress(I,U)
coefficient=droite.slope
print("Coefficient directeur :", coefficient)
oorigine=droite.intercept
print("Ordonnee a l'origine :",oorigine)
