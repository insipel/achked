#!/usr/bin/env python3

def gen_numeronyms(s):
    l = []
    n = len(s)

    # sz should range from 2 to n - 2(leaving first and last char
    # to compress)
    for sz in range(2, n - 1):

        # 'j' should range from 1st char to n - 3rd char (when sz is
        # 2). for sz 3, it should go till n-4, for sz n-2, it should
        # have just value 1. so the invariant should be i + j should
        # be n-1.
        # to include n - 1 - sz, need to go 1 beyond
        #print("sz:", sz)
        for j in range(1, (n - 1 - sz) + 1):
            #print("sz:", sz, ", j:", j)
            #l.append(s[0] + s[1:j] + str(sz) + s[j+sz:])
            l.append(s[0:j] + str(sz) + s[j+sz:])

    #l.append(s[0] + str(n - 2) + s[n - 1])
    return l

def main():
    s = "animesh"
    l = gen_numeronyms(s)
    print('String is:', s)
    print("Numeronyms are:", l)

if __name__ == '__main__':
    main()

