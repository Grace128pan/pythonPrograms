import PyPDF2
import pyttsx3
import os

# Define the paths
pdf_path = 'textToSpeech/poem.pdf'
audio_path = 'textToSpeech/poem.mp3'

# Initialize the TTS engine
engine = pyttsx3.init()

# Read the PDF file
with open(pdf_path, 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    text = ''
    for page in reader.pages:
        text += page.extract_text()

# Convert text to speech and save as mp3
engine.save_to_file(text, audio_path)
engine.runAndWait()

print(f"The audio file is saved at: {os.path.abspath(audio_path)}")
