#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 21:56:07 2020

@author: kmi20042005
"""

#For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.

#Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 
#2 in the second, and 3 in the fourth index 
#(we cannot hold 5 since it would run off to the left), so we can trap 8 units of water.

from kathryn30 import waterwall,waterwall2

#testing version which doesn't allow mid points larger than end points
print(waterwall([2,1,2]))

print(waterwall([3,0,1,3,0,5]))

#testing other version
print(waterwall2([2,1,2]))

print(waterwall2([3,0,1,3,0,5]))

print(waterwall2([5,1,6,3,3,2,4,2,3]))

print(waterwall2([2,1,3,1,5,1,6]))