#!/usr/bin/env python3

def power(base, exp):
    res = 1
    orig_base=base
    orig_exp = exp

    while exp:
        print(base, exp, res)
        if exp & 1:
            res = res * base
        base *= base
        exp = exp >> 1

    print("Power(", orig_base,",",orig_exp,"):", res)

power(3, 7)

