import speech_recognition as sr
import pyaudio
import pocketsphinx
import pyttsx3
#import time
r = sr.Recognizer()
command=''
temp=''
#t1=time.process_time()
#t2=time.process_time()
with sr.Microphone() as source:
    print("Say something!")
    while(True):
        audio = r.listen(source)
        try:
            command=r.recognize_google(audio)
            temp=temp+command+'.'
        except sr.UnknownValueError:
            pass
        if('terminate' in command):
            break



temp=temp.replace('terminate','')
print(f"You said \"{temp}\" " )

