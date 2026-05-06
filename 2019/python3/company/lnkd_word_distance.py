#!/usr/bin/env python3


from collections import defaultdict
class WordDistance:

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.locations = defaultdict(list)

        # Prepare a mapping from a word to all it's locations (indices).
        for i, w in enumerate(words):
            self.locations[w].append(i)

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        loc1, loc2 = self.locations[word1], self.locations[word2]
        l1, l2 = 0, 0
        min_diff = float("inf")

        # Until the shorter of the two lists is processed
        while l1 < len(loc1) and l2 < len(loc2):
            min_diff = min(min_diff, abs(loc1[l1] - loc2[l2]))
            if loc1[l1] < loc2[l2]:
                l1 += 1
            else:
                l2 += 1
        return min_diff

l = ['apple', 'banana', 'guava', 'kiwi', 'apple', 'cherry', 'jujube',
        'grape', 'cherry', 'kiwi', 'apple', 'jujube']

wd = WordDistance(l)
print(wd.shortest('grape','kiwi'))

'''
Approach 1: Using Preprocessed Sorted Indices

Intuition

A given word can occur multiple times in the original word list. Let's suppose the first word, word1 in the input to the function shortest occurs at the indices [i1, i2, i3, i4] in the original list. Similarly, let's assume that the second word, word2, appears at the following locations inside the word list [j1, j2, j3].

Now, given these list of indices, we are to simply find the pair of indices (i, j) such that their absolute difference is minimum.

    The main idea for this approach is that if the list of these indices is in sorted order, we can find such a pair in linear time.

The idea is to use a two pointer approach. Let's say we have a pointer i for the sorted list of indices of word1 and j for the sorted list of indices of word2. At every iteration, we record the difference of indices i.e. abs(word1[i] - word2[j]). Once we've done that, we have two possible choices for progressing the two pointers.

word1[i] < word2[j]

If this is the case, that means there is no point in moving the j pointer forward. The location indices for the words are in a sorted order. We know that word2[j + 1] > word2[j] because these indices are sorted. So, if we move j forward, then the difference abs(word1[i] - word2[j + 1]) would be even greater than abs(word1[i] - word2[j]). That doesn't help us since we want to find the minimum possible distance (difference) overall.

    So, if we have (word1[i] < word2[j]), we move the pointer 'i' one step forward i.e. (i + 1) in the hopes that abs(word1[i + 1] - word2[j]) would give us a lower distance than abs(word1[i] - word2[j]). We say "hopes" because it is not certain this improvement would happen.

Let's look at two different examples. In the first example we will see that moving i forward gave us the best difference overall (0). In the second example we see that moving i forward leads us to our second case (yet to discuss) but doesn't lead to any improvement in the difference.

Example-1

word1_locations = [2,4,5,9]
word2_locations = [4,10,11]

i, j = 0, 0
min_diff = 2 (abs(2 - 4))
word1[i] < word2[j] i.e. 2 < 4
  move i one step forward

i, j = 1, 0 (abs(4 - 4))
min_diff = 0 (We hit the jackpot!)  

Example-2

word1_locations = [2,7,15,16]
word2_locations = [4,10,11]

i, j = 0, 0
min_diff = 2 (abs(2 - 4))
word1[i] < word2[j] i.e. 2 < 4
  move i one step forward

i, j = 1, 0
min_diff = 2 (2 < abs(7 - 4))

Here, we did not update out global minimum difference.
That is why we said earlier, moving 'i' forward may or
may not give a lower difference. But moving 'j' forward in
our case would definitely worsen the difference (or keep it same!).

Let's move onto our second scenario.

word1[i] > word2[j]

If this is the case, that means there is no point in moving the i pointer forward. We know that word1[i + 1] > word2[j] because these indices are sorted. So, if we move i forward, then the difference abs(word1[i + 1] - word2[j]) would be even greater than abs(word1[i] - word2[j]). That doesn't help us since we want to find the minimum possible distance (difference) overall.

    So, along the similar lines of thought as the previous case, if we have (word1[i] > word2[j]), we move the pointer 'j' one step forward i.e. (j + 1) in the hopes that abs(word1[i] - word2[j + 1]) would give us a lower distance than abs(word1[i] - word2[j]). We say "hopes" because as showcased in the previous scenario, it is not certain this improvement would happen.

Now let's formally look at the algorithm for solving this problem.
'''
