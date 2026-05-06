#!/usr/bin/env python

def printf(fmt_str, *fmt_args):
    print fmt_str % fmt_args

def main():
    pass

if __name__ == '__main__':
    printf("%s temp %s", "1", "2")

