# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 21:54:43 2021
Shuffling a deck of cards
@author: Tindi.Sommers
"""
import random


# A function for dealing a deck of cards
def initialize_deck():
    deck = [('Ace', 'Hearts'), ('Deuce', 'Hearts'), ('Three', 'Hearts'), ('Four', 'Hearts'), ('Five', 'Hearts'), ('Six', 'Hearts'), ('Seven', 'Hearts'), ('Eight', 'Hearts'), ('Nine', 'Hearts'), ('Ten', 'Hearts'), ('Jack', 'Hearts'), ('Queen', 'Hearts'), ('King', 'Hearts'),
            ('Ace', 'Diamonds'), ('Deuce', 'Diamonds'), ('Three', 'Diamonds'), ('Four', 'Diamonds'), ('Five', 'Diamonds'), ('Six', 'Diamonds'), ('Seven', 'Diamonds'), ('Eight', 'Diamonds'), ('Nine', 'Diamonds'), ('Ten', 'Diamonds'), ('Jack', 'Diamonds'), ('Queen', 'Diamonds'), ('King', 'Diamonds'),
            ('Ace', 'Clubs'), ('Deuce', 'Clubs'), ('Three', 'Clubs'), ('Four', 'Clubs'), ('Five', 'Clubs'), ('Six', 'Clubs'), ('Seven', 'Clubs'), ('Eight', 'Clubs'), ('Nine', 'Clubs'), ('Ten', 'Clubs'), ('Jack', 'Clubs'), ('Queen', 'Clubs'), ('King', 'Clubs'),
            ('Ace', 'Spades'), ('Deuce', 'Spades'), ('Three', 'Spades'), ('Four', 'Spades'), ('Five', 'Spades'), ('Six', 'Spades'), ('Seven', 'Spades'), ('Eight', 'Spades'), ('Nine', 'Spades'), ('Ten', 'Spades'), ('Jack', 'Spades'), ('Queen', 'Spades'), ('King', 'Spades')]
    random.shuffle(deck)
    return deck


deck = initialize_deck()

for index, card in enumerate(deck):
    if index % 4 == 0:
        print()
    temp = f'{card[0]} of {card[1]}'
    print(f'{temp:<20}', end='')