import speech_recognition as sr

condition = True

while condition:
        r = sr.Recognizer()
        with sr.Microphone() as source:
                print ('Say Something!')
                audio = r.listen(source)

        text = r.recognize_google(audio)
        print (text)
        if text == 'bye':
            condition = False
                