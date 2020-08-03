#This is a voice Ai
#Author-Pranab Kr. Nath

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib


engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')

#print(voices[0].id)
engine.setProperty("voice", voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning")

    elif hour>=12 and hour<18:
        speak("Good afternoon")
    else:
        speak("Good Evening")
    speak("i am jesica sir, please tell me how may i help you?")

def takeCommand():
    #it take microphone input and return string output


    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)

        print("Say again please...!!")
        return "None"
    return query


def sendEmail(to,content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("#yourMail@gmail.com", "#password")
    server.sendmail("yourMail@gmail.com",to,content)
    server.close()



if __name__ == '__main__':
    #speak("Pranab is a photographer")
    wishme()
    while True:

        query=takeCommand().lower()

        if "wikipedia" in query:
            speak("Searching in Wiki...")
            results=wikipedia.summary(query, sentences=2)
            speak("According to wiki ")
            print(results)
            speak(results)

        elif "open youtube" in query:
            speak("opening youtube..")
            webbrowser.open("Youtube.com")

        elif "open google" in query:
            speak("opening google..")
            webbrowser.open("Google.com")

        elif "stackoverflow" in query:
            speak("opening stackoverflow..")
            webbrowser.open("stackoverflow.com")

        elif "play music" in query:
            music_dir = "D:\\SONGS\\MP3\\Bollywood Unwind - Romantic Classics _5b2015-MP3-320Kbps_5d-(FrkMusic.Info)"
            songs = os.listdir(music_dir)
            #print(songs,"\n")

        elif "play song" in query:
            music_dir = "D:\\SONGS\\MP3\\Bollywood Unwind - Romantic Classics _5b2015-MP3-320Kbps_5d-(FrkMusic.Info)"
            songs = os.listdir(music_dir)
            #print(songs,"\n")

            os.startfile(os.path.join(music_dir, random.choice(songs)))

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, The time is{strTime} now")

        elif "send email to pranav" in query:
            try:
                speak("what should i say?")
                content = takeCommand()
                to = "krprana99@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!") 
            except Exception as e:
                #print(e)
                speak("Sorry sir, i'm not able to send th email")
