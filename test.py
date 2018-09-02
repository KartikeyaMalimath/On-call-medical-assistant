import random
from six.moves import input
from gtts import gTTS
import os
language = 'en'
import speech_recognition as sr

from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('Test')

conv = open('training.txt', 'r').readlines()

bot.set_trainer(ListTrainer)

bot.train(conv)


#training data

greetings = ['hola', 'hello', 'hi', 'hi', 'hey!','hey']
greetingReply = ['welcome to Med call, please tell your main symptom']

question = ['how are you','how are you doing']
responses = ['Okay',"I'm fine"]

symptoms = ['i have headache','i have fever',]
responses2 = ['from how many days?']
headache = ['headache']
fever = ['fever']
stomach = ['stomach ache']
vomiting = [' vomiting']
sour = ['sour throat']
bodyache = ['bodyache']
breathing = ['breathing problem']
loose = ['loose motion']
indigestion = ['indigestion']
user1 = ['headache', 'fever', 'stomach ache','burning eyes', ' vomiting',' bleeding nose','sour throat',' bodyache',' breathing problem','loose motion','indigestion']
bot1 = ['from how many days?']

user2 = ['cold',' headache',' running nose']
bot2 = ['do you have fever?']

user3 = ['no']
bot3 = ['any other synptoms?']

user4= ['i fainted', 'i am feeling giddy' ]
bot4 = ['were you standing in sun for a long time?']

user5 = ['yes']

user6 = ['i m feeling uneasy','i am feeling uncomfortable','i am not feeling good','i am feeling tired']
bot6 = ['please be more scpecific']

bot7 = ['what is your age?']
bot8 = ['are male or female?']
bot9 = ['what is your weight?']
bot10 = ['do you have cough?']
bot11 = ['do have sour throat?']
bot12 = ['do have headache?']
bot13 = ['are you feeling tired?']
bot14 = ['do you have migrane history?']
bot15 = ['are you having burnig sensations?']
bot16 = ['do you have actidity?']
bot17 = ['do you have vomiting']
bot18 = ['how many hours did you sleep?']
bot19 = ['do you loose motion?']
bot20 = ['do you stomach ache?']
bot21 = ['do you have indigestion?']
bot22 = ['do u have cold?']
bot23 = ['are you working in closed areas?']
bot24 = ['physical stress?']
bot25 = ['ok thank you let is figure out what is going on']
bot26  = ['do you have migrane history?']
bot31 = ['do you have dehydration?']
bot27 = ['do you have dry cough or wet cough?']
user7 = ['dry']
user8 = ['wet']
bot32 = ['did you eat something cold?']
user9 = ['cut','wound']
bot28 = ['old or new cut?']
bot33 = ['any asthma histoty?']
user10 = ['burn']
bot29 = ['old or new burn?']

user11 = ['mouth ulser']

user12 = ['heart pain','chest pain','got fracture', 'i am feeling dizzy']
bot30 = ['please consult a doctor']

#training data end

#function to generate MP3 
def appu (testText) :
    myobj = gTTS(text= testText, lang=language, slow=False)
    myobj.save("test.mp3")

#main

condition = True
flag = True

