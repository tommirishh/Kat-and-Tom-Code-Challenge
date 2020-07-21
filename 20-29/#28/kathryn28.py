#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 16:17:51 2020

@author: kmi20042005
"""

#Write an algorithm to justify text. Given a sequence of words and an 
#integer line length k, return a list of strings which represents each line, 
#fully justified.

#More specifically, you should have as many words as possible in each line. 
#There should be at least one space between each word. 
#Pad extra spaces when necessary so that each line has exactly length k. 
#Spaces should be distributed as equally as possible, with the extra spaces, 
#if any, distributed starting from the left.

#If you can only fit one word on a line, then you should pad the right-hand 
#side with spaces.

#Each word is guaranteed not to be longer than k.


# I made this without using any reference material
def justify(words,k):
    
    #justified is the final output
    justified=[]
    #string resets for each line
    string=[]
    
    #while there are still words to be added 
    while len(words)>0:
        #if the length of current sentence + next word is less than k
        #add the next word on the end 
        if len(''.join(string))+len(words[0])+len(string)<=k:
            string.append(words[0])
            words.pop(0)
        #otherwise distribute the remaining spaces
        else:
            #l is the number of words in this sentence
            l=len(string)
            #n is the remaining number of characters to fill with spaces
            n=k-len(''.join(string))
            
            #if statement to handle case where only 1 word on a line
            if l==1:
                string.append(n*' ')
            
            else:
                #m is the number of spaces to be put in between every word
                m=int(n/(l-1))
                #o is remaining number of spaces to distribute from the left
                o=n%(l-1)
            
                #add spaces to every mid-point
                if m>0:
                    for i in range(1,l):
                        string.insert(l-i,m*" ")
            
                #distribute remaining spaces from the left
                if o>0:
                    for i in range(1,2*o,2):
                        string[i]=string[i]+' '
            
            #add the string to final out put
            justified.append(''.join(string))
            #reset the string
            string=[]
    

    #the final line will never be >k so repeat above section
    #to add the final line on 
    l=len(string)
    n=k-len(''.join(string))
    
    if l==1:
        string.append(n*' ')
            
    else:
        m=int(n/(l-1))
        o=n%(l-1)
            
        if m>0:
            for i in range(1,l):
                string.insert(l-i,m*" ")
            
            if o>0:
                for i in range(1,2*o,2):
                    string[i]=string[i]+' '
                    
    justified.append(''.join(string))    

            
            
    return justified 
