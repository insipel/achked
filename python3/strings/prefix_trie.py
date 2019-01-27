#!/usr/bin/env python3

class TrieNode:

    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie:
    def __init__(self, node):
        self.root = node

def add_word(trie, w):
    node = trie.root
    for c in w:
        if c not in node.children:
            node.children[c] = TrieNode()
        node = node.children[c]
    node.end_of_word = True

def create_trie(words):
    root = TrieNode()
    trie = Trie(root)

    for w in words:
        add_word(trie, w)

    return trie

def find_word(trie, w):
    node = trie.root
    for c in w:
        if c not in node.children:
            return False
        node = node.children[c]
    return node.end_of_word

def _dfs(node, word, words):

    if node.end_of_word:
        words.append(''.join(word))

    for c in node.children:
        word.append(c)
        _dfs(node.children[c], word, words)
        word.pop(-1)

def dfs(trie):
    node = trie.root
    word = []
    l = []

    _dfs(node, word, l)
    return l

def get_last_node(node, word):

    for c in word:
        if c not in node.children:
            return None
        node = node.children[c]

    return node

def collect_words(node, word, all_words):
    if node.end_of_word:
        all_words.append(''.join(word))

    for c in node.children:
        word.append(c)
        collect_words(node.children[c], word, all_words)
        word.pop(-1)

def prefix_check(trie, word):
    node = get_last_node(trie.root, word)
    l = [c for c in word]
    all_words = []
    if node:
        collect_words(node, l, all_words)
    return all_words


def main():
    w = ["caller", "call", "basket", "ball", "bask", "do", "an",
            "and", "ant", "doll", "dollar"]
    trie = create_trie(w)
    print("dictionary is:", w)

    print("++ Membership check ++")
    p = ["call", "cold", "dol", "do", "bald"]
    for w in p:
        print(w, " is in trie: ", find_word(trie, w))

    print("++ Trie Walk ++")
    print("list of words:", dfs(trie))

    print("++ Prefix match and collect matches ++")
    word = 'cald'
    print("list of words:", prefix_check(trie, word))

if __name__ == '__main__':
    main()