while condition:
        
        while flag:
            disclaimer = 'Hello'
            myobj = gTTS(text='disclaimer', lang=language, slow=False)
            myobj.save("hello.mp3")
            os.system("mpg321 hello.mp3")
            flag = False

        r = sr.Recognizer()
        with sr.Microphone() as source:
                print ('Say Something!')
                audio = r.listen(source)
        text = r.recognize_google(audio)
        if text == 'bye':
                print ('bye')
                myobj = gTTS(text='bye', lang=language, slow=False)
                myobj.save("bye.mp3")
                os.system("mpg321 bye.mp3")
                condition = False
        elif text in greetings:
                random_greeting = random.choice(greetingReply)
                print(random_greeting)
                appu(random_greeting)
                os.system("mpg321 test.mp3")
        elif text in question:
                random_response = random.choice(responses)
                print(random_response)
                appu (random_response)
                os.system("mpg321 test.mp3")
        elif text in symptoms:
                random_response2 = random.choice(responses2)
                print(random_response2)
                appu (random_response2)
                os.system("mpg321 test.mp3")
        elif text in headache:
                random_response3 =  random.choice(bot1)
                print (random_response3)
                appu(random_response3)
                os.system("mpg321 test.mp3")
                symptom1 = text
                sym = True
                while sym:
                    r = sr.Recognizer()
                    with sr.Microphone() as source:
                            print ('Say symptom!')
                            audio = r.listen(source)
                    days = 0
                    days = r.recognize_google(audio) 

                    
                    if days != 0:
                        if symptom1 == 'headache':
                            symptom2Res = random.choice(bot2)
                            print (symptom2Res)
                            appu (symptom2Res)
                            os.system("mpg321 test.mp3")
                            
                            r = sr.Recognizer()
                            with sr.Microphone() as source:
                                print ('Say symptom!')
                                audio = r.listen(source)
                            symBolean1 = r.recognize_google(audio)

                            
                            symptom2Res = random.choice(bot14)
                            print (symptom2Res)
                            appu (symptom2Res)
                            os.system("mpg321 test.mp3")
                            
                            r = sr.Recognizer()
                            with sr.Microphone() as source:
                                print ('Say symptom!')
                                audio = r.listen(source)
                            symBolean2 = r.recognize_google(audio)

                            symptom2Res = random.choice(bot22)
                            print (symptom2Res)
                            appu (symptom2Res)
                            os.system("mpg321 test.mp3")
                            
                            r = sr.Recognizer()
                            with sr.Microphone() as source:
                                print ('Say symptom!')
                                audio = r.listen(source)
                            symBolean3 = r.recognize_google(audio)
                            sym = False


        elif text in stomach:
                random_response3 =  random.choice(bot1)
                print (random_response3)
                appu(random_response3)
                os.system("mpg321 test.mp3")
                symptom1 = text
                sym = True
                while sym:
                    r = sr.Recognizer()
                    with sr.Microphone() as source:
                            print ('Say symptom!')
                            audio = r.listen(source)
                    days = 0
                    days = r.recognize_google(audio) 

                    
                    if days != 0:
                        if symptom1 == 'stomach ache':
                            symptom2Res = random.choice(bot16)
                            print (symptom2Res)
                            appu (symptom2Res)
                            os.system("mpg321 test.mp3")
                            
                            r = sr.Recognizer()
                            with sr.Microphone() as source:
                                print ('Say symptom!')
                                audio = r.listen(source)
                            symBolean1 = r.recognize_google(audio)

                            
                            symptom2Res = random.choice(bot17)
                            print (symptom2Res)
                            appu (symptom2Res)
                            os.system("mpg321 test.mp3")
                            
                            r = sr.Recognizer()
                            with sr.Microphone() as source:
                                print ('Say symptom!')
                                audio = r.listen(source)
                            symBolean2 = r.recognize_google(audio)

                            symptom2Res = random.choice(bot19)
                            print (symptom2Res)
                            appu (symptom2Res)
                            os.system("mpg321 test.mp3")
                            
                            r = sr.Recognizer()
                            with sr.Microphone() as source:
                                print ('Say symptom!')
                                audio = r.listen(source)
                            symBolean3 = r.recognize_google(audio)
                            sym = False

        elif text in fever:
                random_response3 =  random.choice(bot1)
                print (random_response3)
                appu(random_response3)
                os.system("mpg321 test.mp3")
                symptom1 = text
                sym = True
                while sym:
                    r = sr.Recognizer()
                    with sr.Microphone() as source:
                            print ('Say symptom!')
                            audio = r.listen(source)
                    days = 0
                    days = r.recognize_google(audio) 

                    
                    if days != 0:
                        if symptom1 == 'fever':
                            symptom2Res = random.choice(bot22)
                            print (symptom2Res)
                            appu (symptom2Res)
                            os.system("mpg321 test.mp3")
                            
                            r = sr.Recognizer()
                            with sr.Microphone() as source:
                                print ('Say symptom!')
                                audio = r.listen(source)
                            symBolean1 = r.recognize_google(audio)

                            
                            symptom2Res = random.choice(bot24)
                            print (symptom2Res)
                            appu (symptom2Res)
                            os.system("mpg321 test.mp3")
                            
                            r = sr.Recognizer()
                            with sr.Microphone() as source:
                                print ('Say symptom!')
                                audio = r.listen(source)
                            symBolean2 = r.recognize_google(audio)

                            symptom2Res = random.choice(bot10)
                            print (symptom2Res)
                            appu (symptom2Res)
                            os.system("mpg321 test.mp3")
                            
                            r = sr.Recognizer()
                            with sr.Microphone() as source:
                                print ('Say symptom!')
                                audio = r.listen(source)
                            symBolean3 = r.recognize_google(audio)

                            sym = False  
        elif text in vomiting:
                random_response3 =  random.choice(bot1)
                print (random_response3)
                appu(random_response3)
                os.system("mpg321 test.mp3")
                symptom1 = text
                sym = True
                while sym:
                    r = sr.Recognizer()
                    with sr.Microphone() as source:
                            print ('Say symptom!')
                            audio = r.listen(source)
                    days = 0
                    days = r.recognize_google(audio) 

                    
                    if days != 0:
                        if symptom1 == 'Vomiting':
                            symptom2Res = random.choice(bot2)
                            print (symptom2Res)
                            appu (symptom2Res)
                            os.system("mpg321 test.mp3")
                            
                            r = sr.Recognizer()
                            with sr.Microphone() as source:
                                print ('Say symptom!')
                                audio = r.listen(source)
                            symBolean1 = r.recognize_google(audio)

                            
                            symptom2Res = random.choice(bot20)
                            print (symptom2Res)
                            appu (symptom2Res)
                            os.system("mpg321 test.mp3")
                            
                            r = sr.Recognizer()
                            with sr.Microphone() as source:
                                print ('Say symptom!')
                                audio = r.listen(source)
                            symBolean2 = r.recognize_google(audio)

                            symptom2Res = random.choice(bot21)
                            print (symptom2Res)
                            appu (symptom2Res)
                            os.system("mpg321 test.mp3")
                            
                            r = sr.Recognizer()
                            with sr.Microphone() as source:
                                print ('Say symptom!')
                                audio = r.listen(source)
                            symBolean3 = r.recognize_google(audio)
        
                            sym = False     
        elif text in loose:
                random_response3 =  random.choice(bot1)
                print (random_response3)
                appu(random_response3)
                os.system("mpg321 test.mp3")
                symptom1 = text
                sym = True
                while sym:
                    r = sr.Recognizer()
                    with sr.Microphone() as source:
                            print ('Say symptom!')
                            audio = r.listen(source)
                    days = 0
                    days = r.recognize_google(audio) 

                    
                    if days != 0:
                        if symptom1 == 'Loose Motions':
                            symptom2Res = random.choice(bot2)
                            print (symptom2Res)
                            appu (symptom2Res)
                            os.system("mpg321 test.mp3")
                            
                            r = sr.Recognizer()
                            with sr.Microphone() as source:
                                print ('Say symptom!')
                                audio = r.listen(source)
                            symBolean1 = r.recognize_google(audio)

                            
                            symptom2Res = random.choice(bot20)
                            print (symptom2Res)
                            appu (symptom2Res)
                            os.system("mpg321 test.mp3")
                            
                            r = sr.Recognizer()
                            with sr.Microphone() as source:
                                print ('Say symptom!')
                                audio = r.listen(source)
                            symBolean2 = r.recognize_google(audio)

                            symptom2Res = random.choice(bot31)
                            print (symptom2Res)
                            appu (symptom2Res)
                            os.system("mpg321 test.mp3")
                            
                            r = sr.Recognizer()
                            with sr.Microphone() as source:
                                print ('Say symptom!')
                                audio = r.listen(source)
                            symBolean3 = r.recognize_google(audio)

                            sym = False                                                 
        elif text in sour:
                random_response3 =  random.choice(bot1)
                print (random_response3)
                appu(random_response3)
                os.system("mpg321 test.mp3")
                symptom1 = text
                sym = True
                while sym:
                    r = sr.Recognizer()
                    with sr.Microphone() as source:
                            print ('Say symptom!')
                            audio = r.listen(source)
                    days = 0
                    days = r.recognize_google(audio) 

                    
                    if days != 0:
                        if symptom1 == 'sore throat':
                            symptom2Res = random.choice(bot10)
                            print (symptom2Res)
                            appu (symptom2Res)
                            os.system("mpg321 test.mp3")
                            r = sr.Recognizer()
                            with sr.Microphone() as source:
                                print ('Do you have dry cough or wet cough?')
                                audio = r.listen(source)
                            symBolean3 = r.recognize_google(audio)
                        
                            if symptom2Res == random.choice(user8):
                                 print (symptom2Res)
                                 appu (symptom2Res)
                                 os.system("mpg321 test.mp3") 
                            elif symptom2Res == random.choice(user9):
                                 print (symptom2Res)
                                 appu (symptom2Res)
                                 os.system("mpg321 test.mp3")
                            else:
                                print ('I did not understand anything.')
                                os.system("mpg321 test.mp3")
                                r = sr.Recognizer()
                            with sr.Microphone() as source:
                                print ('Say symptom!')
                                audio = r.listen(source)
                    if days != 0:
                        if symptom1 == 'sore throat':
                            symptom2Res = random.choice(bot10)
                            pri
                            symBolean1 = r.recognize_google(audio)

                            
                            symptom2Res = random.choice(bot32)
                            print (symptom2Res)
                            appu (symptom2Res)
                            os.system("mpg321 test.mp3")
                    if days != 0:
                        if symptom1 == 'sore throat':
                            symptom2Res = random.choice(bot10)
                            pri
                            
                            r = sr.Recognizer()
                            with sr.Microphone() as source:
                                print ('Say symptom!')
                                audio = r.listen(source)
                            symBolean2 = r.recognize_google(audio)

                            sym = False
        elif text in bodyache:
                random_response3 =  random.choice(bot1)
                print (random_response3)
                appu(random_response3)
                os.system("mpg321 test.mp3")
                symptom1 = text
                sym = True
                while sym:
                    r = sr.Recognizer()
                    with sr.Microphone() as source:
                            print ('Say symptom!')
                            audio = r.listen(source)
                    days = 0
                    days = r.recognize_google(audio) 

                    
                    if days != 0:
                        if symptom1 == 'body ache':
                            symptom2Res = random.choice(bot2)
                            print (symptom2Res)
                            appu (symptom2Res)
                            os.system("mpg321 test.mp3")
                            
                            r = sr.Recognizer()
                            with sr.Microphone() as source:
                                print ('Say symptom!')
                                audio = r.listen(source)
                            symBolean1 = r.recognize_google(audio)

                            
                            symptom2Res = random.choice(bot18)
                            print (symptom2Res)
                            appu (symptom2Res)
                            os.system("mpg321 test.mp3")
                            
                            r = sr.Recognizer()
                            with sr.Microphone() as source:
                                print ('Say symptom!')
                                audio = r.listen(source)
                            symBolean2 = r.recognize_google(audio)

                            symptom2Res = random.choice(bot24)
                            print (symptom2Res)
                            appu (symptom2Res)
                            os.system("mpg321 test.mp3")
                            
                            r = sr.Recognizer()
                            with sr.Microphone() as source:
                                print ('Say symptom!')
                                audio = r.listen(source)
                            symBolean3 = r.recognize_google(audio)
        
                            sym = False     
        elif text in breathing:
                random_response3 =  random.choice(bot1)
                print (random_response3)
                appu(random_response3)
                os.system("mpg321 test.mp3")
                symptom1 = text
                sym = True
                while sym:
                    r = sr.Recognizer()
                    with sr.Microphone() as source:
                            print ('Say symptom!')
                            audio = r.listen(source)
                    days = 0
                    days = r.recognize_google(audio) 

                    
                    if days != 0:
                        if symptom1 == 'Breathing Problem':
                            symptom2Res = random.choice(bot23)
                            print (symptom2Res)
                            appu (symptom2Res)
                            os.system("mpg321 test.mp3")
                            
                            r = sr.Recognizer()
                            with sr.Microphone() as source:
                                print ('Say symptom!')
                                audio = r.listen(source)
                            symBolean1 = r.recognize_google(audio)

                            
                            symptom2Res = random.choice(bot33)
                            print (symptom2Res)
                            appu (symptom2Res)
                            os.system("mpg321 test.mp3")
                            
                            r = sr.Recognizer()
                            with sr.Microphone() as source:
                                print ('Say symptom!')
                                audio = r.listen(source)
                            symBolean2 = r.recognize_google(audio)
        
                            sym = False     
        else:
                print("I did not understand what you said") 
                        
                        
