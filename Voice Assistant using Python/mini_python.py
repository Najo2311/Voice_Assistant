import pyttsx3    # text to speech
import speech_recognition as sr       # speech to text   
import wikipedia
import webbrowser    #for search
import requests
import datetime
import pyjokes
import playsound
from gtts import gTTS     #text into audio
import os        # to interact with operating system
import wolframalpha     # to  calculate expertlevel answers
from selenium import webdriver    #automates web browsers
def speak(audio):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty("voices")
    engine.setProperty('voice', voices[1].id)# 1 for female and 0 for male voice
    rate=engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.say(audio)
    engine.runAndWait()

def sptext():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold =1     
        audio = r.listen(source)
    try:
        print("Recognizing...")
        data = r.recognize_google(audio, language='en-in')
        print("User said:" + data + "\n")
    except Exception as e:
        print(e)
        speak("I didnt understand")
        return "None"
    return data

if __name__ == "__main__":
    speak("Voice Assistance Activated ")
    speak("How can i help you")
    while True:
        data= sptext().lower()
        if 'wikipedia' in data:
            speak("Searching Wikipedia ...")
            data= data.replace("wikipedia", '')
            results = wikipedia.summary(data, sentences=2)
            speak("According to wikipedia")
            speak(results)
        elif ' Who are you' in data:
            speak("Hello I am Najiya")
        elif 'open youtube' in data:
            speak("opening youtube")
            webbrowser.open("youtube.com")
        elif 'open google' in data:
            speak("opening google")
            webbrowser.open("google.com")
        elif 'open stackoverflow' in data:
            speak("opening stackoverflow")
            webbrowser.open("stackoverflow.com")
        elif 'open spotify' in data:
            speak("opening spotify")
            webbrowser.open("spotify.com")
        elif 'open whatsapp' in data:
            speak("opening whatsapp")
            loc = "C:\\Users\\jaspr\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(loc)
        elif 'play music' in data:
            speak("opening music")
            webbrowser.open("spotify.com")
        elif 'play music' in data:
            speak("opening music")
            webbrowser.open("spotify.com")
        elif 'local disk d' in data:
            speak("opening local disk D")
            webbrowser.open("D://")
        elif 'local disk c' in data:
            speak("opening local disk C")
            webbrowser.open("C://")
        elif 'local disk e' in data:
            speak("opening local disk E")
            webbrowser.open("E://")
        elif 'joke' in data:
            speak("Opening joke")
            joke_1=pyjokes.get_joke(language="en",category="netural")
            print(joke_1)
        elif 'notepad' in data:
            speak("Opening Notepad")
            webbrowser.open("Notepad://")
        elif 'now time' in data:
            speak("Current Time is")
            time=datetime.datetime.now()
            print(time)
        elif 'exit' in data:
            speak("Thank you...")
            break
        
