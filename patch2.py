import speech_recognition as sr
import pyaudio
import pocketsphinx
import pyttsx3
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
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
        
def print_to_pdf():
    # Create a file named 'entry.pdf' in the current directory
    with open('entry.pdf', 'wb') as pdf_file:
        # Create a canvas object, using the letter page size
        c = canvas.Canvas(pdf_file, pagesize=letter)

        # Write text to the canvas
        c.drawString(100, 750, command)

        # Save the canvas
        c.save()

print_to_pdf()