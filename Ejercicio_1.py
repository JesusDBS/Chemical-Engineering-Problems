# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 10:07:45 2019

@author: Invitado
"""

#Método de resolución número 1
import sympy

m1,m2,m3 = sympy.symbols('m1 m2 m3') #Convierte las variables en simbólicas

#Balances de masa
eq1 = 0.9*m1 + 0.3*m2 + 0.1*m3 - 30
eq2 = 0.1*m1 + 0.5*m2 + 0.2*m3 -25
eq3 = 0.2*m2 + 0.7*m3 - 10

sol = sympy.solve([eq1,eq2,eq3],[m1,m2,m3]) #Resuelve el sistema
print('La solución por el método 1 es:',sol)

#Método de resolución número 2
import numpy as np
import numpy.linalg as nl

A = np.array([[0.9,0.3,0.1],[0.1,0.5,0.2],[0,0.2, 0.7]]) #Matriz de coeficientes
f = np.array([30,25,10])
sol = nl.solve(A,f)
print('La solución por el método 2 es: ',sol)

#Método de resolución número 3
def BalanceDeMasa(Y): #Definir los balances de masa
    m1 = Y[0]
    m2 = Y[1]
    m3 = Y[2]
    
    eq1 = 0.9*m1 + 0.3*m2 + 0.1*m3 - 30
    eq2 = 0.1*m1 + 0.5*m2 + 0.2*m3 -25
    eq3 = 0.2*m2 + 0.7*m3 - 10
        
    sol = np.array([eq1,eq2,eq3])
    
    return sol

from scipy.optimize import broyden1

semilla = np.array([0.1,0.1,0.1])
respuesta = broyden1(BalanceDeMasa,semilla)
print('La solución por el método 3 es:',respuesta)

#Método de resolución número 4
from scipy.optimize import fsolve

fun = lambda Y: BalanceDeMasa(Y) #Función anónima 
respuesta = fsolve(fun,semilla)
print('La solución por el método 4 es:', respuesta)

#Método de resolución número 5
from scipy.optimize import newton_krylov as nk

respuesta = nk(BalanceDeMasa,semilla)
print('La solución por el método 5 es:', respuesta)











    
    
    
    