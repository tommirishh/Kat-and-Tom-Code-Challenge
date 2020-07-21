#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 19:20:58 2020

@author: kmi20042005
"""
#Implement regular expression matching with the following special characters:

#. (period) which matches any single character
#* (asterisk) which matches zero or more of the preceding element
#That is, implement a function that takes in a string 
#and a valid regular expression and returns whether or not the string 
#matches the regular expression.

#For example, given the regular expression "ra." and the string 
#"ray", your function should return true. 
#The same regular expression on the string "raymond" should return false.

#Given the regular expression ".*at" and the string "chat", 
#your function should return true. The same regular expression on the string 
#"chats" should return false.

#I did this just with '.' to start
def period(st,ex):
    
    st=list(st)
    ex=list(ex)
    
    if len(st)!=len(ex):
        return False
    
    for i in range(0,len(st)):
        if st[i]!='.':
            if st[i]!=ex[i]:
                return False
            
    return True


        
            
            