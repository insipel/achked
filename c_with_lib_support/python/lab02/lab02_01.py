#!/usr/bin/env python

name = raw_input("Name please? ")

while True:
    money = raw_input("Money please? ")
    try:
        money1 = float(money)
    except ValueError:
        print "Please try again!"
    else:
        break

print name + ", give me $%.2f" %(money1/2)


