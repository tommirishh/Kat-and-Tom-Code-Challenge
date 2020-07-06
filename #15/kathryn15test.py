
from kathryn15 import sample1

import matplotlib.pyplot as plt
import numpy as np

x=[]

for i in range(0,1000):
    x.append(sample1(range(0,100)))
    
plt.scatter(x,np.zeros(1000),marker=".")
plt.show()

