from Body.speak import Speak
from Body.listen import ListenAndSpeak
from Brain.brain import ReplyBrain
from Features.clap import Tester

print("Starting Jarvis...Please wait...")
def MainExe():
    print("Executing Main exe")
    Speak("Hello sir ! Hope you have a Good day. I'm ready to help you.... ")

    while True:
        query = str(ListenAndSpeak())
        if len(query) >= 3:
            reply = ReplyBrain(query)
            Speak(reply)
        elif("turn on the tv" in query):
            Speak("Turning on the tv sir...")

def ClapDetector():
    query = Tester()
    if "True-Mic" in query:
        print("")
        print("Clap detected")
        print("")
        MainExe()
    else:
        pass

ClapDetector()