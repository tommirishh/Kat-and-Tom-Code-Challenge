# -*- coding: utf-8 -*-
"""
Created on Fri Jul 03 17:20:20 2020

@author: kmiri_000
"""

#There exists a staircase with N steps, 
#and you can climb up either 1 or 2 steps at a time. 
#Given N, write a function that returns the number of 
#unique ways you can climb the staircase.

from scipy.special import comb

#this is the method I developed independently 
def steps(n):
    #calculate number of combinations needed to get total 
    if n%2==0:
        i=n/2
    else:
        i=(n-1)/2
    
    #number of steps is at least 1
    k=1
        
    for j in range(1,i+1):
        k=k+comb(n-j,j)
        
    return k 

#I then referred to https://www.dailycodingproblem.com/blog/staircase-problem/       
#which points out that this is a fibonacci sequence 

def steps2(n):
    
    i=1
    j=2
    
    for m in range (0,n-2):
        k=i+j
        i=j
        j=k
        
    return k 

print steps2(7) 