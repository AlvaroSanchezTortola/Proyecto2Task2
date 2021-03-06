# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 20:51:33 2018

@author: ALVARO
"""
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
from scipy.stats import multivariate_normal
import math, re
import imageio

def generateGrid(maxx, minx, maxy, miny, delta):
    """
    arange genera lista valores consecutivos con saltos delta desde x a y
    meshgrid genera un grid de los valores x y y para imprimir
    """
    delta = 0.025
    x = np.arange(minx, maxx, delta)
    y = np.arange(miny, maxy, delta)
    X, Y = np.meshgrid(x, y)
    return X, Y

def drawContour(xgrid, ygrid, mu, sigma, n, color):
    """
    Bivariate Gaussian distribution for equal shape X, Y.
    x, y donde estara, sigma x, sigmay, mux, muy
    """
    pos = np.dstack((xgrid, ygrid))
    rv = multivariate_normal(mu, sigma)
    plt.contour(xgrid, ygrid, rv.pdf(pos), n, colors=color)    
    
def drawContourF(xgrid, ygrid, mu, sigma, n):
    pos = np.dstack((xgrid, ygrid))
    rv = multivariate_normal(mu, sigma)
    plt.contourf(xgrid, ygrid, rv.pdf(pos), n) 

def drawDots(matrix, marker, color):
    plt.plot(*zip(*matrix), marker=marker, color=color, ls='')
    
def drawDot(x, y, marker, color):
    plt.plot(x, y, marker=marker, color=color, ls='')
    
def generateFigure(maxx, minx, maxy, miny, color):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.set_facecolor(color)
    #plt.title('{} gaussianos'.format())
    plt.xlim(minx, maxx)
    plt.ylim(miny, maxy)
    
def generateImage(maxx, minx, maxy, miny, delta, color):
    X, Y = generateGrid(maxx, minx, maxy, miny, delta)
    generateFigure(maxx, minx, maxy, miny, color)
    return X, Y

def showImage(name, dpi):
    fig1 = plt.gcf()    
    plt.show()
    fig1.savefig(name, bbox_inches='tight', dpi=dpi)

def getFirstDecimal(a):
    frac=math.modf(a)
    frac1=str(frac[0])
    return frac1[2]

def readFile(file_name, log=False):
    matriz=[]
    data = [line for line in open(file_name, 'r')]
    for i in range(len(data)):
        columna = []
        linea = data[i]
        linea = linea.replace('[', '')
        linea = linea.replace(']', '')
        linea = linea.replace(' ', '')
        linea = linea.replace('\n', '')
        if(log):print(linea)
       
       
        n1, n2 = linea.split(",")
        if(log):print(n1, n2)
        columna.append(float(n1))
        columna.append(float(n2))
        matriz.append(columna)

    if (log):
        for j in range(len(data)):
            print(matriz[j])
        print("\n")
    return matriz

def Gif(imagenes):
    imageio.mimsave('movie.gif', imagenes)