# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 14:38:11 2019

@author: Invitado
"""

#A + 2B ---> C <---> D

import numpy as np

k1 = 0.75
k2 = 0.15
k3 = 0.025
vo = 10


def PFR(Y,V):
    
    CA = Y[0]
    CB = Y[1]
    CC = Y[2]
    CD = Y[3]
    
    r1 = k1*CA*CB**2
    r2 = k2*CC
    r3 = k3*CD
    
    dCA_dV = -r1/vo
    dCB_dV = -2*r1/vo
    dCC_dV = (r1-r2+r3)/vo
    dCD_dV = (r2-r3)/vo
    
    salida = np.array([ dCA_dV,dCB_dV,dCC_dV,dCD_dV])
    
    return salida



