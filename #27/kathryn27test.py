#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 19:32:44 2020

@author: kmi20042005
"""

from kathryn27 import brackets

#test cases for challenge #27 
#TRUE cases
print(brackets('[]'))
print(brackets('[{}]'))
print(brackets('{()()[[]]}'))

#FALSE cases
print(brackets(']'))
print(brackets('{[}]'))
print(brackets(']['))
