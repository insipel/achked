#!/usr/bin/env python3

from collections import Counter


def min_window(s: str, t: str) -> str:
  if not s or not t:
    return ""

  # Dictionary containing all counts of characters in the target pattern
  target_counts = Counter(t)
  required_unique = len(target_counts)

  # Counter to keep track of current characters in the active window
  window_counts = {}

  # Formed is used to keep track of how many unique characters in the target 
  # currently match the desired frequency in the window.
  formed = 0

  # Pointers and window tracking: (window_length, left, right)
  l, r = 0, 0
  min_len = float("inf")
  min_left, min_right = 0, 0

  while r < len(s):
    char = s[r]
    window_counts[char] = window_counts.get(char, 0) + 1

    # If the current character's frequency matches its target frequency, increment 'formed'
    if char in target_counts and window_counts[char] == target_counts[char]:
      formed += 1

    # Try and contract the window from the left until it ceases to be valid
    while l <= r and formed == required_unique:
      char = s[l]

      # Save the smallest window details found so far
      if (r - l + 1) < min_len:
        min_len = r - l + 1
        min_left = l
        min_right = r

      # The character at the left pointer is about to be excluded from the window
      window_counts[char] -= 1
      if char in target_counts and window_counts[char] < target_counts[char]:
        formed -= 1

      l += 1

    # Expand the window outwards by moving the right pointer
    r += 1

  return "" if min_len == float("inf") else s[min_left : min_right + 1]


def main():
  s = "ADOBACODEBANCA"
  t = "ABCA"
  print(f"String: {s}")
  print(f"Pattern: {t}")
  print(f"Minimum Window: {min_window(s, t)}")


if __name__ == "__main__":
  main()

'''
def prep_map(pattern) -> dict:
    pattern_map = {}
    for c in pattern:
        # pattern_map[c] = pattern_map.get(c, 0) - (1 if c in pattern_map else 0)
        pattern_map[c] = pattern_map.get(c, 0)
    return pattern_map

def ctrl_set(input_str, pattern):
    missing = len(pattern)
    pattern_map = prep_map(pattern)
    i, st, end = 0, 0, len(input_str)
    cur_size, min_st, min_end = float('inf'), 0, 0

    #print(pattern_map)
    while i < end:
        if input_str[i] in pattern_map:
            #print("i:", i, ", pattern_map[input_str[i]]:", pattern_map[input_str[i]])
            v = pattern_map[input_str[i]]
            if v == 0:
                missing -= 1
            pattern_map[input_str[i]] += 1

        while not missing:
            #print("st:", st)
            #print("New st:", min_st, ", end:", i)
            if input_str[st] in pattern_map:
                #print("entering at i:", i)
                v = pattern_map[input_str[st]]
                if v == 1:
                    missing += 1
                    if (i - st) < cur_size:
                        cur_size = i - st
                        min_st = st
                        min_end = i
                        #print("New cur_size:", cur_size+1, ", st:",
                        #        min_st, ", end:", min_end)
                pattern_map[input_str[st]] -= 1
            st += 1
        i += 1

    return cur_size + 1, min_st, min_end

def main():
    #input_str = "aniemshlonesh"
    #pattern = "nes"
    #input_str = "animeisimmsshlonesh"
    input_str = "animeisiimmsshloneshiims"
    pattern = "iims"
    print("String:", input_str)
    print("Pattern:", pattern)
    cur_size, st, end = ctrl_set(input_str, pattern)
    print("sstr size:", cur_size, ", st:", st, ", end:", end)

if __name__ == '__main__':
    main()

'''