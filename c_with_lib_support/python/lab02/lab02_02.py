#!/usr/bin/env python

while True:
    str_number = raw_input ("Number to square please: ")
    try:
        number = float(str_number)
    except ValueError:
        print "Please try again."
    else:
        break

while True:
    str_digits = raw_input ("How many digits to the right of the decimal place would you like to have displayed? ")
    try:
        digits = int(str_digits)
    except ValueError:
        print "Please try again."
    else:
        break

print "%f squared is %.*f" %(number, digits, (number * number))

