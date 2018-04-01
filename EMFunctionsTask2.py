# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 22:53:46 2018

@author: ALVARO
"""
import random
import numpy as np
from scipy.stats import norm

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