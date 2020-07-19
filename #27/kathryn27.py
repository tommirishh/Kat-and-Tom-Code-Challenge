# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).
#For example, given the string "([])[]({})", you should return true.
#Given the string "([)]" or "((()", you should return false.

x=[1,2,3,4]

def brackets(x):
    
    
	
	#define open and closing brackets
	op=["(","{","["]
	cl=[")","}","]"]

	for i in range(0,len(x)):
		if x[i] in op:
			n=i
		else:
			
			m=i