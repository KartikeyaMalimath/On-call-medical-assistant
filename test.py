import random
from six.moves import input
from gtts import gTTS
import os
language = 'en'

greetings = ['hola', 'hello', 'hi', 'hi', 'hey!','hey']

question = ['how are you?','how are you doing?']
responses = ['Okay',"I'm fine"]

symptoms = ['i have headache','i have fever',]
responses2 = ['from how many days?']

while True:
        userInput = input(">> ")
        if userInput in greetings:
                random_greeting = random.choice(greetings)
                print(random_greeting)
                myobj = gTTS(text=random_greeting, lang=language, slow=False)
                myobj.save("test.mp3")
                os.system("mpg321 test.mp3")
        elif userInput in question:
                random_response = random.choice(responses)
                print(random_response)
                myobj = gTTS(text=random_response, lang=language, slow=False)
                myobj.save("test1.mp3")
                os.system("mpg321 test1.mp3")
        elif userInput in symptoms:
                random_response2 = random.choice(responses2)
                print(random_response2)
                myobj = gTTS(text=random_response2, lang=language, slow=False)
                myobj.save("test2.mp3")
                os.system("mpg321 test2.mp3")
        else:
                print("I did not understand what you said") 
                        
                        
