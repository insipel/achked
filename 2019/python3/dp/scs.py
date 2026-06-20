#!/usr/bin/env python3

# Shortest Common Supersequence

# This routine prints LCS in reverse order. Hence if we had used
# recursion to print, it would have printed in correct order. Here to
# print in right order, need to use a temporary buffer.
def print_scs(scs, s1, s2):
    n = len(scs)
    m = len(scs[0])

    i = n - 1
    j = m - 1

    while i > 0 and j > 0:

        if scs[i][j] == 1:
            print(s1[i - 1])
            #print(s1[i])
            i = i - 1
            j = j - 1
        elif scs[i][j] == 2:
            print(s1[i - 1])
            #print(s1[i])
            i = i - 1
        elif scs[i][j] == 3:
            print(s2[j - 1])
            #print(s2[j])
            j = j - 1
        else:
            print("this case should never happen")

    while j > 0:
        print(s2[j - 1])
        j -= 1

    while i > 0:
        print(s1[i - 1])
        i -= 1

def find_scs(s1, s2):
    l1 = len(s1)
    l2 = len(s2)

    # increase the size of 
    res = [ [0 for _ in range(l2 + 1)]
               for _ in range(l1 + 1)]
    scs = [ [0 for _ in range(l2 + 1)]
               for _ in range(l1 + 1)]

    for i in range(l1+1):
        for j in range(l2+1):
            if i == 0 or j == 0:
                res[i][j] = i if j == 0 else j
                scs[i][j] = 2 if j == 0 else 3
            elif s1[i - 1] == s2[j - 1]:
                print(s1[i - 1], s2[j - 1])
                res[i][j] = 1 + res[i-1][j-1]
                scs[i][j] = 1
            else:
                if res[i][j - 1] < res[i - 1][j]:
                    res[i][j] = res[i][j - 1] + 1
                    scs[i][j] = 3 # Up
                else:
                    res[i][j] = res[i - 1][j] + 1
                    scs[i][j] = 2 # Left

    for i in range(l1+1):
        print(res[i])

    print("SCS trace")
    for i in range(l1+1):
        print(scs[i])

    print_scs(scs, s1, s2)
    return res[l1][l2]

def main():
    #s1 = "ABXYZM"
    s1 = "CXYZM"
    s2 = "BDYZNPQM"
    #s1 = "ABXYZM"
    #s2 = "DNPQ"
    print(s1, s2)
    print(find_scs(s1, s2))

if __name__ == '__main__':
    main()

