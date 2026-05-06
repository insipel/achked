#!/usr/bin/env python

def print_dict(**str_dict):
    strs = {}
    strs.update(str_dict)

    print ("Come to a %(theme) %(what) on %(date)" % strs)

def main():
    event_d = {"what":"party", "date":"Oct 31", "theme":"Halloween"}
    print_dict(**event_d)

if __name__ == '__main__':
    main()

