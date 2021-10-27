from typing import Text
import pyttsx3
import datetime
import speech_recognition as sr 
sr.__version__
'3.8.1'

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


WAKE = "Bosco"
print("start")


engine = pyttsx3.init()

def time():
                Time = datetime.datetime.now().strftime("%I:%M")
                speak(Time)


def get_audio(): #capture sound
    print("mic start")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #playsound('audio.mp3')
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recongnizning...")
        text = r.recognize_google(audio, language='en-in')
        print(text)

    except Exception as e:
        print(e)
        #speak("Say that again please...")
        return "None"
    return text()
get_audio( )

        


def wakeWord(text):
    text = text()  # Convert the text to all lower case words
# Check to see if the users command/text contains a wake word    
    for phrase in WAKE:
        if phrase in text:
            return True
# If the wake word was not found return false
    return False

while True:
    text = get_audio
    
    response = ''
    
    if (wakeWord(text) == True):
        
        if('time') in text:
            time()