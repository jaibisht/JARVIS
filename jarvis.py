#Imports
import os
import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen

#Setting up engine

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Defining Speak command
def speak(audio):
	engine.say(audio)
	engine.runAndWait()

# Wish me
def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour>= 0 and hour<12:
		speak("Good Morning Sir !")

	elif hour>= 12 and hour<18:
		speak("Good Afternoon Sir !") 

	else:
		speak("Good Evening Sir !") 

	assname =("Jarvis")
	speak("I am your Assistant")
	speak(assname)
	
# User's Name
def username():
	speak("What should i call you sir")
	uname = takeCommand()
	speak("Welcome Mister")
	speak(uname)
	columns = shutil.get_terminal_size().columns
	
	print("#####################".center(columns))
	print("Welcome Mr.", uname.center(columns))
	print("#####################".center(columns))
	
	speak("How can i Help you, Sir")

# Listening Status
def takeCommand():
	
	r = sr.Recognizer()
	
	with sr.Microphone() as source:
		
		print("Listening...")
		r.pause_threshold = 1
		audio = r.listen(source)

	try:
		print("Recognizing...") 
		query = r.recognize_google(audio, language ='en-in')
		print(f"User said: {query}\n")

	except Exception as e:
		print(e) 
		print("Unable to Recognize your voice.") 
		return "None"
	
	return query

#Send Email 
def sendEmail(to, subject, content):
    server = smtplib.SMTP('smtp-mail.outlook.com', 587)
    server.ehlo()
    server.starttls()

    server.login('your_email@outlook.com', 'your_password')
    message = f"Subject: {subject}\n\n{content}"
    
    server.sendmail('your_email@outlook.com', to, message)
    server.close()

if __name__ == '__main__':
	clear = lambda: os.system('cls')
	
	# This Function will clean any
	# command before execution of this python file
	clear()
	wishMe()
	username()

	while True:
		
		query = takeCommand().lower()
		
		# All the commands said by user will be 
		# stored here in 'query' and will be
		# converted to lower case for easily 
		# recognition of command

# Open Wikipedia
		if 'wikipedia' in query:
			speak('Opening Wikipedia\n')
			webbrowser.open("wikipedia.org")

# Open Youtube
		elif 'open youtube' in query:
			speak("Opening Youtube\n")
			webbrowser.open("youtube.com")

# Open Google
		elif 'open google' in query:
			speak("Opening Google\n")
			webbrowser.open("google.com")

# Open Stackoverflow
		elif 'open stackoverflow' in query:
			speak("Opening Stackoverflow\n")
			webbrowser.open("stackoverflow.com") 

# Time
		elif 'time' in query or 'what is the time' in query:
			strTime = datetime.datetime.now().strftime("%H:%M:%S")
			speak(f"Sir, the time is {strTime}")

# Send a mail
		elif 'send a mail' in query:
			try:
				speak("Please fill the data")
				subject = input("Enter subject: ")
				content = input("Enter content: ")
				to = input("Receiver email address: ")
				sendEmail(to, subject, content)  # Pass subject and content to the function
				speak("Email has been sent !")
			except Exception as e:
				print(e)
				speak("I am not able to send this email")

# Joke
		elif 'joke' in query or 'tell me a joke' in query:
			speak(pyjokes.get_joke())

# Exit
		elif 'exit' in query:
			speak("Thanks for giving me your time")
			exit()

