#!/usr/bin/env python

def DoBreakfast(meat = "Bacon",
                eggs = "Over Easy",
                potatos = "Hash Browns",
                toast = "white",
                beverage = "coffee"):
    print "Here is your %s and %s eggs with %s and %s toast. Can I bring you more %s?" \
            % (meat, eggs, potatos, toast, beverage)


def main():
    DoBreakfast()
    DoBreakfast(meat = "ham", toast = "extra")
    DoBreakfast(beverage = "Tea", potatos = "mashed potatos")
    DoBreakfast()

main()
