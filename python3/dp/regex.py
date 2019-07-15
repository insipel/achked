#!/usr/bin/env python3

# Works Perfect
def regex_dp_class_brief(s, p):
    slen, plen = len(s), len(p)

    res = [[ False for _ in range(plen+1)] for _ in range(slen+1)]

    for i in range(slen):
        res[i][plen] = False
    res[slen][plen] = True

    for i in range(slen, -1, -1):

        for j in range(plen-1, -1, -1):

            # Four cases:
            # if p[j] is '.'
            # if p[j] is '*'
            # if (j+1)<plen and p[j+1] is '*'
            # if p[j] is not a wildcard char
            if i == slen:
                if p[j] == '.':
                    res[i][j] = False
                elif p[j] == '*':
                    res[i][j] = res[i][j+1]
                elif (j+1) < plen and p[j+1] == '*':
                    res[i][j] = res[i][j+2]
                else:
                    res[i][j] = False
            else:
                if p[j] == '.':
                    res[i][j] = res[i+1][j+1]
                elif p[j] == '*':
                    res[i][j] = res[i+1][j] or res[i][j+1]
                #elif s[i] != p[j] '''Note here''' and (j+1) < plen and p[j+1] == '*':
                elif s[i] != p[j] and (j+1) < plen and p[j+1] == '*':
                    res[i][j] = res[i][j+2]
                elif s[i] != p[j]: # Note here
                    res[i][j] = False
                else: # Note here
                    res[i][j] = res[i+1][j+1]

#            if i == slen and p[j] == '.':
#                res[i][j] = False # Done
#            elif p[j] == '.':
#                res[i][j] = res[i+1][j+1] # Done
#            elif i == slen and p[j] == '*':
#                res[i][j] = res[i][j+1] # Done
#            elif p[j] == '*':
#                #print("s[i]:", s[i], ", p[j]:", p[j])
#                res[i][j] = res[i+1][j] or res[i][j+1] # Done
#            elif i == slen and (j+1) < plen and p[j+1] == '*':
#                res[i][j] = res[i][j+2] # Done
#            elif i == slen:
#                res[i][j] = False # Done
#            elif s[i] != p[j] and (j+1) < plen and p[j+1] == '*':
#                res[i][j] = res[i][j+2]
#            elif s[i] != p[j]:
#                res[i][j] = False
#            else:
#                res[i][j] = res[i+1][j+1]

    for i in range(slen+1):
        print(res[i])

    return res[0][0]

def regex_dp_class(s, p):
    slen, plen = len(s), len(p)

    res = [[ False for _ in range(plen+1)] for _ in range(slen+1)]

    for i in range(slen):
        res[i][plen] = False
    res[slen][plen] = True

    for i in range(slen, -1, -1):

        for j in range(plen-1, -1, -1):

            if i == slen and p[j] == '.':
                res[i][j] = False
            elif p[j] == '.':
                res[i][j] = res[i+1][j+1]
            elif i == slen and p[j] == '*':
                res[i][j] = res[i][j+1]
            elif p[j] == '*':
                print("s[i]:", s[i], ", p[j]:", p[j])
                res[i][j] = res[i+1][j] or res[i][j+1]
            elif i == slen and (j+1) < plen and p[j+1] == '*':
                res[i][j] = res[i][j+2]
            elif i == slen:
                res[i][j] = False
            elif s[i] != p[j] and (j+1) < plen and p[j+1] == '*':
                res[i][j] = res[i][j+2]
            elif s[i] != p[j]:
                res[i][j] = False
            else:
                res[i][j] = res[i+1][j+1]

    for i in range(slen+1):
        print(res[i])

    return res[0][0]

def regex_rec(s, p, i, j):

    print("s:", s, ", p:", p, ", i:", i, ", j:", j)
    if i == len(s) and j == len(p):
        return True 
    if j != len(p) and p[j] == '*':
        if i == len(s):
            return False

        if regex_rec(s, p, i+1, j) or regex_rec(s, p, i, j+1):
            return True

    if (i != len(s) and j != len(p)) and (s[i] == p[j] or p[j] == '.'):
        if regex_rec(s, p, i+1, j+1):
            return True

    return False

# INCOMPLETE
def regex_dp_geeks(s, p):
    n, m = len(s), len(p)

    if m == 0:
        return n == 0

    #bool lookup[n + 1][m + 1]; 
    lookup = [[ False for _ in range(m+1)] for _ in range(n+1)]

    #// initailze lookup table to false 
    #memset(lookup, false, sizeof(lookup)); 

    #// empty pattern can match with empty string 
    lookup[0][0] = True

    #// Only '*' can match with empty string 
    #for (int j = 1; j <= m; j++) 
    #    if (pattern[j - 1] == '*') 
    #        lookup[0][j] = lookup[0][j - 1]; 
    for j in range(1, m+1):
        if p[j - 1] == '*':
            lookup[0][j] = lookup[0][j - 1]

    #// fill the table in bottom-up fashion 
    #for (int i = 1; i <= n; i++) 
    for i in range(1, n+1): #(int i = 1; i <= n; i++)
        for j in range(1, m+1): #(int j = 1; j <= m; j++) 
            #// Two cases if we see a '*' 
            #// a) We ignore ‘*’ character and move 
            #//    to next  character in the pattern, 
            #//     i.e., ‘*’ indicates an empty sequence. 
            #// b) '*' character matches with ith 
            #//     character in input 
            if (p[j - 1] == '*'):
                lookup[i][j] = lookup[i][j - 1] or lookup[i - 1][j]
                
            #// Current characters are considered as 
            #// matching in two cases 
            #// (a) current character of pattern is '?' 
            #// (b) characters actually match 
            elif (p[j - 1] == '.' or s[i - 1] == p[j - 1]):
                lookup[i][j] = lookup[i - 1][j - 1]

            #// If characters don't match 
            else:
                lookup[i][j] = False

    return lookup[n][m]

#s = "aabcb"
#p = "aa*.b"
#input: abaac, abac
#pattern: ab*c, a.a*c, .*, .*c, .*d
s="abaac"
#p = "ab*c"
#p = "a.a*c"
p = "a.b*.a*c"
#p = ".*"
#p = ".*c"
#p = ".*d"
print("str:    ", s)
print("pattern:", p)
#print(regex_rec(s, p, 0, 0))
#print(regex_dp_geeks(s, p))
#print(regex_dp_class(s, p))
print(regex_dp_class_brief(s, p))

