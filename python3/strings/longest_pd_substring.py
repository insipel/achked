#!/usr/bin/env python3

def check_pd(s, st, end):
    while st >= 0 and end < len(s):
        if s[st] != s[end]:
            return st + 1, end - 1
        st -= 1
        end += 1
    return st + 1, end - 1

def pd_len(s, i):
    # Odd length
    odd_st, odd_end = check_pd(s, i, i)

    # Even length
    even_st, even_end = check_pd(s, i, i+1)

    if (odd_end - odd_st > even_end - even_st):
        return odd_st, odd_end
    else:
        return even_st, even_end

def lps(s):
    max_st, max_end = 0, -1

    for i in range(len(s)):
        st, end = pd_len(s, i)

        if (end - st > max_end - max_st):
            max_st, max_end = st, end

    return s[max_st:max_end+1]

def main():
    #s = 'abcdcbadabcdbbaaddc'
    s = 'abc'
    print("Longest palindrome substring is:", lps(s))

if __name__ == '__main__':
    main()

