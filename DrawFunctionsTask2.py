# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 20:51:33 2018

@author: ALVARO
"""
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab

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

def drawContour(xgrid, ygrid, sigmax, sigmay, mux, muy, n, color):
    """
    Bivariate Gaussian distribution for equal shape X, Y.
    x, y donde estara, sigma x, sigmay, mux, muy
    """
    Z = mlab.bivariate_normal(xgrid, ygrid, sigmax, sigmay, mux, muy)
    plt.contour(xgrid, ygrid, Z, n, colors=color)
    #plt.clabel(CS, inline=1, fontsize=10)    

def drawDots(matrix, marker, color):
    plt.plot(*zip(*matrix), marker=marker, color=color, ls='')
    
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