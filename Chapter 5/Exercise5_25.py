# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 22:39:47 2021
Shuffling a deck of cards
@author: Tindi.Sommers
"""

import random
import numpy as np
import sys


# A function for shuffling a deck of cards
def initialize_deck():
    deck = [('Ace', 'Hearts'), ('Deuce', 'Hearts'), ('Three', 'Hearts'), ('Four', 'Hearts'), ('Five', 'Hearts'), ('Six', 'Hearts'), ('Seven', 'Hearts'), ('Eight', 'Hearts'), ('Nine', 'Hearts'), ('Ten', 'Hearts'), ('Jack', 'Hearts'), ('Queen', 'Hearts'), ('King', 'Hearts'),
            ('Ace', 'Diamonds'), ('Deuce', 'Diamonds'), ('Three', 'Diamonds'), ('Four', 'Diamonds'), ('Five', 'Diamonds'), ('Six', 'Diamonds'), ('Seven', 'Diamonds'), ('Eight', 'Diamonds'), ('Nine', 'Diamonds'), ('Ten', 'Diamonds'), ('Jack', 'Diamonds'), ('Queen', 'Diamonds'), ('King', 'Diamonds'),
            ('Ace', 'Clubs'), ('Deuce', 'Clubs'), ('Three', 'Clubs'), ('Four', 'Clubs'), ('Five', 'Clubs'), ('Six', 'Clubs'), ('Seven', 'Clubs'), ('Eight', 'Clubs'), ('Nine', 'Clubs'), ('Ten', 'Clubs'), ('Jack', 'Clubs'), ('Queen', 'Clubs'), ('King', 'Clubs'),
            ('Ace', 'Spades'), ('Deuce', 'Spades'), ('Three', 'Spades'), ('Four', 'Spades'), ('Five', 'Spades'), ('Six', 'Spades'), ('Seven', 'Spades'), ('Eight', 'Spades'), ('Nine', 'Spades'), ('Ten', 'Spades'), ('Jack', 'Spades'), ('Queen', 'Spades'), ('King', 'Spades')]
    random.shuffle(deck)
    return deck


# for index, card in enumerate(deck):
#    if index % 4 == 0:
#        print()
#    temp = f'{card[0]} of {card[1]}'
#    print(f'{temp:<20}', end='')

# A function for dealing a five-card hand

def deal_hand():
    deck = initialize_deck()
    hand1 = []
    for i in range(5):
        hand1.append(deck[0])
        del deck[0]
        random.shuffle(deck)
    hand2 = []
    for i in range(5, 10):
        hand2.append(deck[0])
        del deck[0]
        random.shuffle(deck)
    return hand1, hand2


# A function for checking ONE PAIR
def is_pair(hand):
    hand_faces = [x[0] for x in hand]
    face, freq = np.unique(hand_faces, return_counts=True)
    count = 0
    for i in freq:
        if i == 2:
            count += 1
    if count == 1:
        return True
    else:
        return False


# A function for checking TWO PAIRS
def is_two_pair(hand):
    hand_faces = [x[0] for x in hand]
    face, freq = np.unique(hand_faces, return_counts=True)
    count = 0
    for i in freq:
        if i == 2:
            count += 1
    if count == 2:
        return True
    else:
        return False


# A function for cheking three of a kind
def is_three_of_a_kind(hand):
    hand_faces = [x[0] for x in hand]
    face, freq = np.unique(hand_faces, return_counts=True)
    count = 0
    for i in freq:
        if i >= 3:
            count += 1
    if count >= 1:
        return True
    else:
        return False


# A function for checking if a hand is flush
def is_flush(hand):
    hand_suit = [x[1] for x in hand]
    suit, freq = np.unique(hand_suit, return_counts=True)
    for i in freq:
        if i == 5:
            return True
        else:
            return False


# A function for checking if a hand is a full house
def is_full_house(hand):
    hand_faces = [x[0] for x in hand]
    faces, freq = np.unique(hand_faces, return_counts=True)
    count1, count2 = 0
    for i in freq:
        if i == 2:
            count1 += 1
        elif i == 3:
            count2 += 1

    if count1 >= 1 and count2 >= 1:
        return True
    else:
        return False


# A function for checking four of a kind
def is_four_kind(hand):
    hand_faces = [x[0] for x in hand]
    face, freq = np.unique(hand_faces, return_counts=True)
    count = 0
    for i in freq:
        if i >= 4:
            count += 1
    if count >= 1:
        return True
    else:
        return False


# deal two game hands and determine who is the winner
hand1, hand2 = deal_hand()
print(hand1, hand2)
print()
# check which of the hands is a pair
if is_pair(hand1) and not is_pair(hand2):
    print(f'Hand1: {hand1} is the winner! It is a pair.')
    sys.exit()
if is_pair(hand2) and not is_pair(hand1):
    print(f'Hand2: {hand2} is the winner! It is a pair.')
    sys.exit()

# check which of the two hands has two pairs
if is_two_pair(hand1) and not is_two_pair(hand2):
    print(f'Hand1: {hand1} is the winner! It has two pairs.')
    sys.exit()
if is_two_pair(hand2) and not is_two_pair(hand1):
    print(f'Hand2: {hand2} is the winner! It has two pairs.')
    sys.exit()
