#!/usr/bin/python
#Write a generator, genPrimes, that returns the sequence of prime numbers on successive calls to its next() method: 2, 3, 5, 7, 11, ...

def gnePrimes():
    num = 2
    prime = True
    while True:
        if prime == True:
            yield num
        num = num + 1
        for i in range(2,num):
            if num%i==0:
                prime = False
                break
        else:
            prime = True           


for i in gnePrimes():
    print i
            
