#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np
x = range(0, 30)
p0 = [0,0,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,0,0,0,0,0,0,0,0,0,0,0,None,0]
p1 = [None,1,None,None,1,None,None,None,None,None,None,None,None,None,None,None,None,1,1,1,1,1,1,1,None,1,1,1,None,1]
p2 = [None,2,None,None,2,None,None,None,None,2,None,None,None,None,None,None,None,None,None,None,None,None,2,2,2,2,None,None,None,2]
p3 = [None,3,None,3,None,3,3,None,3,None,3,None,3,3,3,3,3,None,3,None,3,None,3,None,None,3,None,3,3,None]
p4 = [None,4,None,4,None,4,None,None,None,None,None,None,4,4,4,None,None,None,None,None,4,None,None,None,None,4,None,None,4,None]
ylabel  = ["P1", "P2", "P3", "P4", "P5"]
xlabel  =  range(1,31)
for xc in x:
    plt.axvline(x=xc)
#ax1.axes.get_yaxis().set_visible(False) 
plt.yticks(x, ylabel)
#plt.scatter(x, p1,color="green",s=100)
plt.scatter(x, p0,color="red",s=100)
plt.scatter(x, p1,color="green",s=100)
plt.scatter(x, p2,color="blue",s=100)
plt.scatter(x, p3,color="purple",s=100)
plt.scatter(x, p4,color="brown",s=100)
plt.xticks(np.arange(min(x), max(x)+1, 1.0),xlabel)
#plt.legend(['p1', 'p2', 'p3', 'p4'], loc='upper left')
plt.show()
