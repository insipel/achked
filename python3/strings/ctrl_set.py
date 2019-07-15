#!/usr/bin/env python3

def ctrl_set(s, p):
    missing = len(p)
    h = { c:0 for c in p}
    i, st, end = 0, 0, len(s)
    cur_size, min_st, min_end = float('inf'), 0, 0

    #print(h)
    while i < end:
        if s[i] in h:
            #print("i:", i, ", h[s[i]]:", h[s[i]])
            v = h[s[i]]
            if v == 0:
                missing -= 1
            h[s[i]] += 1

        while not missing:
            #print("st:", st)
            #print("New st:", min_st, ", end:", i)
            if s[st] in h:
                #print("entering at i:", i)
                v = h[s[st]]
                if v == 1:
                    missing += 1
                    if (i - st) < cur_size:
                        cur_size = i - st
                        min_st = st
                        min_end = i
                        #print("New cur_size:", cur_size+1, ", st:",
                        #        min_st, ", end:", min_end)
                h[s[st]] -= 1
            st += 1
        i += 1

    return cur_size + 1, min_st, min_end

def main():
    #s = "animeshlonesh"
    #p = "nes"
    #s = "animeisimmsshlonesh"
    s = "animeisiimmsshloneshiims"
    p = "ims"
    print("String:", s)
    print("Pattern:", p)
    cur_size, st, end = ctrl_set(s, p)
    print("sstr size:", cur_size, ", st:", st, ", end:", end)

if __name__ == '__main__':
    main()

