# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 20:22:13 2020

@author: kmiri_000
"""

#Given an array of integers, return a new array such that each element 
#at index i of the new array is the product of all the numbers 
#in the original array except the one at i.

#For example, if our input was [1, 2, 3, 4, 5], 
#the expected output would be [120, 60, 40, 30, 24]. 
#If our input was [3, 2, 1], the expected output would be [2, 3, 6].

def mult_array1(a):
    
    #b is the resulting array, c will be product of all numbers in a
    b=[]
    c=1
    
    #find product of all numbers
    for i in range(0,len(a)):
        c=c*a[i]
        
    
    #divide by each number to make final array 
    for i in range(0,len(a)):
        bi=c/a[i]
        b.append(bi)
        
    return b

#test case
print mult_array1([1,2,3,4,5])
#test case 
print mult_array1([3,2,1])

#Follow-up: what if you can't use division? 

def mult_array2(a):
    
    #b is the resulting array 
    b=[]
    
    #iterate over each number 
    for i in range(0,len(a)):
        
        #c will be the multiplied value
        c=1
        
        #remove value at i and save for later
        ai=a.pop(0)
        
        #iterate over remaining values to multiply
        for i in range(0,len(a)):
            c=c*a[i]
        
        #add to the array 
        b.append(c)
        
        #add removed value back in at the end of the array 
        a.append(ai)
        
    return b


#test case
print mult_array2([1,2,3,4,5])
#test case 
print mult_array2([3,2,1])