# -*- coding: utf-8 -*-
from random import random
import numpy as np
from scipy.optimize import curve_fit

def ajuste(function,data_x,data_y,p,sigmay):
    res, cov = curve_fit(function, data_x, data_y, maxfev=1000,  p0 = p, sigma = sigmay)
    x = np.linspace(data_x.min(),data_x.max(),500)
    return res, cov, x

def recta(x,a,b):
    return a+b*x

def simulacion(distancia, disparos, radio):
    suma=0
    for i in range(disparos):
        x = random()*2 - 1
        theta = np.arccos(x)
    
        if theta>=(-np.arctan(radio/distancia)) and theta<=(np.arctan(radio/distancia)):
            suma+=1
    return suma