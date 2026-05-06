#!/usr/bin/env python
""" Produces a list of primes numbers > 2

"""
MAX = 100

print 'primes less than ', MAX, ' are:'

for number in range (3, MAX, 2):
    div = 2
    while div * div <= number:
        if number % div == 0:
            break
        div += 1
    else:
        print number,

print
