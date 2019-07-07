#!/usr/bin/env python3

def string_interleave(s1, s2, s3):
    l1 = len(s1)
    l2 = len(s2)
    l3 = len(s3)

    res = [ [ False for _ in range(l2+1)]
                    for _ in range(l1+1)]

    res[0][0] = True
    for i in range(1, l1+1):
        res[i][0] = res[i-1][0] and s1[i - 1] == s3[i - 1]

    for j in range(1, l2+1):
        res[0][j] = res[0][j-1] and s2[j - 1] == s3[j - 1]

    for i in range(1, l1+1):
        for j in range(1, l2+1):

            if i > 0 and j > 0 and s1[i - 1] == s2[j - 1]  and s1[i - 1] == s3[i + j - 1]:

                res[i][j] = res[i - 1][j] or res[i][j - 1]
            elif i > 0 and s1[i - 1] == s3[i + j - 1]:
                res[i][j] = res[i - 1][j]
            elif j > 0 and s2[j - 1] == s3[i + j - 1]:
                res[i][j] = res[i][j - 1]

    for i in range(l1+1):
        print(res[i])
    return res[l1][l2]

def string_interleave_not_working(s1, s2, s3):
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
    s1 = "ab"
    s2 = "bab"
    s3 = "baabb"
    #s1 = "animesh"  # This is the example where my simple logic  to
    # determine interleaving won't work. Problem appears after
    # matching 'kum'. FOr next char 'a', it'll match in s1. However
    # the next char 'r' will not find a match in either s1 or s2.
    #s2 = "kumarpathak"
    #s3 = "kumaranimeshpathak"
    print(string_interleave(s1, s2, s3))

if __name__ == '__main__':
    main()

