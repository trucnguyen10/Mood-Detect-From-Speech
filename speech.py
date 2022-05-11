from regex import P
import speech_recognition as sr
from textblob import TextBlob
import webbrowser
import time
from flask import Flask, render_template, url_for, request, redirect
import os

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Tell me about your day, we're here to listen to you :")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("This is your day : {}".format(text))
    except:
        print("Sorry could not recognize what you said, can you try again?")

blob = TextBlob(text)
sentiment = blob.sentiment.polarity
print(sentiment)

mood = ""

if sentiment >= 0.5:
    mood = "Glad to hear that you had a great day. Keep it up !!"
if sentiment <= 0.5 and sentiment >= 0.0:
    mood = "Even when nothing much happened, you are growing to become a better version of yourself!"
if sentiment <= 0.0:
    mood = "Everyone has bad day. Keep going and enjoy your life!"


html_content = f"<html> <head> <p>  {text} </p> <h2> {mood} </h2> </head> <body> </body> </html>"
with open("index.html", "w") as html_file:
    html_file.write(html_content)
    print("html file created successfully !!")
webbrowser.open_new_tab("index.html")
