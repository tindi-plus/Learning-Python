# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 19:09:17 2021.

Generate and display random sentences

@author: Tindi.Sommers
"""

import numpy as np
article = np.array(['the', 'a'])
noun = np.array(['car', 'goat', 'house', 'shoe', 'ball', 'book', 'water'])
verb = np.array(['eating', 'driving', 'wearing', 'reading', 'drinking', 'playing'])
preposition = np.array(['on', 'above', 'in', 'with', 'by', 'below', 'from'])


def sentence():
    """Generate sentences at random."""
    global article, noun, verb, preposition
    my_sentence = article[np.random.randint(0, 2)]
    my_sentence += ' ' + noun[np.random.randint(0, 7)]
    my_sentence += ' ' + verb[np.random.randint(0, 6)]
    my_sentence += ' ' + preposition[np.random.randint(0, 7)]
    my_sentence += ' ' + article[np.random.randint(0, 2)]
    my_sentence += ' ' + noun[np.random.randint(0, 7)]
    my_sentence += '.'
    return my_sentence.capitalize()


# generate the sentences
for i in range(20):
    print(sentence())
