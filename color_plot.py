#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np
x = range(1, 31)
#ax1 = plt.axes(frameon=False)
p1 = [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,1]
p2 = [0,2,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,2,2,0,2,2,2,0,2]
p3 = [0,3,0,0,3,0,0,0,0,3,0,0,0,0,0,0,0,3,0,3,0,0,3,3,3,3,0,0,0,3]
p4 = [0,4,0,4,0,4,0,0,0,0,0,0,4,4,4,4,4,0,4,0,4,0,0,0,0,0,0,4,4,0]
for xc in x:
    plt.axvline(x=xc)
#ax1.axes.get_yaxis().set_visible(False) 
plt.scatter(x, p1,color="green",s=100)
plt.scatter(x, p2,color="red",s=100)
plt.scatter(x, p3,color="blue",s=100)
plt.scatter(x, p4,color="purple",s=100)
plt.xticks(np.arange(min(x), max(x)+1, 1.0))
plt.legend(['p1', 'p2', 'p3', 'p4'], loc='upper left')
plt.show()

