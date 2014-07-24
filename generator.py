#!/usr/bin/python
#Write a generator, genPrimes, that returns the sequence of prime numbers on successive calls to its next() method: 2, 3, 5, 7, 11, ...
#GENERATOR:

# A generator seperates the concept of computing a very long sequence of objects, from the actual process of computing them explicitly.
# Generators allows us to generate each new object as needed as a part of another computation, rather than computing a very long sequence
# only to throw most of it away while you do something on an element, then repeating the process.

def genPrimes():
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


#Any definition having a yield statement is called a generator.
#Rather than generating a list of prime numbers upto some point, stop and return it. Using a generator will help you generate every prime
#number on the fly, as you need them. 

primenum = genPrimes()
print primenum.next() #prints 2
print primenum.next() #prints 3 ... calling next() on generator will generate the primes numbers.

# If we were to use a generator to iterate over a million numbers, how many numbers do we need to store in memory at once?
# Ans: 2 (current number and max number). However you will need a store all the million numbers in ram if a standard fn is used.	
