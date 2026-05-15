#!/usr/bin/env python3

# Problem: Longest Repeating Substring
# Given a string, find the longest substring that appears at least twice
# (at different positions) within the string.
#
# Approach: Suffix Trie
# Build a suffix trie for the input string. Every internal node in the trie
# represents a prefix shared by two or more suffixes — i.e., a repeated
# substring. DFS the trie, counting how many suffixes (end-of-word markers)
# exist below each node. Any node with num_ends > 1 is a repeated substring;
# track the longest such prefix seen.
#
# Example: s = "ababaa"  →  longest repeating substring: "aba"
#
# See the DP/LCP alternative at the bottom of this file (O(n^2) time/space).


from suffix_trie import build_suffix, print_trie


def find_longest(node, l, max_ends, result):
    # l is the current path of characters from root to this node (the prefix so far)
    num_ends = 0

    for c in node.children:
        l.append(c)
        # Recurse and accumulate how many suffix endings exist in this subtree
        num_ends += find_longest(node.children[c], l, max_ends, result)
        l.pop(-1)

        # Earlier I put num_ends += 1 here to account for a$ but it
        # introduced a double counting bug. When debugged further, I
        # found that it wasn't required. the outside node.end_of_word
        # will also take care of a$ case as well.
        # if node.end_of_word:
        #    num_ends += 1
        #    print("num_ends:", num_ends, ", ", ''.join(l))

        # if num_ends > 1 and len(result[0]) < len(l):
        #    result[0] = ''.join(l)

    if node.end_of_word:
        # This node is the terminal of one suffix — count it
        num_ends += 1
        print("num_ends:", num_ends, ", ", "".join(l))

    # num_ends > 1 means the prefix l is shared by at least two suffixes → it repeats
    if num_ends > 1 and len(result[0]) < len(l):
        result[0] = "".join(l)

    return num_ends


def main():
    # word = 'mississippi'
    # word = 'aaaa'
    # word = 'efabcdhefhabcdiefi'
    # word = 'abcdefghi'
    word = "ababaa"
    # word = 'abaa'
    trie = build_suffix(word)
    l = []
    print_trie(trie.root, l)

    # result is a list so find_longest can mutate it (Python has no pass-by-ref for strings)
    l, max_ends, result = [], [0], [""]
    find_longest(trie.root, l, max_ends, result)
    print("longest repeating sstr is:", result[0])


if __name__ == "__main__":
    main()


# Brute Force Approach
# Try every possible substring length from longest to shortest.
# For each length, slide a window across the string and track seen substrings in a set.
# The first duplicate found is the longest repeating substring.
# Time: O(n^3) — O(n^2) substrings, each hashed in O(n)
# Space: O(n^2) — the set can hold up to O(n) substrings each of length O(n)
def longest_repeating_brute(s):
    n = len(s)
    # Try lengths from n-1 down to 1; return as soon as we find a repeat
    for length in range(n - 1, 0, -1):
        seen = set()
        for i in range(n - length + 1):
            sub = s[i : i + length]
            if sub in seen:
                return sub  # First hit at this length is our answer
            seen.add(sub)
    return ""  # No repeating substring found


"""

DP Solution from the IK Editorial

package LongestRepeatedSubstring.solutions; /**
 * *********************** PROBLEM DESCRIPTION ***************************
 * Given a string str of length n, find the longest repeated substring in it.
 */

import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class other_solution {

    // -------------------- START ----------------------

    public static String getLongestRepeatedSubstring(String inputStr) {
        int n = inputStr.length();
        int[][] lcp = new int[n][n];
        // lcp[i][j] = k means length of longest common prefix between suffix starting at i and suffix
        // starting at j is k

        for (int i = 0; i < n; i++) {
            lcp[i][n - 1] = (inputStr.charAt(i) == inputStr.charAt(n - 1) ? 1 : 0);
        }

        for (int i = 0; i < n; i++) {
            lcp[n - 1][i] = (inputStr.charAt(n - 1) == inputStr.charAt(i) ? 1 : 0);
        }

        int lrsLen = 0, lrsIndex = -1;
        for (int i = n - 2; i >= 0; i--) {
            for (int j = n - 2; j >= 0; j--) {
                if (inputStr.charAt(i) == inputStr.charAt(j)) {
                    lcp[i][j] = 1 + lcp[i + 1][j + 1];
                } else {
                    lcp[i][j] = 0;
                }
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (lcp[i][j] > lrsLen) {
                    lrsIndex = i;
                    lrsLen = lcp[i][j];
                }
            }
        }

        String lrs = "";
        if (lrsIndex > -1) {
            lrs = inputStr.substring(lrsIndex, lrsIndex + lrsLen);
        }

        return lrs;
    }

    // -------------------- END ----------------------

    private static BufferedReader br;

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new PrintWriter(System.out));

        String inputStr = br.readLine().trim();

        String result = getLongestRepeatedSubstring(inputStr);
        bufferedWriter.write(result);
        bufferedWriter.newLine();
        bufferedWriter.close();

        br.close();
    }

}

/**
 * Time complexity: O(n^2)
 * Space complexity: O(n^2)
 */

"""
