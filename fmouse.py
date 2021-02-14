import pyautogui
import speech_recognition as sr
from win32com.client import Dispatch
import pyaudio
s=Dispatch("SAPI.SpVoice")
line1='use mouse events by voice'
print(line1);s.speak(line1)
r=sr.Recognizer()
r1=sr.Recognizer()
r2=sr.Recognizer()
r3=sr.Recognizer()
r4=sr.Recognizer()
while True:
    with sr.Microphone() as source:
            audio=r3.listen(source)
            while True:
                if 'click on link one' in r2.recognize_google(audio):
                    print('click on link on')
                    site=("clicking....")
                    print(site,s.speak(site))
                    pyautogui.moveTo(x=891, y=589)
                    pyautogui.click(button='left',x=866, y=392)
                    print("mouse click is done")
                    s.speak("mouse click is done")
                break
            while True:
                if 'scroll down' in r2.recognize_google(audio):
                    print('scroll down')
                    site=("scrolling down....")
                    print(site,s.speak(site))
                    pyautogui.moveTo(x=891, y=589)
                    pyautogui.vscroll(-200,x=866, y=392)
                    print("scrolling is done")
                    s.speak("scrolling is done")
                break
            while True:
                if 'scroll upward' in r2.recognize_google(audio):
                    print('scroll upward')
                    site=("scrolling upward....")
                    print(site,s.speak(site))
                    pyautogui.moveTo(x=891, y=589)
                    pyautogui.vscroll(200,x=866, y=392)
                    print("scrolling is done")
                    s.speak("scrolling is done")
                break
            while True:
                if 'scroll at the top' in r2.recognize_google(audio):
                    print('scroll top')
                    site=("scrolling top....")
                    print(site,s.speak(site))
                    pyautogui.moveTo(x=891, y=589)
                    pyautogui.vscroll(20000,x=866, y=392)
                    print("scrolling is done")
                    s.speak("scrolling is done")
                break
            while True:
                if 'scroll at the bottom' in r2.recognize_google(audio):
                    print('scroll bottom')
                    site=("scrolling bottom....")
                    print(site,s.speak(site))
                    pyautogui.moveTo(x=891,y=589)
                    pyautogui.vscroll(-20000,x=866, y=392)
                    print("scrolling is done")
                    s.speak("scrolling is done")
                break
            while True:
                if 'move left' in r2.recognize_google(audio):
                    print('move left')
                    site=("moving left....")
                    print(site,s.speak(site))
                    pyautogui.moveTo(x=891,y=589)
                    pyautogui.move(-280,0)
                    print("cursor position moved to left")
                    s.speak("cursor position moved to left")
                break
            while True:
                if 'move right' in r2.recognize_google(audio):
                    print('move right')
                    site=("moving right....")
                    print(site,s.speak(site))
                    pyautogui.moveTo(x=891,y=589)
                    pyautogui.move(280,0)
                    print("cursor position moved to right")
                    s.speak("cursor position moved to right")
                break
            while True:
                if 'clear search bar' in r2.recognize_google(audio):
                    pyautogui.moveTo(x=910, y=124)
                    pyautogui.click(button='left',x=910, y=124)
                    pyautogui.hotkey('ctrl','a')
                    pyautogui.press('backspace')
                    print("cleared the searched bar")
                    s.speak("cleared the searched bar")
                break
            while True:
                if 'write in search bar' in r2.recognize_google(audio):
                    print("write in search bar")
                    print("tell me what you want to write in search bar")
                    s.speak("tell me what you want to write in search bar")
                    with sr.Microphone() as source:
                        Audio=r2.listen(source)
                        print("ok")
                        s.speak("ok")
                        text=r.recognize_google(Audio,language='en')
                        get=r2.recognize_google(Audio)
                        pyautogui.moveTo(x=910, y=124)
                        pyautogui.click(button='left',x=910, y=124)
                        pyautogui.typewrite(text)
                        pyautogui.press('enter')
                        print("written and searched")
                        s.speak("written and searched")
                break
            if 'exit' in r2.recognize_google(audio):
                break
