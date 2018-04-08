# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 18:12:02 2018

@author: ALVARO
"""

import DrawFunctionsTask2 as dw
import EMFunctionsTask2 as em
import numpy
import random

def main():
    #a=[[1,2],[3,3],[4,4],[5,2],[-1,-5],[-3,1],[-4,2],[-2,-2],   [-5,-5],[5,-2],[-7,5],[0,0]]
    #a=[ [random.uniform(-10, 10), random.uniform(-10, 10)] for i in range(25) ]
    a= dw.readFile("input_task2.txt")
    
    cluster=[]
    colors = ['r', 'b', 'g', 'y', 'o', 'p']
    k = 2

    X, Y = dw.generateImage(maxx=10, minx=-10, maxy=10, miny=-10, delta=0.025, color='xkcd:white')   
    
    dw.drawDots(a, marker='x', color='k')
    
    pi = em.randomPi(k)
    gaussians = [[em.randomGaussian(), pi[i]]for i in range(k)]
    print (gaussians)
    for i in range(k): dw.drawContour(X, Y, gaussians[i][0][0], gaussians[i][0][1], int(dw.getFirstDecimal(gaussians[i][1][0]))+2, colors[i]) 
    
    dw.showImage('output.jpg', dpi=200)
       
    for j in range(len(a)):
        probs = [em.probability(a[j], gaussians[i][0][0], gaussians[i][0][1], gaussians[i][1][0]) for i in range(k)]
        cluster.append(em.getIndexOfLargerNumber(probs))
    print(probs)
    print(cluster)
    
    X, Y = dw.generateImage(maxx=10, minx=-10, maxy=10, miny=-10, delta=0.025, color='xkcd:white')  
    for l in range(len(a)):
        dw.drawDot(a[l][0], a[l][1], marker='x', color=colors[cluster[l]])
    for i in range(k): dw.drawContour(X, Y, gaussians[i][0][0], gaussians[i][0][1], int(dw.getFirstDecimal(gaussians[i][1][0]))+2, colors[i]) 
    dw.showImage('output.jpg', dpi=200)
    
    for _ in range(5):
        #agrupar puntos segun cluster
        grupos = []
        for i in range(k):
            tupla = []
            for j in range(len(a)):
                if(cluster[j]==i): 
                    tupla.append(a[j])
            grupos.append(tupla)    
        #print(grupos)
        #actualizar pi
        percentage_assigned_to_cluster = []
        for i in range(k): percentage_assigned_to_cluster.append(cluster.count(i)/float(len(a)))
        #print(percentage_assigned_to_cluster)
        for i in range(len(gaussians)): gaussians[i][1][0] = percentage_assigned_to_cluster[i]
        #print(gaussians)
        
        #actualizar mu y sigma
        for i in range(k):
            xes = []
            yes = []
            for j in range(len(grupos[i])):
                xes.append(grupos[i][j][0])
                yes.append(grupos[i][j][1])
            #actualizar mu
            gaussians[i][0][0][0] = round(numpy.mean(xes), 2)
            gaussians[i][0][0][1] = round(numpy.mean(yes), 2)
            
            #actualizar sigma
            gaussians[i][0][1][0][0] = round(numpy.std(xes), 1)+0.00001
            gaussians[i][0][1][1][1] = round(numpy.std(yes), 1)+0.00001
        
        X, Y = dw.generateImage(maxx=10, minx=-10, maxy=10, miny=-10, delta=0.025, color='xkcd:white')  
        for l in range(len(a)):
            dw.drawDot(a[l][0], a[l][1], marker='x', color=colors[cluster[l]])
        for i in range(k): 
            try:
                dw.drawContour(X, Y, gaussians[i][0][0], gaussians[i][0][1], int(dw.getFirstDecimal(gaussians[i][1][0]))+2, colors[i]) 
            except ValueError:
                print("La carlitos")
                
        dw.showImage('output.jpg', dpi=200)
        
        #!!falta actualizar los puentos luego de una pasada
        cluster = probs = []
        for j in range(len(a)):
            probs = [em.probability(a[j], gaussians[i][0][0], gaussians[i][0][1], gaussians[i][1][0]) for i in range(k)]
            cluster.append(em.getIndexOfLargerNumber(probs))
        print(probs)
        print(cluster)
    
    
        
main()