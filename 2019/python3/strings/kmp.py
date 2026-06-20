#!/usr/bin/env python3

def preprocess(p):
    lps = [0] * len(p)
    k = 0
    for i in range(1, len(p)):

        while k != 0 and p[k] != p[i]:
            # The following line is crucial to the understanding. This
            # means that if the current char doesn't match the
            # cur_prefix_char (idxed at k = 'd'), then we would like to
            # check the char at the previous unmatched prefix
            # e.g abcabcdabcabchabcabcf
            #           -      -      cur
            # if we are matching 'f', then we'd need to check the lps
            # value at 'd'. Would 'd' match 'f'? Since it's a No, then
            # we'd need to see if 'd' has any prefix matched. It
            # doesn't have any prefixes, lps value of 'f' would be 0.
            # pattern 'ababababca' shows this quite explicitly for
            # char 'c'. It runs through multiple hops before it sets
            # lps for 'c' as 0
            k = lps[k - 1]

        if p[k] == p[i]:
            k += 1

        lps[i] = k

    return lps

def kmp(w, p):
    lps = preprocess(p)
    print(lps)
    l = []

    q = 0 # Number of matches chars in the pattern
    for i in range(len(w)):

        #print('for i:', i, ', q:', q)
        while q != 0 and w[i] != p[q]:
            #print("mismatch: i:", i, ", q:", q, ', new q:', lps[q])
            q = lps[q - 1]

        if w[i] == p[q]:
            q += 1
            #print('q:', q)

        if q == len(p):
            #print('i:', i)
            l.append(i - len(p) + 1)
            q = lps[q - 1]
            #print(l)
    return l

def main():
    #w = "abracadabra"
    #p = "bra"
    w = "bacbababababcabababababcaab"
    p = "ababababca"
    l = kmp(w, p)
    print("pattern mathces at index:", l)

if __name__ == '__main__':
    main()

