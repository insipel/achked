#!/usr/bin/env python

class StringInputException(AttributeError):
    pass

def UpIt(string):
    if not string.islower():
        raise StringInputException, ("string %s has upper-case characters" % string)

    return string.upper()

try:
    print UpIt("aBc")
except StringInputException, exception_obj:
    print exception_obj

