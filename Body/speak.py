# import pyttsx3

# def Speak(text):
#     engine = pyttsx3.init()
#     voices = engine.getProperty("voices")
#     engine.setProperty("voices", voices[1].id)
#     engine.setProperty("rate",170)
#     engine.say(text)
#     engine.runAndWait()

# Speak("Hello")

# selenium==4.1.3
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

chrome_options = Options()
chrome_options.add_argument('--log-level=3')
chrome_options.headless = True
Path = "Database/chromedriver"
driver = webdriver.Chrome(Path, options = chrome_options)
driver.maximize_window()


website = r"https://ttsmp3.com/text-to-speech/British%20English/"
driver.get(website)
ButtonSelection = Select(driver.find_element(by=By.XPATH, value = '/html/body/div[4]/div[2]/form/select'))
ButtonSelection.select_by_visible_text('British English / Brian')


def Speak(text):
    lengthOfText = len(str(text))
    if(lengthOfText == 0):
        pass
    else:
        print("")
        print(f"Jarvis : {text}")
        print("")
        Data = str(text)
        xpathOfSec = '/html/body/div[4]/div[2]/form/textarea'
        driver.find_element(By.XPATH, value = xpathOfSec).send_keys(Data)
        driver.find_element(By.XPATH, value = '//*[@id="vorlesenbutton"]').click()
        driver.find_element(By.XPATH, value = '/html/body/div[4]/div[2]/form/textarea').clear()

        if(lengthOfText >= 30):
            sleep(5)
        elif(lengthOfText>=40):
            sleep(6)
        elif(lengthOfText>=55):
            sleep(8)
        elif(lengthOfText>=70):
            sleep(10)
        elif(lengthOfText>=100):
            sleep(13)
        elif(lengthOfText>=120):
            sleep(15)
        else:
            sleep(2)



# Speak("Hello buddy")
