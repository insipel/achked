#!/usr/bin/env python

print "Think of a number between 1 and 10"

num_guess = 0
low = 1
high = 10

print "Think of a number between 1 and 10: "

while True:
    guess = (high + low)/2
    print "is your number ", str(guess) + '?'

    while True:
        print """"Please press:
                'y' for yes
                'n' for no"""
        yes_no = raw_input()
        if (yes_no == 'y' || yes_no = 'n'):
            break
        print "Please press again!"

    if (yes_no == 'y'):
        print "Hurray! only", str(num_guess) + "."
    else:
        num_guess += 1

        while True:
            print "No? Then please press:"
            print "'h' if", guess, " is higher than your number"
            print "'l' if", guess, " is lower than your number"
            high_low = raw_input()

            if (high_low

