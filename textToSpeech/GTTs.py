import PyPDF2
from gtts import gTTS
import os

# Define the paths
pdf_path = 'textToSpeech/Poem.pdf'
audio_path = 'textToSpeech/poem2.mp3'

# Read the PDF file
with open(pdf_path, 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    text = ''
    for page in reader.pages:
        text += page.extract_text()

# Convert text to speech using gTTS
tts = gTTS(text, lang='en')
tts.save(audio_path)

print(f"The audio file is saved at: {os.path.abspath(audio_path)}")
