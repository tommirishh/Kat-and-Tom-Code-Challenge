# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 16:41:14 2020

@author: kmiri_000
"""

def lowest_int(k):
    
    #sort from smallest to largest
    k.sort()
    
    #find positive integers with difference of 2 or more
    for i in range(0,len(k)-1):
        if k[i]>0:
            if k[i+1]-k[i]>1:
                return k[i]+1
    
    #if no positive integers have a gap
    if k[-1]>-1:
        return k[-1]+1
    #if all are negative
    else:
        return 1
            
