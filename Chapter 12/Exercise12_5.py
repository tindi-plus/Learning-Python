# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 15:22:11 2021.

Checking a text for misppelled words

@author: Tindi.Sommers
"""
from textblob import TextBlob
from pathlib import Path

text = TextBlob(Path('The Hamlet_The Prince of Denmark.txt').read_text())
text = text.correct()

#print(f'{"WRONG WORD":<12}{"CORRECT WORD":>12}')
#print()
#for word in text.words:
    #if len(word.lower().spellcheck()) != 1:
        #print(f'{word:<12}{word.correct():>12}')
        
