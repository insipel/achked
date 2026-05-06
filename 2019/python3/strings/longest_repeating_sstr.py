#!/usr/bin/env python3

from suffix_trie import build_suffix, print_trie

def find_longest(node, l, max_ends, result):
    num_ends = 0

    for c in node.children:
        l.append(c)
        num_ends += find_longest(node.children[c], l, max_ends, result)
        l.pop(-1)

        # Earlier I put num_ends += 1 here to account for a$ but it
        # introduced a double counting bug. When debugged further, I
        # found that it wasn't required. the outside node.end_of_word
        # will also take care of a$ case as well.
        #if node.end_of_word:
        #    num_ends += 1
        #    print("num_ends:", num_ends, ", ", ''.join(l))

        #if num_ends > 1 and len(result[0]) < len(l):
        #    result[0] = ''.join(l)

    if node.end_of_word:
        num_ends += 1
        print("num_ends:", num_ends, ", ", ''.join(l))

    if num_ends > 1 and len(result[0]) < len(l):
        result[0] = ''.join(l)

    return num_ends


def main():
    #word = 'mississippi'
    #word = 'aaaa'
    #word = 'efabcdhefhabcdiefi'
    #word = 'abcdefghi'
    word = 'ababaa'
    #word = 'abaa'
    trie = build_suffix(word)
    l = []
    print_trie(trie.root, l)

    l, max_ends, result = [], [0], ['']
    find_longest(trie.root, l, max_ends, result)
    print("longest repeating sstr is:", result[0])

if __name__ == '__main__':
    main()


'''

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

'''
