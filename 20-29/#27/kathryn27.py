# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).
#For example, given the string "([])[]({})", you should return true.
#Given the string "([)]" or "((()", you should return false.
#reference https://medium.com/avmconsulting-blog/how-to-solve-the-balanced-brackets-interview-question-babcdafb5298

def brackets(x):
    	
	#define open and closing brackets
    op=['(','{','[']
    cl=[')','}',']']
    stack=[]
	
	#if first value is closing bracket 
    if x[0] in cl:
        return False
	
    for i in range(0,len(x)):
	    if x[i] in op:
		    stack.append(x[i])
	    else:
		    if op.index(stack.pop())!=cl.index(x[i]):
			    return False
	
    if stack == []:
	    return True 
    
	
