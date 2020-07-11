# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 13:05:19 2020

@author: kmiri_000
"""

from kathryn18 import initdeque

#testing subroutine
print initdeque([1,2,3,4])
print initdeque([4,3,2,1])
print initdeque([1,3,4,2])

from kathryn18 import dequesum

#testig dequesum
print dequesum([8,5,10,7,9,4,15,12,90,13],4)
print dequesum([10,5,2,7,8,7],3)

import time
print time.clock()