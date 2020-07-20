# -*- coding: utf-8 -*-
"""
Created on Fri Jul 03 15:07:39 2020

@author: kmiri_000
"""
#reference material for higher order functions
#https://www.geeksforgeeks.org/passing-function-as-an-argument-in-python/#:~:text=Because%20functions%20are%20objects%20we,a%20function%20as%20an%20argument.
import time

#writing as a standard function
def cd(func,n):
    
    #sleep suspends execution for input number of seconds
    time.sleep(n/1000)
    
    return func(n)
    



