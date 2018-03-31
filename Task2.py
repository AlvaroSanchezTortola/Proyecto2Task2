# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 18:12:02 2018

@author: ALVARO
"""

import DrawFunctionsTask2 as dw
import EMFunctionsTask2 as em

def main():
    a=[[1,2],[3,3],[4,4],[5,2]]
    
    k = 2
    

    X, Y = dw.generateImage(maxx=10, minx=-10, maxy=10, miny=-10, delta=0.025, color='xkcd:white')   
    
    dw.drawDots(a, marker='x', color='k')
    dw.drawContour(xgrid=X, ygrid=Y, sigmax=1.0, sigmay=1.0, mux=2.0, muy=2.0, n=20, color='r')
    
    dw.showImage('output.jpg', dpi=200)
    
main()