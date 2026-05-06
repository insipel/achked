#!/usr/bin/env python

def GenerateKey(name):
    sp_word = name.split(" ")
    print sp_word
    return sp_word[1]


def main():
    names = ["Jack Sparrow", "George Washington", "Tiny Sparrow",
    "Jean Ann Kennedy"]

    names.sort(key=GenerateKey)
    print names
    print len(names)

    for name in names:
        sp_word = name.split(" ")
        print sp_word
        print len(sp_word)

main()

