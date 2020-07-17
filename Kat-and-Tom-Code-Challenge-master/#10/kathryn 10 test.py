# -*- coding: utf-8 -*-
"""
Created on Fri Jul 03 15:22:26 2020

@author: kmiri_000
"""

from kathryn10 import cd
import time
import matplotlib.pyplot as plt

#convert seconds to milliseconds
fun = lambda i:i

t=[]
n=[]

for i in range (1,1000,100):
    
    t1=time.clock()

    n.append(cd(fun,i))
    
    t2 = time.clock()
    
    t.append(1000*(t2-t1))

plt.plot(n,t)
plt.show()