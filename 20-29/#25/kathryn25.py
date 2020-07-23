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


#python library that supports regular expressions
import re

#implemented using library which already has these functions
def expmatch(exp,st):
    match=re.search(exp,st)
    
    #match.group returns any part of string that matches
    #check whether it matches whole string
    return match.group()==st


