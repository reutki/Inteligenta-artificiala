import time

import pyautogui
import requests
from bs4 import BeautifulSoup

def vizionari_video():
    vizionari = pyautogui.locateOnScreen(r'C:\Users\marcu\Desktop\Facultate\AI\vizionari.png', confidence=0.5)
    pyautogui.click(vizionari)
    time.sleep(2)
    print('opened profile')

def cautare_search():
     if pyautogui.locateOnScreen(r'C:\Users\marcu\Desktop\Facultate\AI\search.png',confidence=0.7) !=None:
        camp_google= pyautogui.locateOnScreen(r'C:\Users\marcu\Desktop\Facultate\AI\search.png',confidence=0.7)
        pyautogui.click(camp_google)
        time.sleep(3)
        pyautogui.write('www.youtube.com')
        pyautogui.press('enter')
        print('found search on screen')
        time.sleep(3)
     else:
        print('no search on screen')
     if pyautogui.locateOnScreen(r'C:\Users\marcu\Desktop\Facultate\AI\search_youtube.png',confidence=0.7) !=None:
        camp_youtube= pyautogui.locateOnScreen(r'C:\Users\marcu\Desktop\Facultate\AI\search_youtube.png',confidence=0.7)
        pyautogui.click(camp_youtube)
        time.sleep(2)
        pyautogui.write('zona it')
        pyautogui.press('enter')
        print('found youtube search on screen')
        time.sleep(2)
     else:
         print('no youtube search')
     if pyautogui.locateOnScreen(r'C:\Users\marcu\Desktop\Facultate\AI\zona_profile.png',confidence=0.7) !=None:
        profile = pyautogui.locateOnScreen(r'C:\Users\marcu\Desktop\Facultate\AI\zona_profile.png', confidence=0.7)
        pyautogui.click(profile)
        time.sleep(2)
        print('opened profile')
        # pyautogui.scroll(-350)
        # time.sleep(3)
        # pyautogui.click(x = 904, y = 798)
        # time.sleep(3)
        # backClick()
        # pyautogui.click(x=1207, y=809)
        # time.sleep(3)
        # backClick()
     else:
         print('no profile found')


     views()

waitingTime = 3
scroll = -350
xCoord = 651
yCoord = 431
def views():
    videoSection = pyautogui.locateOnScreen(r'C:\Users\marcu\Desktop\Facultate\AI\section.png', confidence=0.7)
    pyautogui.click(videoSection)
    time.sleep(2)
    pyautogui.scroll(scroll)
    # time.sleep(2)
    # pyautogui.click(x=xCoord, y=yCoord)
    # time.sleep(6)
    # backClick()
    # time.sleep(2)
    # pyautogui.scroll(scroll)
    # pyautogui.click(x=xCoord+100, y=yCoord)
    # time.sleep(6)
    # backClick()
    #  if pyautogui.locateOnScreen(r'C:\Users\marcu\Desktop\Facultate\AI\subscribe.png',confidence=0.7) !=None:
    #     subscribe = pyautogui.locateOnScreen(r'C:\Users\marcu\Desktop\Facultate\AI\subscribe.png', confidence=0.7)
    #     pyautogui.click(subscribe)
    #     time.sleep(3)
    #     print('subscribed')
    #     time.sleep(5)
    #  else:
    #      print('no subscribe button')
# def mouseCoordinates():
#     time.sleep(2)
#     pyautogui.scroll(-350)
#     print(pyautogui.position())
time.sleep(2)
vizionari_video()
def backClick():
    if pyautogui.locateOnScreen(r'C:\Users\marcu\Desktop\Facultate\AI\back.png', confidence=0.7) != None:
            back = pyautogui.locateOnScreen(r'C:\Users\marcu\Desktop\Facultate\AI\back.png', confidence=0.7)
            pyautogui.click(back)
            time.sleep(2)


time.sleep(2)
cautare_search()
