import speech_recognition as sr
from deep_translator import GoogleTranslator


def Listen(listenFor=7):
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, 0, listenFor) # 8 in listen() specifies the no. of seconds to listen for

    try: 
        print("Recognizing...")
        query = r.recognize_google(audio, language = "ta") # ta for tamil

    except:
        return ""

    query = str(query).lower()
    return query


def Translate(text):
    line = str(text)
    result = GoogleTranslator(source='ta', target='en').translate(line)
    # data = result.text
    print(f"Translated Data: {result}")
    return result

# Translate("How are you")

def ListenAndTranslate(listenFor=7):
    query = Listen(listenFor)
    data = Translate(query)
    return data


# ListenAndTranslate()