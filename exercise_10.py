import pyttsx3
engine = pyttsx3.init()
engine.say("My name is Mahruful Alam, I wanna become a Software Engineer.")
engine.runAndWait()


import pyttsx3
engine = pyttsx3.init()
l = ['Ashraf', 'Mehedi', 'Sabbir',"Masum","Sifat","Ehsan","Samayon","Engr Mahruful Alam"]
for names in l:
        engine.say(f'Shout out to {names}')
        engine.runAndWait()