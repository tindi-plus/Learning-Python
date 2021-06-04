# -*- coding: utf-8 -*-
"""
@create date: 04-06-2021 11:14:55
@modify date: 04-06-2021 11:14:55
@author: Tindi Sommers
@email:
@desc: Speech recognition using Google Speech to Text Services
"""
import speech_recognition as sr
import pydub  # used to load a WAV file
import pydub.playback  # used to play a WAV file
from gtts import  gTTS
from textblob import TextBlob

# initialize the recognizer
r = sr.Recognizer()

# record the audio from the customer
def record_audio():
    """Record audio input using the microphone"""
    # try to use the microphone
    try:
        with sr.Microphone() as source:
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level 
            r.adjust_for_ambient_noise(source, duration=0.5)
            
            # listen to the user input
            audio = r.listen(source, timeout=2)
            
            return audio # return the recorded audio (AudioData format)
    except:
        print('An error occured. Could not record the audio.')

def play_audio(file_name):
    """Use the pydub module (pip install pydub) to play a WAV file."""
    sound = pydub.AudioSegment.from_mp3(file_name)
    pydub.playback.play(sound)

def text_to_speech(text, lan):
    """Speak a given text in a given laguage using Google Speech to text"""
    tts = gTTS(text, lang=lan)
    # save the audio file
    tts.save('audio.mp3')
    play_audio('audio.mp3')

def speech_to_text(audio):
    """Convert a text file to an audio file"""
    # translate the speech to text using Google
    text = r.recognize_google(audio)
    return text.lower()

if __name__ == '__main__':
    language = input('What language do you want to translate to? Enter the language code: ')
    speech = record_audio()
    text = speech_to_text(speech)
    print(text)
    blob = TextBlob(text)
    # translate the text to the given language.
    translated_text = blob.translate(to=language)
    print(translated_text)
    text_to_speech(str(translated_text), language)


