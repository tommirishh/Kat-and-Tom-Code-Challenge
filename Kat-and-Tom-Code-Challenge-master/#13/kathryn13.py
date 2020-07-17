# -*- coding: utf-8 -*-
"""
Created on Sun Jul 05 15:33:04 2020

@author: kmiri_000
"""
#returns sorted list of only unique list members

#Given an integer k and a string s, find the length of the longest 
#substring that contains at most k distinct characters.

#For example, given s = "abcba" and k = 2, the longest substring with k 
#distinct characters is "bcb".

def substring(s,k):
    
    #returns list of unique characters from list 
    from numpy import unique

    #i, j are indexs of substring
    i=0
    j=k
    
    #n counts length of substrings
    n=k

    #convert string to list of characters
    s=string2list(s)
    
    
    #iterate over the string
    while j<1+len(s):
        
        #if number of unique characters hasn't gone over k
        if len(unique(s[i:j]))<k+1: 
            #extend the substring by 1
            j=j+1
            n=n+1
        #keep substring same length and move along the string
        else:
            i=i+1
            j=j+1
    
    #return max length of string        
    return n-1
            
def string2list(s):
    
    #coverts a string to a list 
    
    l=[]
    
    for i in range(0,len(s)):
        l.append(s[i])
    
    return l
