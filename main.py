import speech_recognition as sr
import pyaudio
import pocketsphinx
import pyttsx3
r = sr.Recognizer()

with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)
    command=r.recognize_google(audio)
    try:
        #print(type(r))
        print(f"You said \"{command}\" " )
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
