import speech_recognition as sr
import pyaudio
import pocketsphinx
import pyttsx3
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import nltk
nltk.download('punkt')
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

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
            temp = temp + ' '
        except sr.UnknownValueError:
            pass
        if('terminate' in command):
            break

temp=temp.replace('terminate','')
print(f"You said \"{temp}\" " )
        
def print_to_pdf():
    # Create a file named 'entry.pdf' in the current directory
    with open('entry.pdf', 'wb') as pdf_file:
        # Create a canvas object, using the letter page size
        c = canvas.Canvas(pdf_file, pagesize = letter)

        # Write text to the canvas
        x = temp
        
        x.split()

        p = ['a','b','c','d','e','g','h','n','o','p','q','s','u','v','w','x','y','z',' ','A','B','C','E','G','H','N','O','P','Q','r','S','U','V','X','Y','Z']
        q = ['j','k','t','F','I','J','K','L','T']
        r = ['i','l','f']
        s = ['M','w','W','O','S','m','D']
        t = ['r','.',':',';',',','/']

        k = 0
        hori = 760
        verti = 30

        for i in x:
            if k == 100:
                hori = hori - 15
                verti = 30
                k = 0
            
            if i in s :
                c.drawString(verti, hori, i)
                verti = verti + 9.2
                k = k + 1
                continue
            
            if i in p :
                c.drawString(verti, hori, i)
                verti = verti + 6
                k = k + 1
                continue

            if i in q :
                c.drawString(verti, hori, i)
                verti = verti + 4.5
                k = k + 1
                continue

            if i in r :
                c.drawString(verti, hori, i)
                verti = verti + 2
                k = k + 1
                continue

            if i in t :
                c.drawString(verti, hori, i)
                verti = verti + .3
                k = k + 1
                continue
                
        # Save the canvas
        c.save()

print_to_pdf()

text = temp 

parser = PlaintextParser.from_string(text, Tokenizer("english"))
summarizer = LexRankSummarizer()

summary = summarizer(parser.document, 2)  

for sentence in summary:
    print(sentence)