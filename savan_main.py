import pyttsx3
import speech_recognition

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def tackCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("understanding...")
        query = r.recognize_google_cloud(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query
if __name__ == "__main__":
    while True:
        query = tackCommand().lower()
        if "hello" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = tackCommand().lower()
                if "go to sleep" in query:
                    speak("Ok Boss, You can call me anytime")
                    break

                elif "Hello" in query:
                    speak("Hello Boss. How are you ?")
                
                elif "Who is Sawan ?":
                    speak("Savan is your begam")
                
                elif "Who is jay ?":
                    speak("he is your second begam")
                
                elif "Who is Bhupen ?":
                    speak("He is my Master and Creator, and He is the Hasban of two wives")