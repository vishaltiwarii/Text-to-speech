# 📖 PDF to Speech Converter

A simple Python project that reads a PDF file and converts its text into speech using **PyPDF2** and **pyttsx3**.  
This can be useful for listening to study material, eBooks, or notes hands-free.

---

## 🚀 Features
- Extracts text from PDF files
- Converts text to speech in real-time
- Works offline (no internet required)
- Supports both **reading aloud** and optional **saving audio to a file**

---

## 🛠️ Tech Stack
- [PyPDF2](https://pypi.org/project/PyPDF2/) → For reading PDF files
- [pyttsx3](https://pypi.org/project/pyttsx3/) → For text-to-speech conversion

---

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/pdf-to-speech.git
   cd pdf-to-speech
Create and activate a virtual environment (optional but recommended):

bash
Copy code
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows
Install dependencies:

bash
Copy code
pip install PyPDF2 pyttsx3
▶️ Usage
Read first page aloud
python
Copy code
import PyPDF2
import pyttsx3

with open('file.pdf', 'rb') as path:
    pdf_reader = PyPDF2.PdfReader(path)
    first_page = pdf_reader.pages[0]
    text = first_page.extract_text()

engine = pyttsx3.init()
engine.say(text)
engine.runAndWait()
Read entire PDF aloud
python
Copy code
with open('file.pdf', 'rb') as path:
    pdf_reader = PyPDF2.PdfReader(path)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"

engine = pyttsx3.init()
engine.say(text)
engine.runAndWait()
Save to audio file (MP3/WAV)
python
Copy code
engine = pyttsx3.init()
engine.save_to_file(text, "output_audio.mp3")
engine.runAndWait()
📂 Example
Place any file.pdf in the project folder and run:

bash
Copy code
python main.py
It will read the PDF aloud or save it as an audio file.

📝 License
This project is licensed under the MIT License.
