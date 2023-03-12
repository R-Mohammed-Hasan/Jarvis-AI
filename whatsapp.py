from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os
from time import sleep
from selenium import webdriver
import pandas as pd
from Body.listen import ListenAndTranslate
from Body.speak import Speak
import pathlib

scriptDirectory = pathlib.Path().absolute()

# options = Options()
# options.add_experimental_option("excludeSwitches", ["enable-logging"])
# options.add_argument("--profile-directory=Default")
# options.add_argument(f"user-data-dir={scriptDirectory}\\userdata")
# os.system("")
# os.environ["WDM_LOG_LEVEL"] = "0"
# PathofDriver = "Database/chromedriver"
# driver = webdriver.Chrome(PathofDriver,options=options)
# driver.maximize_window()
# driver.get("https://web.whatsapp.com/")

ListWeb = {'mom' : "+919566062344",
           'mam' : "+919566062344",
            'dost': "+91",
            "gf": '+91'}

# sleep(10)

def WhatsappMessageSender(prefix=""):
    Speak(f"{prefix} Whom do you want to send message sir")
    Name = str(ListenAndTranslate(5))
    if len(Name) < 2:
        WhatsappMessageSender("Sorry I did'nt get you")
    options = Options()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_argument("--profile-directory=Default")
    # options.headless = True  uncomment this if u need to send message in BG
    options.add_argument(f"user-data-dir={scriptDirectory}\\userdata")
    os.system("")
    os.environ["WDM_LOG_LEVEL"] = "0"
    PathofDriver = "Database/chromedriver"
    driver = webdriver.Chrome(PathofDriver,options=options)
    driver.maximize_window()
    driver.get("https://web.whatsapp.com/")

    Speak("Initializing Whatsapp ")
    Speak(f"Preparing To Send a Message To {Name}")
    Speak("What's The Message By The Way?")
    Message = ListenAndTranslate()
    print(ListWeb['mom'])
    Number = ListWeb['mom']
    LinkWeb = 'https://web.whatsapp.com/send?phone=' + Number + "&text=" + Message
    driver.get(LinkWeb)
    sleep(5)
    try:
        driver.find_element(by=By.XPATH,value='/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button').click()
        Speak("Message Sent")
        
    except:
        Speak("Message sending falied")
