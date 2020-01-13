# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 16:00:16 2019

@author: Invitado
"""
import numpy as np
from scipy.integrate import odeint
import pylab as plt

#Propiedades de la esfera
ro = 19840 #Kg/m^3
Cp = 130 #J/kg*K
e = 0.8 #emisividad
tao = 5.67E-8 #W/m^2*K^4
r = 0.05 #m
V = 5.23599E-4 #m^3
Asup = 3.14159E-2 #Área superficial m^2
q = 2000 #W

#Propiedades del aire
hc = 30 #W/m^2*K
Tinf = 300 #K

To = 350#K
Tf = 641 + 273.15 #Temperatura de fusión de la esfera

def fun(T,t):
    
    dT_dt = (1/(ro*Cp*V))*(q-e*tao*Asup*(T**4 - Tinf**4) - hc*Asup*(T-Tinf))
    
    return dT_dt

P = np.linspace(0,1000,100)
sol = odeint(fun,To,P)
plt.plot(P,sol,label='Temperatura de la esfera') 
plt.plot(P,np.linspace(1,1,100)*Tf,label='Temperatura de fusión')
plt.legend()
plt.xlabel('Tiempo (segundos)')
plt.ylabel('Temperatura (K)')
plt.title('Temperatura de la esfera')
plt.show()

print('La esfera alcanza su temperatura de fusión a partir de los 600 segundos')





