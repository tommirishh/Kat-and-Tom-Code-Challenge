#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 21:06:59 2020

@author: kmi20042005
"""

#solution assuming inside wall heights =< end walls
def waterwall(wall):
    
    height=min(wall[0],wall[-1])
    
    water=0
    
    for i in range(1,len(wall)-1):
        water=water+(height-wall[i])
    return water

#solution allowing for wall height > end walls
def waterwall2(wall):
   
    left=wall[0]
    right=wall[-1]
    
    j=0
    water=0
    
    for i in range(1,len(wall)-1):
          
        if wall[i]>right:
            
            x = min(left,wall[i])-right
  
            if x>0:
                water = water + (i-j-1)*x

            j=i
            
        elif wall[i]>left:
            left=wall[i]
          
        else:
            water=water+(min(left,right)-wall[i])
        
    return water
        