#!/usr/bin/env python
"""An iterating Deck of cards.
"""
import os
import sys
import random

try:
    sys.path.insert(0, os.path.join(
        os.path.split(__file__)[0], '..'))
except NameError:
    sys.path.insert(0, "..") 

import lab_06_Comprehensions.lab06_4 as cards

class Deck:
    """An iteratiing deck of cards that destroys each card 
    as it is taken with a next call - or as it is iterated
    with a for-loop."""

    def __init__(self):
        self._cards = cards.GetCards()
        random.shuffle(self._cards)

    def __iter__(self):
        return self

    def next(self):
        try:
            return self._cards.pop()
        except IndexError:
            raise StopIteration

class Player:
    def __init__(self):
        self.hand = []

    def AcceptCard(self, card):
        self.hand += [card]

    def __str__(self):
        return ', '.join(self.hand)

class GameDealer:
    def __init__(self, no_players=4, no_cards=5):
        self.no_cards = int(no_cards)
        self.players = [Player() for p in range(int(no_players))]
        self.deck = Deck()
        self.DealHands()

    def DealHands(self):
        """Deals cards to the players."""
        for card_no in range(self.no_cards):
            for player in self.players:
                try:
                    new_card = self.deck.next()
                except StopIteration:
                    new_card = "Sorry"
                player.AcceptCard(new_card)

    def __str__(self):
        """Returns a string representation of the dealt
        cards."""
        return  '\n'.join([str(p) for p in self.players])

def main():
    for players, cards in ((4, 5), (20, 3)):
        print "GameDealer(%d, %d)" % (players, cards)
        print GameDealer(players, cards)

if __name__ == '__main__':
    main()
"""
$ lab14_3.py
GameDealer(4, 5)
4 of Clubs, 6 of Hearts, 6 of Diamonds, Jack of Hearts, 2 of Hearts
Queen of Hearts, Ace of Spades, 5 of Clubs, 7 of Clubs, King of Diamonds
Joker, 3 of Diamonds, Ace of Diamonds, 4 of Hearts, 2 of Clubs
10 of Diamonds, 8 of Clubs, Ace of Clubs, King of Clubs, 9 of Clubs
GameDealer(20, 3)
6 of Hearts, King of Clubs, Jack of Spades
3 of Hearts, Joker, Queen of Spades
5 of Clubs, 7 of Diamonds, 6 of Diamonds
[12 hands deleted]
King of Spades, 9 of Hearts, Sorry
4 of Spades, 8 of Diamonds, Sorry
4 of Hearts, 6 of Clubs, Sorry
8 of Clubs, 10 of Diamonds, Sorry
7 of Spades, Queen of Hearts, Sorry
$ """
