#!/usr/bin/env python
""" Package excercise"""

def AddUpNumbers(filename):
    count = 0

    try:
        file_hdl = open(filename)
        for line in file_hdl:
            count += banana.total_text.TotalText(line, count)

    except IOError, info:
        print info
        return

    finally:
        try:
            file_hdl.close()
        except UnboundLocalError:
            pass
        return count



def main(filename = "../banana/numbers.txt"):
    print "Count: %.2f" % AddUpNumbers(filename)


if __name__ == '__main__':
    import sys
    import os

    sys.path.insert(0, "..")
    import banana.total_text
    print dir(banana.total_text)
    print __file__
    print os.path.abspath(__file__)
    print os.path.join(os.path.split(__file__)[0], '..')

    try:
        main(sys.argv[1])
    except IndexError:
        main()

