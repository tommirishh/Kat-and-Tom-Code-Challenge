# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 15:57:09 2020

@author: kmiri_000
"""



#deque solution using algorithm from #3 
#https://www.geeksforgeeks.org/sliding-window-maximum-maximum-of-all-subarrays-of-size-k/
#https://www.youtube.com/watch?v=m-Dqu7csdJk

#subroutine to initialise the first deque
#where y=x[0:k]
def initdeque(y):
    
    d=[]
    
    #initialise deque
    for i in range(0,len(y)):
        while len(d)>0 and y[i]>y[d[-1]]:
            d.pop(-1)
        d.append(i)
        
    return d

def dequesum(x,k):
    
    #initialise first deque
    d=initdeque(x[0:k])
    #output max of first window 
    print x[d[0]]
    
    for i in range(k,len(x)):
        if d[0]==i-k:
            d.pop(0)
            
        while len(d)>0 and x[i]>x[d[-1]]:
            d.pop(-1)
        
        d.append(i)
        
        print x[d[0]]
    



#naive solution to compare speed 
def maxsub1(x,k):
    
    n=len(x)
    
    #number of subarrays is n-k+1
    for i in range (0,n-k+1):
        print(max(x[i:i+k]))
        

