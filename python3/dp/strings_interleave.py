#!/usr/bin/env python3

def string_interleave(s1, s2, s3):
    l1 = len(s1)
    l2 = len(s2)
    l3 = len(s3)

    i1 = i2 = 0
    for i3 in range(l3):
        if i1 < len(s1) and s1[i1] == s3[i3]:
            i1 += 1
        elif i2 < len(s2) and s2[i2] == s3[i3]:
            i2 += 1
        else:
            break;

    print(i1, i2, i3)
    if i3 != len(s3) - 1 or i1 != len(s1) or i2 != len(s2):
        return False
    else:
        return True


def main():
    #s1 = "whyyouarehere"
    #s2 = "wheredoyougo"
    #s3 = "whywhereyouaredoyouherego"
    #s1 = "ab"
    #s2 = "bb"
    #s3 = "abbb"
    s1 = "animesh"  # This is the example where my simple logic  to
    # determine interleaving won't work. Problem appears after
    # matching 'kum'. FOr next char 'a', it'll match in s1. However
    # the next char 'r' will not find a match in either s1 or s2.
    s2 = "kumarpathak"
    s3 = "kumaranimeshpathak"
    print(string_interleave(s1, s2, s3))

if __name__ == '__main__':
    main()

