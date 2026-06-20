#!/usr/bin/env python


def main():
    num_words = 5;
    word_list = []

    for i in range(num_words):

        word = raw_input("Enter the next word: ")

        word_list.insert(i, word)
        print word_list

        if word_list.count(word) == 1:
            print "%d Word is: %s" % (i, word)


main()

