#!/usr/bin/env python3

import re

fd = open("test.txt")

regex = re.compile(" ")
for i, line in enumerate(fd):
    line = line.rstrip("\n")
    lineitems = line.split(" ")
    print(i, lineitems)

