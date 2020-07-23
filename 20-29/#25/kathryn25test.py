#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 19:50:15 2020

@author: kmi20042005
"""

#For example, given the regular expression "ra." and the string 
#"ray", your function should return true. 
#The same regular expression on the string "raymond" should return false.

#Given the regular expression ".*at" and the string "chat", 
#your function should return true. The same regular expression on the string 
#"chats" should return false.

from kathryn25 import expmatch 

#testing version with just .
print(expmatch(".ay","ray"))
print(expmatch(".ay","raymond"))
print(expmatch(".*at","chat"))
print(expmatch(".*at",'chats'))