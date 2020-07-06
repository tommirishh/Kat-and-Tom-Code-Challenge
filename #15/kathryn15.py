# -*- coding: utf-8 -*-
"""
Created on Mon Jul 06 16:51:20 2020

@author: kmiri_000
"""

#Given a stream of elements too large to store in memory, 
#pick a random element from the stream with uniform probability.

#To do this I used resevoir sampling 
#This video is a really nice explanation https://www.youtube.com/watch?v=A1iwzSew5QY

import random 

#Algorithm to pick 1 element from an array of unknown length
def sample1(x):
    
    #counter starts at 0
    i=1
    s=x[0]
    
    #iterate over the array
    while i<len(x):
        
        #pick random interger between 0 and i
        r=random.randint(0,i-1)
        
        #probability of replacing s with x[i] is 1/i
        if r==i-1:
            s=x[i]
        i=i+1
            
    return s

#Algorithm to pick k elemets from an array of unknown length 
#reference https://florian.github.io/reservoir-sampling/
def samplek(x,k):
    
    #resevoir starts with first k elements
    s=x[0:k]
    i=k+1
    while i<len(x):
        
        #generate random number between 0 and 1
        r=random.random()
        
        #probability of including x[i] in reservoir is k/i
        if r<1.0*k/i:
            #replace randomly selected value of reservoir
            j=random.randint(0,k-1)
            s[j]=x[i]
            
        i=i+1
    
    return s
                