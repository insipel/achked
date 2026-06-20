#!/usr/bin/env python3

def lsstr_no_repeats2(s):

    if not s:
        return -1

    h = { c:0 for c in s}
    repeat = 0 # change this 2 for strictly 2 repeats
    i, st, end = 0, 0, len(s)
    max_sz, max_st = float('-inf'), 0

    while i < end:

        v = h[s[i]]
        if v != 0:
            repeat += 1
        h[s[i]] += 1
        
        #while not left:
        if repeat:
            if (i - st) > max_sz:
                #print(h)
                max_sz = i - st
                max_st = st
                #print("getting max_sZ:", max_sz, max_st)

            for j in range(st, i):
                h[s[j]] -= 1
                if h[s[j]] == 1:
                    #h[s[j]] -= 1
                    repeat -= 1
                    #print("breaking at index ", j)
                    break
            st = j+1
            #print("st is now:", st)

        i += 1

    # Good bug: MUST AVOID AVOID AVOID
    if not repeat and (i - st) > max_sz:
        max_sz = i - st
        max_st = st
        #print("all chars unique")

    #print ("st:", max_st, ", end:", max_st+max_sz+1)
    return s[max_st:(max_st+max_sz)]

def lsstr_no_repeats(s):

    if not s:
        return -1

    h = { c:0 for c in s}
    left = 1 # change this 2 for strictly 2 repeats
    i, st, end = 0, 0, len(s)
    max_sz, max_st = float('-inf'), 0

    while i < end:

        if s[i] in h:
            v = h[s[i]]
            if v != 0:
                left -= 1
            h[s[i]] += 1
        
        #while not left:
        if not left:

            if (i - st) > max_sz:
                #print(h)
                max_sz = i - st
                max_st = st
                #print("getting max_sZ:", max_sz, max_st)

            for j in range(st, i):
                v = h[s[j]]
                h[s[j]] -= 1
                if v > 1:
                    left += 1
                    #print("breaking at index ", j)
                    break
            st = j+1
            #print("st is now:", st)

        i += 1

    # Good bug: MUST AVOID AVOID AVOID
    if left and (i - st) > max_sz:
        max_sz = i - st
        max_st = st
        #print("all chars unique")

    #print ("st:", max_st, ", end:", max_st+max_sz+1)
    return s[max_st:(max_st+max_sz)]

print(lsstr_no_repeats("animesh"))
print(lsstr_no_repeats("aniamesh"))
print(lsstr_no_repeats("aaaaaaaa"))
print(lsstr_no_repeats("abababacababa"))

print("New routine")
print(lsstr_no_repeats2("animesh"))
print(lsstr_no_repeats2("aniamesh"))
print(lsstr_no_repeats2("aaaaaaaa"))
print(lsstr_no_repeats2("abababacababa"))
