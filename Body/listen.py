import speech_recognition as sr
# from googletrans import Translator
from deep_translator import GoogleTranslator


def Listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, 0, 8) # 8 in listen() specifies the no. of seconds to listen for

    try: 
        print("Recognizing...")
        query = r.recognize_google(audio, language = "ta") # ta for tamil

    except:
        return ""

    query = str(query).lower()
    return query

# print(Listen())


def Translate(text):
    line = str(text)
    # translator = Translator()
    # result = translator.translate(line, "en")
    result = GoogleTranslator(source='auto', target='en').translate(line)
    # data = result.text
    print(f"Data: {result}")
    return result

# Translate("How are you")

def ListenAndSpeak():
    query = Listen()
    data = Translate(query)
    print("data listened and transalted " + data)
    return data


# ListenAndSpeak()