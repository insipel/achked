#!/usr/bin/env python

import random

def FlipCoin():
    rand = random.random()
    if (rand < 0.5):
        # print "Heads"
        return 1
    else:
        # print "Tail"
        return 0

def GetHeads(target):
    local_target = 0
    num_flips = 0

    while True:

        num_flips += 1

        heads = FlipCoin()
        if heads:
            local_target+= 1

        if (local_target == target):
            return num_flips

def main():
    print "test get heads"

    while True:
        cont = raw_input("Want to continue?")
        if not cont:
            target = random.randint(1, 10)
            print "Target: %d" % target
            num_flips = GetHeads(target)
            print "Took %d flips to get to target %d" % (num_flips, target)
            continue
        else:
            break

main()

