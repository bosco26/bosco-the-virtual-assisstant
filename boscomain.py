from typing import Text
import pyttsx3
import datetime
import speech_recognition as sr 
import random 
from random import choice
import time
import sys
import pyjokes

sys.path.append('/usr/local/lib/python3.9.7/dist-packages/')
sr.__version__
'3.8.1'

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


WAKE = "car"
print("start")
print(__name__)

engine = pyttsx3.init()

def clock():
                Clock = datetime.datetime.now().strftime("%I:%M")
                speak(Clock)

def game():
    rps = ('Rock','Paper','Scissors')
    speak("rock...")
    time.sleep(0.5)
    speak("paper...")
    time.sleep(0.5)
    speak("scissors")
    time.sleep(0.5)
    speak("Shoot!!")
    time.sleep(0.5)
    speak(random.choice(rps))

def coin():
    Coin = ('Heads','Tails')
    speak(random.choice(Coin))
    
def dice():
    Coin = ('1','2','3','4','5','6')
    speak(random.choice(dice))
    
def jokes():
    speak(pyjokes.get_joke())

    
#######################################################################
def get_audio(): #capture sound
    #print("mic start")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #playsound('audio.mp3')
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recongnizning...")
        r = sr.Recognizer()
        text = r.recognize_google(audio, language='en-in').lower()
        print(text)

    except Exception as e:
        print(e)
        #speak("Say that again please...")
        return "None"   
    return text
get_audio()

if __name__ == '__main__': #!works but slow
    
    while True:
        print("nearly there")
        text = get_audio()
        if text.count(WAKE) > 0:
        
            while True:
                command = get_audio().lower()
                
                if 'hey bosco hello' in command:
                        speak('it works')
                        
                elif 'time' in command:
                    clock()
                    
                elif 'game' in command:
                    game()
                
                elif 'coin flip' in command:
                    coin()
                    
                elif 'dice' in command:
                    dice()
                elif 'version' in command:
                    speak('alpha_1')
                elif 'joke' in command:
                    jokes()
