# -*- coding: utf-8 -*-
"""
Created on Sun Jul 05 20:22:21 2020

@author: kmiri_000
"""

#The area of a circle is defined as πr^2. 
#Estimate π to 3 decimal places using a Monte Carlo method.

#used this as reference for the maths https://academo.org/demos/estimating-pi-monte-carlo/

def montecircle(n):
    
    #count points within the circle
    k=0
    
    #generate pairs of coordinates
    for i in range(0,n):
        x=1.0*i/n
        for j in range (0,n):
            y=1.0*j/n 
            
            #test if coordinate is in the circle
            if x*x + y*y <= 1:
                k=k+1
                
    approxpi=4.0*k/(n*n)
    
    return round(approxpi,3)

#
print montecircle(5000)
                