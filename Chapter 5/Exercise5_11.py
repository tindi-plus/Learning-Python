# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 19:36:32 2020

Surmarizing text

@author: Tindi.Sommers
"""

import numpy as np


def sumarize_letters(word):
    word = word.lower()
    word_list = []
    word_list += word

    for i, index in enumerate(word_list):
        if index in [' ', ',', ':', ';', '.']:
            del word_list[i]

    letter, freq = np.unique(word_list, return_counts=True)
    print(letter)
    print(freq)

    sample = list(zip(letter, freq))
    print(sample)


a = 'yuh gf,oiop.jhgfd'
sumarize_letters(a)
