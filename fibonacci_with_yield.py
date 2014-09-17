#!/usr/bin/python

def fn():
    """ Function which generates the numbers """
    a = 0
    b = 1
    while True:
        yield a + b
        a,b = b,a+b
 
#This is not good to have print statements here!
print "0"
print "1"
x = fn()
print x.next()
print x.next()
print x.next()
print x.next()
print x.next()
print x.next()
print x.next()
print x.next()
print x.next()
print x.next()
print x.next()
print x.next()
print x.next()
print x.next()
