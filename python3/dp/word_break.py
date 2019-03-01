#!/usr/bin/env python3

# I prefer this one as indexing makes much more sense in this one.
def working_wordbreak(word, dict):
    n = len(word)
    res = [0] * n
    l = [[] for _ in range(n)]
    print(l)

    for i in range(n-1, -1, -1):
        for j in range(i+1, n+1): # need to do n+1 as in the
            # statement, to fetch 'part', we need to extend j 1 beyond
            # the index. j will end at n, so in word[i:n] will include
            # i to n-1th chars from the word.
            part = word[i:j]
            if part in dict:
                if j == n:
                    res[i] += 1
                    print(i, part)
                    l[i].append(part)
                else:
                    res[i] += res[j]
                    for part_word in l[j]:
                        l[i].append(part + " " + part_word)

    print(res)
    print(l)
    return res[0]

def wordbreak(word, dict):
    n = len(word)
    res = [0] * n
    l = [[] for _ in range(n)]
    print(l)

    for i in range(n-1, -1, -1):
        for j in range(i, n):
            part = word[i:j+1] # Even though it works, I would think
            # that this is not readable as the res[] has to be used
            # with index j+1.
            if part in dict:
                if j == n - 1:
                    res[i] += 1
                    print(i, part)
                    l[i].append(part)
                else:
                    res[i] += res[j+1]
                    for part_word in l[j+1]:
                        l[i].append(part + " " + part_word)

    print(res)
    print(l)
    return res[0]

def main():
    dict = {"cat", "cats", "sand", "and", "dog"}
    word = "catsanddog"
    print(wordbreak(word, dict))

    dict1 = {"mobile","samsung","sam","sung", 
             "man","mango","icecream","and", 
             "go","i","like","ice","cream"}
    #print(wordbreak("ilikelikeimangoiii", dict1))
    #print(wordbreak("samsungandmango", dict1))
    print(wordbreak("samsungandmangok", dict1))

if __name__ == '__main__':
    main()

