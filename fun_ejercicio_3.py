# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 11:34:40 2019

@author: Invitado
"""
import math

Tc = 374.1 #K
Pc = 4060 #KPa
R = 0.08149 #KJ/Kg*K
T = 383 #K

def RK(v): #Ecuación de Rendlich-Knwon
    
    a = 0.4278*(R**2*T**2.5/Pc)
    b = 0.08664*(R*Tc/Pc)
    
    P = (R*T/(v-b))-(a/(v*(v+b)*math.sqrt(T))) #Forma explícita en P
    
    return P