#!/usr/bin/env python3

# Problem: Longest Palindromic Substring
# Given a string s, find and return the longest substring that is a palindrome.
# A palindrome reads the same forwards and backwards (e.g., "racecar", "abba").
#
# Approach: Expand Around Center (O(n^2) time, O(1) space)
# For each character (and each pair of adjacent characters), treat it as the
# center of a potential palindrome and expand outward while both sides match.
# Track the widest palindrome found across all centers.
#
# Example: s = "abcdcbadabcdbbaaddc"
#          Longest palindromic substring → "abcdcba"


def check_pd(s, st, end):
    # Expand outward from the initial [st, end] window while characters match.
    # Returns the [start, end] indices of the widest palindrome centered here.
    while st >= 0 and end < len(s):
        if s[st] != s[end]:
            # Mismatch: step back inside the last valid palindrome boundary
            return st + 1, end - 1
        st -= 1
        end += 1
    # Loop ended because we hit a string boundary, not a mismatch
    return st + 1, end - 1


def pd_len(s, center_index):
    # Check both palindrome parity rooted at index center_index:
    #   odd-length  → single center character (e.g., "aba")
    odd_st, odd_end = check_pd(s, center_index, center_index)
    #   even-length → center between center_index and center_index+1 (e.g., "abba")
    even_st, even_end = check_pd(s, center_index, center_index + 1)

    # Return whichever expansion produced the longer palindrome
    if odd_end - odd_st > even_end - even_st:
        return odd_st, odd_end
    else:
        return even_st, even_end


def lps(s):
    # Start with an empty best (max_end < max_st means length -1)
    max_st, max_end = 0, -1

    # center_index represents the index where the PD exploration begins
    for center_index in range(len(s)):
        st, end = pd_len(s, center_index)

        # Update the global best if this center produced a longer palindrome
        if end - st > max_end - max_st:
            max_st, max_end = st, end

    return s[max_st : max_end + 1]


def main():
    s = "abcdcbadabcdbbaaddc"
    # s = 'abc'
    print("Longest palindrome substring is:", lps(s))


if __name__ == "__main__":
    main()
