#!/usr/bin/env python
"""Use list comprehensions to make a deck of cards."""

def GetCards():
    """Return a deck of cards as a list of strings."""
    values = [str(x) for x in range(2, 11)
              ] + ['Jack','Queen','King','Ace']
    suits = ('Clubs', 'Diamonds', 'Hearts', 'Spades') 
    deck = ['%s of %s' % (value, suit) for suit in suits
			for value in values] + ["Joker"] * 2
    return deck

def DisplayDeck(deck, columns_wide=80):
    number_of_cards = len(deck)
    print "The deck of %d cards contains:" % number_of_cards
    width_so_far = 0
    for index, card in enumerate(deck):
        if index == number_of_cards - 1: #last card in deck
            new_card = 'and %s.' % card
        else:
            new_card = '%s,' % card
        card_len = len(new_card) + 1 #for space added by print
        width_so_far += card_len
        if width_so_far > columns_wide:
            print
            width_so_far = card_len
        print new_card,

def main():
    deck = GetCards()
    DisplayDeck(deck)

if __name__ == '__main__':
    main()
"""





$ lab06_4.py
The deck of 54 cards contains:
2 of Clubs, 3 of Clubs, 4 of Clubs, 5 of Clubs, 6 of Clubs, 7 of Clubs,
8 of Clubs, 9 of Clubs, 10 of Clubs, Jack of Clubs, Queen of Clubs,
[some skipped]
3 of Spades, 4 of Spades, 5 of Spades, 6 of Spades, 7 of Spades, 8 of Spades,
9 of Spades, 10 of Spades, Jack of Spades, Queen of Spades, King of Spades,
Ace of Spades, Joker, and Joker.
$ """

