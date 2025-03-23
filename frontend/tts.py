from gtts import gTTS

def get_speech_from_text(text):
    tts = gTTS(text=text, lang='en')  # Converts text to speech
    tts.save("output.mp3") # Saves the speech as an audio file
