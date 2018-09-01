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

greetings = ['hola', 'hello', 'hi', 'hi', 'hey!','hey']

question = ['how are you','how are you doing']
responses = ['Okay',"I'm fine"]

symptoms = ['i have headache','i have fever',]
responses2 = ['from how many days?']

user1 = ['headache', 'fever', 'stomachache','burning eyes', ' vomiting',' bleeding nose','sour throat',' bodyache',' breathing problem','loose motion','indigestion']
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
bot22 = ['do u have cough?']
bot23 = ['are you working very long with electronic devices?']
bot24 = ['physical stress?']
bot25 = ['ok thank you let is figure out what is going on']
bot26  = ['do you have migrane history?']

bot27 = ['do you have dry cough or wet cough?']
user7 = ['dry']
user8 = ['wet']

user9 = ['cut','wound']
bot28 = ['old or new cut?']

user10 = ['burn']
bot29 = ['old or new burn?']

user11 = ['mouth ulser']

user12 = ['heart pain','chest pain','got fracture', 'i am feeling dizzy']
bot30 = ['please consult a doctor']


condition = True
while condition:
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
                random_greeting = random.choice(greetings)
                print(random_greeting)
                myobj = gTTS(text=random_greeting, lang=language, slow=False)
                myobj.save("test.mp3")
                os.system("mpg321 test.mp3")
        elif text in question:
                random_response = random.choice(responses)
                print(random_response)
                myobj = gTTS(text=random_response, lang=language, slow=False)
                myobj.save("test1.mp3")
                os.system("mpg321 test1.mp3")
        elif text in symptoms:
                random_response2 = random.choice(responses2)
                print(random_response2)
                myobj = gTTS(text=random_response2, lang=language, slow=False)
                myobj.save("test2.mp3")
                os.system("mpg321 test2.mp3")
        else:
                print("I did not understand what you said") 
                        
                        
