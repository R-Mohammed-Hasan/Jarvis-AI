import os
import keyboard
import pyautogui
import webbrowser
from time import sleep

def OpenExe(query):
    query = str(query).lower()

    if "visit" in query or "launch" in query:
        nameOfWeb = query.replace("visit ", "")
        nameOfWeb = nameOfWeb.replace("launch ", "")
        link = f"https://www.{nameOfWeb}.com"
        webbrowser.open(link)
        return True

    elif "open" in query:
        nameOfApp = query.replace("open ", "")
        pyautogui.hotkey('command','shift')
        pyautogui.hotkey('command','space')
        sleep(1)
        pyautogui.write(nameOfApp, interval=0.1)
        sleep(1)
        pyautogui.press('enter')
        sleep(0.5)
        return True
    
    elif "start" in query: 
        nameOfApp = query.replace("start ", "")




# print(pyautogui.KEY_NAMES)    for list of keys options present

OpenExe("open vs code") 
