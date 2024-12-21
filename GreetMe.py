import pyttsx3
import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[3].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    hour = int(datetime.datetime.noe().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning, Boss")
    elif hour>12 and hour<=18:
        speak("Good Afternoon, Boss")
    else:
        speak("Good Evening, Boss")

    speak("Any work for me ?")