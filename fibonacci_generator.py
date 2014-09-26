#!/usr/bin/python

def fib():
    """ Generates the fibonacci sequence on demand """
    f = []
    while True:
        if len(f) == 0:
            f.append(0)
            yield 0
        elif len(f) ==1 :
            f.append(1)
            yield 1
        else:
            x =  f[-1] + f[-2]
            yield x
            f.append(x)

y = fib()
print y.next()
print y.next()
print y.next()
print y.next()
print y.next()
print y.next()
print y.next()
print y.next()
print y.next()
print y.next()
print y.next()
print y.next()
print y.next()
print y.next()
print y.next()
print y.next()
print y.next()
print y.next()
