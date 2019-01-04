#!/usr/bin/env python

import os
import lab08_2

def CountVowelsInDir(dirname):
    count = 0
    for (this_dir, dir_names, file_names) in os.walk(dirname):
        for file_name in file_names:
            count += lab08_2.CountVowelsInFile(file_name)

    return count

def main(dirname = os.getcwd()):
    print dirname
    print CountVowelsInDir(dirname)

if __name__ == '__main__':
    import sys

    try:
        main(sys.argv[1])
    except IndexError:
        main()

