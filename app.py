import PyPDF2
import pyttsx3

with open('file.pdf', 'rb') as path:
    pdf_reader = PyPDF2.PdfReader(path)
    first_page = pdf_reader.pages[0]
    text = first_page.extract_text()


engine = pyttsx3.init()
engine.say(text)
engine.runAndWait()
