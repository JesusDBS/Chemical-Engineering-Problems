# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 11:33:50 2019

@author: Invitado
"""

import numpy as np
import fun_ejercicio_3 as f #Importa la función

vo = 0.6219 #m^3/Kg
vf = 0.02856 #m^3/Kg

fun = lambda v: f.RK(v) #Llama a la ecuación RK como una función anónima

vint = np.linspace(vo,vf,100) #Intervalo de integración

W = np.trapz(fun(vint),vint) #Calcula el trabajo
print('El trabajo necesario para la compresión es %.2f KJ' %W) 
                                                                