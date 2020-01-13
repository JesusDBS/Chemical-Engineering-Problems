# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 14:49:58 2019

@author: Invitado
"""
import numpy as np
from scipy.integrate import odeint
import fun_ejercicio_6 as f
import matplotlib.pyplot as plt

CAo = 1.15#mol/L
CBo = 0.9#mol/L
V = 100 #Lts

fun = lambda Y,t: f.PFR(Y,V)
P = np.linspace(0,V,100) #Intervalo de integración
y = np.array([1.15,0.9,0,0])
sol = odeint(fun,y,P)

CA = sol[0:sol.size-1,0]
CB = sol[0:sol.size-1,1]
CC = sol[0:sol.size-1,2]
CD = sol[0:sol.size-1,3]

plt.plot(CA,'y',label='CA')
plt.plot(CB,'b',label='CB')
plt.plot(CC,'r',label='CC')
plt.plot(CD,'g',label='CD')
plt.title('Perfil de concentraciones')
plt.xlabel('Volumen(L)')
plt.ylabel('Concentraciones (mol/L)')
plt.legend()
plt.show()

