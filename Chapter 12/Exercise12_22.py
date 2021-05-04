# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 14:50:50 2021.

Creating text to speech and speech to text

@author: Tindi.Sommers
"""
import speech_recognition as sr
import pyttsx3
from textblob import TextBlob
from gtts import  gTTS
import os

# initialize the recognizer
r = sr.Recognizer()

def speak_en(command):
    """Convert text to speech"""
    # initialize the pyttsx3 engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

def speak_lan(text, lan):
    """Speak a given text in a given laguage using Google Speech to text"""
    tts = gTTS(text, lang=lan)
    # save the audio file
    tts.save('audio.mp3')
    os.system('start audio.mp3')
    
# get the language the user wants to learn
language = input('Input the code for the language you want to learn: ')

# welcome the user
welcome = 'You are welcome to this session. If you want to exit the session, say please exit.'
speak_en(welcome)
# keep looping as long as the program is running
while True:
    try:
        # use the microphone as a source of input
        with sr.Microphone() as source:
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level 
            r.adjust_for_ambient_noise(source, duration=0.5)
            
            # listen to the user input
            audio = r.listen(source, timeout=10, phrase_time_limit=10)
            
            # translate the speech to text using Google
            text = r.recognize_google(audio)
            
            # convert the text to lower case text
            text = text.lower()
            print(text, end='\n')
            
            if text == 'please exit':
                speak_en('Thank you for using this service. Goodbye.')
                break
            
            # translate the text to the choosen language
            blob = TextBlob(text)
            translated = blob.translate(to=language)
            
            # print the translated text
            print(translated, end='\n')

            speak_lan(str(translated), language)
            
    
    except sr.RequestError as e:
        print(f'Could not request results: {e}')
    except sr.UnknownValueError:
        print('An Unknown error occured')


            
    