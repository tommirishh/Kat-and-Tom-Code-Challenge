#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 19:01:02 2020

@author: kmi20042005
"""

#For example, given the list of words ["the", "quick", "brown", "fox", "jumps",
# "over", "the", "lazy", "dog"] and k = 16, you should return the following:

#["the  quick brown", # 1 extra space on the left
#"fox  jumps  over", # 2 extra spaces distributed evenly
#"the   lazy   dog"] # 4 extra spaces distributed evenly

from kathryn28 import justify 

#example used in email
print(justify(["the", "quick", "brown", "fox", "jumps","over", "the", "lazy", "dog"],16))

#test when there's only 1 word in final sentence
print(justify(["I","am","pretty","good","at","Python"],12))

#test only 1 word in middle sentence
print(justify(["I","am","pretty","good","at","Python"],8))



