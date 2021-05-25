# -*- coding: utf-8 -*-
"""
Created on Fri May 21 17:59:14 2021.

Inter language translation for the United Nations

@author: Tindi.Sommers
"""
from ibm_watson import LanguageTranslatorV3

def translate(text, model):
    """Use Watson Language Translator to translate text from one language to 
       another"""
    # create Watson Translator client
    language_translator = LanguageTranslatorV3(version='2018-05-31')

    # perform the translation
    translated_text = language_translator.translate(
        text=text, model_id=model).get_result()

    # Get 'translations' list. If method translate's text argument has 
    # multiple strings, the list will have multiple entries. We passed
    # one string, so the list contains only one element.
    translations_list = translated_text['translations']
    
    # get translations_list's only element
    first_translation = translations_list[0]

    # get 'translation' key's value, which is the translated text
    translation = first_translation['translation']

    return translation  # return the translated string


# get the text you want to translate from the user
english = input('Enter the text you want to translate in English:')

# translate the english text to spanish
spanish = translate(text=english, model='en-es')

# print the English and spanish texts
print(f'English: {english}\nSpanish: {spanish}\n')

# translate from spanish to french
french = translate(text=spanish, model='es-fr')

# print the English and the French texts
print(f'English: {english}\nFrench: {french}\n')

# translate from French to German
german = translate(text=french, model='fr-de')

# print the English and the German texts
print(f'English: {english}\nGerman: {german}\n')

# translate from German to Italian
italian = translate(text=german, model='de-it')

# print the English and the Italian texts
print(f'English: {english}\nItalian: {italian}\n')

# translate from Italian to English
english2 = translate(text=italian, model='it-en')

# print the English and the French texts
print(f'English: {english}\nEnglish: {english2}')


