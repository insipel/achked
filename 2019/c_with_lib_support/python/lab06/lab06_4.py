#!/usr/bin/env python

def MakeOneDeck():
    card_type = ["Clubs", "Diamonds", "Spades", "Hearts"]
    pic_cards = ["Jack", "QUeen", "King", "Ace"]
    num_cards = [x for x in range(2,11)]
    card_num = num_cards + pic_cards
    print card_num

    comp_list = [ "%s of %s" % (num, c_type) for c_type in card_type for num in card_num]
    comp_list += ["Joker, and Joker."]
    return comp_list

def main():

    print MakeOneDeck()

if __name__ == '__main__':
    main()

