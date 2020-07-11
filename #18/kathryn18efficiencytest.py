# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 13:17:29 2020

@author: kmiri_000
"""

from kathryn18 import dequesum, maxsub1
import numpy as np 
import time
import matplotlib.pyplot as plt

dequetime=[]
maxsubtime=[]
nrange=range(1000,20000,1000)

for n in nrange:
    x=np.random.randint(0,20000,n)
    
    t1=time.clock()
    maxsub1(x,50)
    t2=time.clock()
    dequesum(x,50)
    t3=time.clock()
    
    dequetime.append(t3-t2)
    maxsubtime.append(t2-t1)
    
plt.plot(nrange,dequetime,marker='x')
plt.plot(nrange,maxsubtime,marker='+')
plt.show()