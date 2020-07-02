# -*- coding: utf-8 -*-
"""
Created on Thu Jul 02 17:13:20 2020

@author: kmiri_000
"""
#challenge Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.
#For example, [2, 4, 6, 2, 5] should return 13


# the algorithm from this page can be used for +ve numbers only
# https://www.geeksforgeeks.org/maximum-sum-such-that-no-two-elements-are-adjacent/
# I added an if statement to allow for -ve numbers

# Q:is it fair to assume that a list of negative numbers highest sum = 0? 

def sumx(x):
    
    #inc is 
    inc=[x[0]]
    exc=[0]

    for i in range(1,len(x)):
        if x[i]>1:
            inc.append(exc[i-1]+x[i])
        else:
            inc.append(exc[i-1])
        exc.append(max(inc[i-1],exc[i-1]))
        
    return max(inc[-1],exc[-1])
  
