#!/usr/bin/env python

import random

def FlipCoin():
    rand = random.random()
    if (rand < 0.5):
        print "Heads"
    else:
        print "Tail"


def main():
    print "test flipping coin"

    FlipCoin()

main()
