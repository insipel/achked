#!/usr/bin/env python3

class TrieNode:

    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie:

    def __init__ (self, node):
        self.root = node

def insert_trie(node, word, i):

    for j in range(i, len(word)):
        if word[j] not in node.children:
            node.children[word[j]] = TrieNode()
        node = node.children[word[j]]
    node.end_of_word = True

def build_suffix(word):
    #root = TrieNode()
    trie = Trie(TrieNode())
    root = trie.root

    for i in range(len(word) - 1, -1, -1):
        insert_trie(root, word, i)

    return trie

def print_trie(node, l):
    if node.end_of_word:
        print(''.join(l))

    for c in node.children:
        l.append(c)
        print_trie(node.children[c], l)
        l.pop(-1)

def main():
    word = 'mississippi'
    trie = build_suffix(word)
    l = []
    print_trie(trie.root, l)

if __name__ == '__main__':
    main()


