# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 14:04:10 2019

@author: Invitado
"""

import numpy as np
from scipy.optimize import broyden1
import fun_ejercicio_4 as f

R = 8.314 #J/mol*K
PM = 58.123 #g/mol

fun = lambda Y: f.Calor_Latente(Y)
semilla = np.array([12,2000,300,200]) 
sol = broyden1(fun,semilla)

print('La temperatura de saturación es %.2f K' %(sol[3] + 273.15))

B = sol[1]
C = sol[2]
T = sol[3] + + 273.15 #K

Dh_Vap = (B*R*T**2)/(T+C)**2

print('El calor suministrado es %.2f J/g' %(Dh_Vap/PM))