#!/usr/bin/env python

import re

def AddNumbers(filename):

    hdl = open(filename)
    s = re.compile(r"(\d*\.\d+|\d+|\d\.)")
    for line in hdl:
        print line
        res = s.search(line)
        print res.groups()
        print s.findall(line)

def main():
    AddNumbers("./numbers.txt")

if __name__ == '__main__':
    main()

