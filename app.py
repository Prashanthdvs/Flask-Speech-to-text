import speech_recognition as sr
from flask import logging, Flask, render_template, request, flash
from transformers import pipeline
import soundfile as sf
import sounddevice as sd

app = Flask(__name__)
app.secret_key = "VatsalParsaniya"
pipe = pipeline(model="Shubham09/whisper31filescheck")     # change to "your-username/the-name-you-picked"

@app.route('/')
def index():
    flash(" Welcome to Vatsal's site")
    return render_template('index.html')

@app.route('/audio_to_text/')
def audio_to_text():
    #flash(" Press Start to start recording audio and press Stop to end recording audio")
    return render_template('audio_to_text.html')

@app.route('/audio', methods=['POST'])
def audio():
    r = sr.Recognizer()
    with open('audio.flac', 'wb') as f:
        f.write(request.data)
  
    with sr.AudioFile('audio.flac') as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data, language='en-IN', show_all=True)
        text = pipe('audio.flac')
        print(text["text"])

        return_text = " Did you say : <br> "

        try:

            return_text += text + " <br> "
        except:
            return_text = " Sorry!!!! Voice not Detected "
        
    return str(return_text)


if __name__ == "__main__":
    app.run(debug=True)
