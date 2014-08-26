#!/usr/bin/python

import matplotlib.pyplot as plt
#import numpy as np
x = range(0, 31)
p0 = [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None]
p1 = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 1, None, None, None, None, None, None, None, None, None, None, None]
p2 = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, 2, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
p3 = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 3, None, None, None, None, None, None, None, None, None, None, None]
p4 = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
#ylabel  = ["P0","P1","P3","P4","P5"]
xlabel  =  range(1,31)
print len(p0), len(p1), len(p2), len(p3), len(p4)
#for xc in x:
#    plt.axvline(x=xc, color='b',ls='dotted')
#ax1.axes.get_yaxis().set_visible(False) 
plt.yticks(x, ylabel)
#plt.scatter(x, p1,color="green",s=100)
plt.scatter(x, p0,color="red",s=100)
plt.scatter(x, p1,color="green",s=100)
plt.scatter(x, p2,color="blue",s=100)
plt.scatter(x, p3,color="purple",s=100)
plt.scatter(x, p4,color="brown",s=100)
#plt.xticks(np.arange(min(x), max(x)+1, 1.0),xlabel)
plt.xticks(range(0,30),xlabel)
plt.title(", ".join(ylabel)+"August 2014")
plt.grid(True,color="b")
#plt.legend(['p1', 'p2', 'p3', 'p4'], loc='upper left')
plt.show()
