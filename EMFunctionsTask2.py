# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 22:53:46 2018

@author: ALVARO
"""
import random
import numpy as np
from scipy.stats import norm
import decimal
decimal.getcontext().prec = 20

def randomGaussian():
    mu = [round(random.uniform(-8, 8), 2), round(random.uniform(-8, 8), 2)]
    
    det = 0.0
    positive_defined = False
    while(det==0.0 or positive_defined == False):
        #sigma = [ [round(random.uniform(0, 3), 1) for _ in range(2)] for i in range(2)]
        temp = round(random.uniform(-3, 3), 1)
        sigma = [[round(random.uniform(-3, 3), 1), temp],[temp, round(random.uniform(-3, 3))]]
        det = np.linalg.det(sigma) 
        positive_defined = np.all(np.linalg.eigvals(sigma) > 0)
        #print("adentro", np.all(np.linalg.eigvals(sigma) > 0), det)
    #print("afuera")
    return mu, sigma

def randomPi(k):
    return np.random.dirichlet(np.ones(k),size=1).transpose()

def probability(point, mu, sig, pi):
    p = pi
    for i in range(len(point)):
        p *= norm.pdf(point[i], mu[i], sig[i][i])
    return p

def getIndexOfLargerNumber(array):
    return np.argmax(array)

def formula(point, mu, sig, pi):
    resta = restaArray(point, mu)
    parte1 = transpose(resta)
    invers = inversa(sig)
    parte2 = multMatrizxArray(invers, resta)
    parte3 = round(multTranspxArray(parte1, parte2), 10)
    try: expo = 2.7182**parte3
    except OverflowError:
        expo = 0.00001
    deter = round(det(sig), 10)
    deter = deter**(-1/2)
    return 0.5*(1/(2*3.1416))*deter*expo

def det(matriz):
    a = matriz[0][0]
    b = matriz[0][1]
    c = matriz[1][0]
    d = matriz[1][1]
    return ((a*b)-(c*d))+0.0001

def transpose(array):
    matriz = [[0, 0],[0,0]]
    matriz[0][0] = array[0]
    matriz[1][0] = array[1]
    return matriz

def restaArray(array_1, array_2):
    array = [0,0]
    array[0] = array_1[0]-array_2[0]
    array[1] = array_1[1]-array_2[1]
    return array

def inversa(matriz):
    salida = [[0, 0], [0, 0]]
    de = 1/(det(matriz)+0.000001)
    salida[0][0] = de*matriz[1][1]
    salida[0][1] = -de*matriz[0][1]
    salida[1][0] = -de*matriz[1][0]
    salida[1][1] = de*matriz[0][0]
    return salida
    
def multMatrizxArray(matriz, array):
    salida = [[0],[0]]
    salida[0] = matriz[0][0]*array[0]+matriz[0][1]*array[1]
    salida[1] = matriz[1][0]*array[0]+matriz[1][1]*array[1]
    return salida

def multTranspxArray(matriz, array):
    return round((matriz[0][0]*array[0]+matriz[1][0]*array[1])+0.00001, 10)

print("formula: ", formula([1, 1], [2, 2], [[0.5,0.15],[0.21,0.15]], 0.5))
print("formula: ", formula([1, 1], [5, 5], [[0.5,0.15],[0.21,0.15]], 0.5))