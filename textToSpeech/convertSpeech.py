import pyttsx3
import os

# Initialize the TTS engine
engine = pyttsx3.init()

# Specify the text to be converted to speech
text = "Hello, I am a text to speech engine"

# Save the speech to an mp3 file
output_path = "textToSpeech/output.mp3"
engine.save_to_file(text, output_path)
engine.runAndWait()  # Ensure the saving process completes

# Get the current working directory
current_dir = os.getcwd()
print(f"The file is saved at: {os.path.join(current_dir, output_path)}")
