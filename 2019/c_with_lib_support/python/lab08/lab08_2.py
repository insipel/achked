#!/usr/bin/env python

import lab06_5_copy

def CountVowelsInFile(filename):

    try:
        file_obj = open(filename);
        count = 0

        for line in file_obj:
            count += lab06_5_copy.CountVowels(line)

        return count

    except IOError, info:
        print info

    finally:
        try:
            file_obj.close()
        except UnboundLocalError:
            print "Couldn't close file!"
            return 0

def main(filename = "temp"):
    print "There are %d vowels in the file" % (CountVowelsInFile(filename))

if __name__ == '__main__':
    import sys

    try:
        main(sys.argv[1])
    except  IndexError:
        main()

