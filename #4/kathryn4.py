# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 16:41:14 2020

@author: kmiri_000
"""

def lowest_int(k):
    
    k.sort()
    
    for i in range(0,len(k)-1):
        if k[i]>0:
            if k[i+1]-k[i]>1:
                return k[i]+1
    
    if k[-1]>-1:
        return k[-1]+1
    else:
        return 1
            
