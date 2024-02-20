# -*- coding: utf-8 -*-

"""
Este programa realiza una simulación del número de cuentas que realiza un
detector circular de radio R al colocarse a diferentes distancias de una
fuente de radiación.

Esta simulación, creada como parte de las prácticas de Efecto Compton de
la asignatura Técnicas Experimentales IV, sirve para comprender mejor
la eficiencia de un detector de radiación (eficiencia geométrica, intrínseca
y total)

Entre los resultados esperados para esta simulació, se espera lo siguiente:
    1) La eficiencia geométrica decade con la distancia
    2) La eficiencia intrínseca no depende de la distancia
    3) La eficiencia total, suma de ambas, debe ser liniealmente dependiente
    con la eficiencia geométrica.
"""

import matplotlib.pyplot as plt
import numpy as np
from src import functions

# Tomamos distintas distancias en centímetros a las que colocar el detector
distancias = np.array([6.2,6.7,7.5,8.1,9.0,11.0,12.8,15.0])

# Aproximamos el detector cuadrado a un detector circular con el mismo area
lx = 1
ly = 1
R = np.sqrt(lx*ly/np.pi)

# Numero de disparos (emisiones)
n = 100000

# Cuentas
suma=0
N = []

egeo = np.zeros(len(distancias))
aux=0

# Realizamos la simulación para cada distancia
for distancia in distancias:
    suma = functions.simulacion(distancia, n, R)
    N.append(suma/2)
    egeo[aux] = suma/n
    print('Cuentas que se detectan: ', N[aux])
    print('Eficiencia geometrica de ', egeo[aux])
    aux+=1

# Representamos la eficiencia geometrica con la distancia
plt.figure(1)
plt.scatter(distancias,egeo,8,color='black')
plt.xlabel('Distancia / cm')
plt.ylabel('$\epsilon _{g}$')

et = np.array([0.00112259, 0.00081751, 0.0006869 , 0.0005943 , 0.00045266,
       0.00032299, 0.0002403 , 0.00014952])

s_et = np.array([28.2469534, 11.7233600, 6.65550916, 4.99302814,
       4.36200894, 5.80602036, 3.41727683, 3.12773709])/100000

ei = et/egeo
sei = 1/np.array(egeo)**2 * s_et*egeo

# Representamos la eficiencia intrinseca con la distancia
plt.figure(2)
plt.scatter(distancias,ei,8,color='black')
plt.errorbar(distancias,ei,yerr=sei,fmt='none', ecolor='red',elinewidth=0.8)
plt.xlabel('Distancia / cm')
plt.ylabel('Eficiencia intrínseca $\epsilon _{i}$')


plt.figure(3)
res,cov,xx = functions.ajuste(functions.recta,egeo,et,[1,ei[2]],sei)

a,b = res
sa,sb = np.sqrt(np.diag(cov))

# Representamos la eficiencia total con la geométrica

plt.plot(xx,functions.recta(xx,a,b),'k--')
plt.scatter(egeo,et,8,color='black')
plt.errorbar(egeo,et,yerr=s_et,fmt='none', ecolor='red',elinewidth=0.8)
plt.xlabel('Eficiencia geométrica $\epsilon _{g}$')
plt.ylabel('Eficiencia total $\epsilon _{t}$')
