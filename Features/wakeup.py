import speech_recognition as sr
import subprocess, sys

def Listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, 0, 8) # 8 in listen() specifies the no. of seconds to listen for

    try: 
        print("Recognizing...")
        query = r.recognize_google(audio, language = "en")

    except:
        return ""

    query = str(query).lower()
    return query

def Wakeup():
    query = Listen().lower()

    if "wake up" in query:
        print(sys.platform)
        opener = "python3"
        subprocess.call([opener, "main.py"])
    else:
        pass


while True:
    Wakeup()


