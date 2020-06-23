# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 16:08:58 2020

@author: kmiri_000
"""
from Kathryn1 import list_add
import matplotlib.pyplot as plt
import time

t=[]
x=[]

for i in range(0,20):
    
    xi=range(0,500*i)
    
    t1=time.time()
    
    list_add(20000,xi)
    
    t2=time.time()
    t3=t2-t1
    t.append(t3)
    x.append(500*i)
    

plt.plot(x,t,"x")
plt.xlabel("length of list")
plt.ylabel("time to run function")
plt.show()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
