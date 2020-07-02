# -*- coding: utf-8 -*-
"""
Created on Thu Jul 02 18:11:23 2020

@author: kmiri_000
"""
from kathryn10 import sumx
import time
import matplotlib.pyplot as plt
import numpy as np

t=[]
x=[]

for i in range(1,50):
    test = range(0,1000*i)
    
    t1=time.time()
    sumx(test)
    t2=time.time()
    t.append(t2-t1)
    x.append(10*i)
    
plt.scatter(x,t)
plt.show()

