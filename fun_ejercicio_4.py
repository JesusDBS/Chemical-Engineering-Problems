# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 12:33:54 2019

@author: Invitado
"""
import numpy as np
import math

#Temperaturas en grados centígrados y Presiones en Kilopascales
#T2 y P2 corresponden al punto triple 
#T3 y P3 corresponden al punto crítico

T1 = -0.95 #Temperatura de ebullición normal
T2 = -139.15
P2 = 0.0007 
T3 = 151.85 
P3 = 3796

Pop = 1.88 #Mpa

def Calor_Latente(Y):
    
    A = Y[0]
    B = Y[1]
    C = Y[2]
    Tsat = Y[3]
    
    fun_1 = A*(T1+C)-B- math.log(101.325)*(T1+C)
    fun_2 = A*(T2+C)-B- math.log(P2)*(T2+C)
    fun_3 = A*(T3+C)-B- math.log(P3)*(T3+C)
    fun_4 = A*(Tsat+C)-B- math.log(Pop*1000)*(Tsat+C)
    
    sol = np.array([fun_1,fun_2,fun_3,fun_4])
    
    return sol












