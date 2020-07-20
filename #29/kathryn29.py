#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 22:19:52 2020

@author: kmi20042005
"""

#Run-length encoding is a fast and simple method of encoding strings. 
#The basic idea is to represent repeated successive characters 
#as a single count and character. For example, the string "AAAABBBCCDAA" 
#would be encoded as "4A3B2C1D2A".

#Implement run-length encoding and decoding. 
#You can assume the string to be encoded have no digits and consists solely 
#of alphabetic characters. You can assume the string to be decoded is valid.

#https://www.journaldev.com/23689/python-string-append for list->string method

def encoder(x):
    
    enc=[]
    n=1
    
    #iterate over the string
    for i in range(1,len(x)):
        #keep a count of the multiples of current letter
        if x[i]==x[i-1]:
            n=n+1
        #when a new letter is started add the previous count and letter 
        #and reset count
        else:
            enc.extend((str(n),str(x[i-1])))
            n=1
    
    #add the final letter to the list
    enc.extend((str(n),str(x[-1])))
    
    #convert from list to string
    return ''.join(enc)

def decoder(y):
    
    dec=[]
    
    #iterate in jumps of 2
    for i in range(0,len(y),2):
        #multiply the letters by corresponding values
        dec.append(int(y[i])*y[i+1])
    
    #convert from list to string 
    return "".join(dec)

