# -*- coding: utf-8 -*-
"""
Created on Thu May  9 15:51:48 2019

@author: Invitado
"""

import numpy as np
import numpy.linalg as nl
import pylab
import math

t = np.array([0,20,60,90,128,180,300,420])

Ca = np.array([0.225,0.1898,0.1323,0.1158,0.0967,0.0752,0.0478,0.0305])

rA = -np.diff(Ca)/np.diff(t) #Ecuentra -dCA/dt = -rA = k'*CA^n

ln_CA = np.log(Ca[1:Ca.size])
ln_rA = np.log(rA)

#Regresión lineal
n=ln_CA.size
x = ln_CA 
y = ln_rA
Xsum = np.sum(x)
Ysum = np.sum(y)
XYsum = np.sum(np.dot(x,y))
X2sum = np.sum(np.dot(x,x))
A = np.array([[n, Xsum], [Xsum, X2sum]])
f = np.array([Ysum, XYsum])
c = nl.solve(A, f) #Resuelve el sistema
yLR = c[0] + c[1]*x

yprom = np.mean(y)
num = np.sum((yLR-yprom)**2)
den = np.sum((y-yprom)**2)
r2 = num/den

#Grafica Ln(-rA) = lnk' + nLnCA
pylab.plot(x,y,'o',x,yLR)
pylab.xlabel('lnCA')
pylab.ylabel('ln(-rA)')
pylab.title('Método diferencial')
pylab.show()

print('La constante de velocidad es : %.2f' %math.exp(c[0]))
print('El orden de la reacción es aproximadamente: %.2f' %c[1])
print('El valor del r^2 es: %.4f ' %r2)













































































































