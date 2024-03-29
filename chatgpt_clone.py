import pyttsx3
import webbrowser
import datetime
import smtplib
import shutil
import pyjokes

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    """Function to convert text to speech"""
    engine.say(text)
    engine.runAndWait()

# Global variable to store the username
uname = ""

#Send Email 
def sendEmail(to, subject, content):
    server = smtplib.SMTP('smtp-mail.outlook.com', 587)
    server.ehlo()
    server.starttls()

    server.login('your_email@outlook.com', 'your_password')
    message = f"Subject: {subject}\n\n{content}"
    
    server.sendmail('your_email@outlook.com', to, message)
    server.close()

# Wish me
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning Sir ! I am your personal Assistant")

    elif hour>= 12 and hour<18:
        speak("Good Afternoon Sir ! I am your personal Assistant") 

    else:
        speak("Good Evening Sir ! I am your personal Assistant") 

# User's Name
def username():
    speak("What should I call you?")
    global uname
    uname = input("Enter your name: ")
    speak(f"Welcome Mister {uname}")
    columns = shutil.get_terminal_size().columns
    
    print("###############################################################".center(columns))
    print(f"Welcome Mr. {uname}".center(columns))
    print("###############################################################".center(columns))
    
    speak("How can I help you today?")

wishMe()
username()

# Assistant logic
def process_command(command):
    global uname
    # Hello
    if command == 'hello' or command == 'hi':
        speak('Hello! How can I help you?')

    # Time
    elif 'time' in command or 'what is the time' in command:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, the time is {strTime}")

    # Web Browser --> websites
    elif 'open wikipedia' in command or 'wikipedia' in command:
        speak('Opening Wikipedia')
        webbrowser.open("https://en.wikipedia.org")

    elif 'open youtube' in command or 'youtube' in command:
        speak('Opening Youtube')
        webbrowser.open("https://www.youtube.com")

    elif 'open google' in command or 'google' in command:
        speak('Opening Google')
        webbrowser.open("https://www.google.com")

    elif 'open stackoverflow' in command or 'stackoverflow' in command:
        speak('Opening Stackoverflow')
        webbrowser.open("https://stackoverflow.com")

    # Send Email
    elif 'send email' in command or 'send mail' in command:
        try:
            speak("Please fill the data")
            subject = input("Enter subject: ")
            content = input("Enter content: ")
            to = input("Receiver email address: ")   
            sendEmail(to, subject, content)  # Pass subject and content to the function
            speak("Email has been sent !")
        except Exception as e:
            print(e)
            speak("Sorry, I am not able to send this email")

    # Joke
    elif 'joke' in command or 'tell me a joke' in command:
        speak("Hope you like this one sir.")
        print(pyjokes.get_joke())

    # Exit
    elif 'exit' in command:
        speak(f"Have a nice day, Mister {uname}")
        exit()

# Main loop to get user input and process commands
while True:
    user_input = input("Type your command: ")
    process_command(user_input.lower())  # Convert user input to lowercase for case-insensitive matching
