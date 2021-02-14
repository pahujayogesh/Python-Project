def main():
    import speech_recognition as sr
    from win32com.client import Dispatch
    import webbrowser as wb
    import pyaudio
    s=Dispatch("SAPI.SpVoice")
    r=sr.Recognizer()
    r1=sr.Recognizer()
    r2=sr.Recognizer()
    r3=sr.Recognizer()
    r4=sr.Recognizer()
    with sr.Microphone() as source:
        line1='where do you want to search:'
        print(line1)
        s.speak(line1)
        line2='search here with your voice input'
        print(line2)
        s.speak(line2)
        line3 = "Or say show website to see website names"
        print(line3)
        s.speak(line3)
        line4='and add feedback or comment about this program by giving voice input as respond'
        print(line4)
        s.speak(line4)
        audio=r3.listen(source)
        if 'show website' in r2.recognize_google(audio):
            site=("showing websites name:")
            print(site,s.speak(site))
            import interface
        elif 'YouTube' in r2.recognize_google(audio):
            print("YouTube")
            r2=sr.Recognizer()
            url='https://www.youtube.com/results?search_query='
            with sr.Microphone() as source:
                A=("Tell me what to search")
                print("Tell me what to search",s.Speak(A))
                Audio=r2.listen(source)
                with sr.Microphone() as source:
                    a=("choose your language")
                    print("choose your language",s.Speak(a))
                    audio=r.listen(source)
                    s.Speak("OK")
                try:
                    if 'Hindi' in r.recognize_google(audio):
                        text=r.recognize_google(Audio,language='hi-IN')
                        get=r2.recognize_google(Audio)
                        print("यूट्यूब पर आपकी खोज है:",text)
                    else:
                        'english' in r.recognize_google(audio)
                        text=r.recognize_google(Audio,language='en')
                        get=r2.recognize_google(Audio)
                        print("your search on YouTube is:",text)
                        s.Speak(text,s.Speak("your search on YouTube is:"))
                    wb.get().open_new(url+get)
                except sr.UnknownValueError:
                    print('error')
                except sr.RequestError as e:
                    print('failed'.format(e))
                with sr.Microphone() as source:
                    yn=('Do you want to use mouse events on your searched youtube page:')
                    print(yn,s.speak(yn))
                    audio=r3.listen(source)
                    if 'yes' in r4.recognize_google(audio):
                        print("yes")
                        import m1
                    elif 'no' in r4.recognize_google(audio):
                        print("no")
                        main()
        elif 'Google' in r2.recognize_google(audio):
            print("Google")
            r2=sr.Recognizer()
            url='https://www.google.com/search?q='
            with sr.Microphone() as source:
                A=("Tell me what to search")
                print("Tell me what to search",s.Speak(A))
                Audio=r2.listen(source)
                with sr.Microphone() as source:
                    a=("choose your language")
                    print("choose your language",s.Speak(a))
                    audio=r.listen(source)
                    s.Speak("OK")
                try:
                    if 'Hindi' in r.recognize_google(audio):
                        text=r.recognize_google(Audio,language='hi-IN')
                        get=r2.recognize_google(Audio)
                        print("गूगल पर आपकी खोज है:",text)
                    else:
                        'english' in r.recognize_google(audio)
                        text=r.recognize_google(Audio,language='en')
                        get=r2.recognize_google(Audio)
                        print("your search on google is:",text)
                        s.Speak(text,s.Speak("your search on Google is:"))
                    wb.get().open_new(url+get)
                except sr.UnknownValueError:
                    print('error')
                except sr.RequestError as e:
                    print('failed'.format(e))
        elif 'gana' in r2.recognize_google(audio):
            print("Gaana")
            r2=sr.Recognizer()
            url='https://gaana.com/search/'
            with sr.Microphone() as source:
                A=("Tell me what to search")
                print("Tell me what to search",s.Speak(A))
                Audio=r2.listen(source)
                with sr.Microphone() as source:
                    a=("choose your language")
                    print("choose your language",s.Speak(a))
                    audio=r.listen(source)
                    s.Speak("OK")
                try:
                    if 'Hindi' in r.recognize_google(audio):
                        text=r.recognize_google(Audio,language='hi-IN')
                        get=r2.recognize_google(Audio)
                        print("गाना पर आपकी खोज है:",text)
                    else:
                        'english' in r.recognize_google(audio)
                        text=r.recognize_google(Audio,language='en')
                        get=r2.recognize_google(Audio)
                        print("your search on Gaana.com is:",text)
                        s.Speak(text,s.Speak("your search on Gaana is:"))
                    wb.get().open_new(url+get)
                except sr.UnknownValueError:
                    print('error')
                except sr.RequestError as e:
                    print('failed'.format(e))
        elif 'SoundCloud' in r2.recognize_google(audio):
            print("soundcloud")
            r2=sr.Recognizer()
            url='https://soundcloud.com/search?q='
            with sr.Microphone() as source:
                A=("Tell me what to search")
                print("Tell me what to search",s.Speak(A))
                Audio=r2.listen(source)
                with sr.Microphone() as source:
                    a=("choose your language")
                    print("choose your language",s.Speak(a))
                    audio=r.listen(source)
                    s.Speak("OK")
                try:
                    if 'Hindi' in r.recognize_google(audio):
                        text=r.recognize_google(Audio,language='hi-IN')
                        get=r2.recognize_google(Audio)
                        print("साउंड क्लाउड पर आपकी खोज है:",text)
                    else:
                        'english' in r.recognize_google(audio)
                        text=r.recognize_google(Audio,language='en')
                        get=r2.recognize_google(Audio)
                        print("your search on SoundCloud is:",text)
                        s.Speak(text,s.Speak("your search on Soundcloud is:"))
                    wb.get().open_new(url+get)
                except sr.UnknownValueError:
                    print('error')
                except sr.RequestError as e:
                    print('failed'.format(e))
        elif 'Facebook' in r2.recognize_google(audio):
            print("facebook")
            r2=sr.Recognizer()
            url='https://www.google.com/search?q=site%3Afacebook.com+'
            with sr.Microphone() as source:
                A=("Tell me what to search")
                print("Tell me what to search",s.Speak(A))
                Audio=r2.listen(source)
                with sr.Microphone() as source:
                    a=("choose your language")
                    print("choose your language",s.Speak(a))
                    audio=r.listen(source)
                    s.Speak("OK")
                try:
                    if 'Hindi' in r.recognize_google(audio):
                        text=r.recognize_google(Audio,language='hi-IN')
                        get=r2.recognize_google(Audio)
                        print("फेसबुक पर आपकी खोज है:",text)
                    else:
                        'english' in r.recognize_google(audio)
                        text=r.recognize_google(Audio,language='en')
                        get=r2.recognize_google(Audio)
                        print("your search on Facebook is:",text)
                        s.Speak(text,s.Speak("your search on Facebook is:"))
                        
                    wb.get().open_new(url+get)
                except sr.UnknownValueError:
                    print('error')
                except sr.RequestError as e:
                    print('failed'.format(e))
        elif 'Flipkart' in r2.recognize_google(audio):
            print("Flipkart")
            r2=sr.Recognizer()
            url='https://www.flipkart.com/search?q='
            with sr.Microphone() as source:
                A=("Tell me what to search")
                print("Tell me what to search",s.Speak(A))
                Audio=r2.listen(source)
                with sr.Microphone() as source:
                    a=("choose your language")
                    print("choose your language",s.Speak(a))
                    audio=r.listen(source)
                    s.Speak("OK")
                try:
                    if 'Hindi' in r.recognize_google(audio):
                        text=r.recognize_google(Audio,language='hi-IN')
                        get=r2.recognize_google(Audio)
                        print("फ्लिपकार्ट पर आपकी खोज है:",text)
                    else:
                        'english' in r.recognize_google(audio)
                        text=r.recognize_google(Audio,language='en')
                        get=r2.recognize_google(Audio)
                        print("your search on FlipKart is:",text)
                        s.Speak(text,s.Speak("your search on Flipkart is:"))
                    wb.get().open_new(url+get)
                except sr.UnknownValueError:
                    print('error')
                except sr.RequestError as e:
                    print('failed'.format(e))
                with sr.Microphone() as source:
                    yn=('Do you want to use mouse events on your search flipkart page:')
                    print(yn,s.speak(yn))
                    audio=r3.listen(source)
                    if 'yes' in r4.recognize_google(audio):
                        print("yes")
                        import fmouse
                    elif 'no' in r4.recognize_google(audio):
                        print("no")
                        main()
        elif 'Amazon' in r2.recognize_google(audio):
            print("Amazon")
            r2=sr.Recognizer()
            url='https://www.amazon.in/s?k='
            with sr.Microphone() as source:
                A=("Tell me what to search")
                print("Tell me what to search",s.Speak(A))
                Audio=r2.listen(source)
                with sr.Microphone() as source:
                    a=("choose your language")
                    print("choose your language",s.Speak(a))
                    audio=r.listen(source)
                    s.Speak("OK")
                try:
                    if 'Hindi' in r.recognize_google(audio):
                        text=r.recognize_google(Audio,language='hi-IN')
                        get=r2.recognize_google(Audio)
                        print("अमीजोन पर आपकी खोज है:",text)
                    else:
                        'english' in r.recognize_google(audio)
                        text=r.recognize_google(Audio,language='en')
                        get=r2.recognize_google(Audio)
                        print("your search on Amazon is:",text)
                        s.Speak(text,s.Speak("your search on amazon is:"))
                    wb.get().open_new(url+get)
                except sr.UnknownValueError:
                    print('error')
                except sr.RequestError as e:
                    print('failed'.format(e))
                with sr.Microphone() as source:
                    yn=('Do you want to use mouse events on your searched amazon page:')
                    print(yn,s.speak(yn))
                    audio=r3.listen(source)
                    if 'yes' in r4.recognize_google(audio):
                        print("yes")
                        import amouse
                    elif 'no' in r4.recognize_google(audio):
                        print("no")
                        main()
        elif 'respond' in r2.recognize_google(audio):
            print("Respond")
            import sendmail
        with sr.Microphone() as source:
            yn=('Do you want to run again:')
            print(yn,s.speak(yn))
            audio=r3.listen(source)
            if 'yes' in r4.recognize_google(audio):
                print("yes")
                main()
            elif 'no' in r4.recognize_google(audio):
                print("no")
                exit()
            else:
                main()
main()
