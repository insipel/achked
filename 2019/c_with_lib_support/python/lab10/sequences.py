#!/usr/bin/env python

import cProfile

def DoLens(sequence):
    i = 0
    while i < len(sequence):
        sequence[i]
        i += 1

def DoWhile(sequence):
    i = 0
    sequence_len = len(sequence)
    while i < sequence_len:
        sequence[i]
        i += 1

def DoRange(sequence):
    for i in range(len(sequence)):
        sequence[i]

def DoIterator(sequence):
    for element in sequence:
        element

def DoAll(seq):
    DoLens(seq)
    DoWhile(seq)
    DoRange(seq)
    DoIterator(seq)

def main():
    seq = [x for x in range(10000)]
    cProfile.run("DoAll(%s)" % str(seq))

if __name__ == '__main__':
    main()
