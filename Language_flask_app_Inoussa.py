import os
from flask import Flask, render_template, request, jsonify
import openai
import speech_recognition as sr
import pyttsx3
import soundfile as sf
import io
import simpleaudio as sa
from playsound import playsound
import threading


import warnings
warnings.filterwarnings("ignore", message="The NumPy module was reloaded")



app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'audio_files')
openai.api_key = "YOUR-API-KEY-HERE"
LANGUAGES = {
    'english': 'en',
    'french': 'fr',
}

# Set up Text-to-Speech API credentials
openai.api_key = "YOUR-API-KEY-HEREC"
model_engine = "text-davinci-003"
voice_engine = "text-to-speech/mark"

# Initialize the recognizer
r = sr.Recognizer()
GREETING_KEYWORDS = {
    'en': ['Hello!', 'Hi there!', 'Hey!'],
    'fr': ['Bonjour!', 'Salut!', 'Coucou!'],
}
dialogueArray = []

def build_prompt(text, language):
    prompt = f"{text}\n"
    if language == 'english':
        prompt += "Ino: "
    else:
        prompt += f"Ino ({language}): "
    return prompt


@app.route('/')
def home():
    return render_template('home.html', title='Home')

@app.route('/text')
def text():
    return render_template('text.html', title='Text')

@app.route('/speech')
def speech():
    return render_template('speech.html', title='Speech')

def generate_chat_response(user_input, lang):
    # Generate a response using OpenAI API
    prompt = build_prompt(user_input, lang)
    response = generate_response(prompt, lang)
    print(f"Response ({lang}): {response}")

    # Speak the response using pyttsx3 library
    sayResponse(response)

    return jsonify({'response': response})

@app.route('/chat', methods=['POST'])
def chat():
    lang = request.form['language']

    # Check if the input is from text or speech
    if 'input_text' in request.form:
        # Get the user input from the text form
        user_input = request.form['input_text']

    else:
        # Get the audio data from the speech form
        audio_data = request.form['audio_data']

        # Use SpeechRecognition library to transcribe the audio data
        r = sr.Recognizer()
        with sr.AudioFile(audio_data) as source:
            audio = r.record(source)
        try:
            user_input = r.recognize_google(audio, language=lang)
        except sr.UnknownValueError:
            return jsonify({'error': 'Unable to recognize speech'})

    if lang == 'en':
        response = generate_chat_response(user_input, lang)
    elif lang == 'fr':
        response = generate_chat_response(user_input, lang)
    else:
        return jsonify({'error': 'Invalid language'})

    return response

def generate_response(prompt, language):
    engine = "text-davinci-003" if language == 'fr' else "text-davinci-003"
    response = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

def generate_and_speak_response(user_input, lang):
    # Generate a text response based on the user's input
    response = generate_chat_response(user_input, lang)

    # Convert the text response to speech using pyttsx3 library
    engine = pyttsx3.init()
    engine.setProperty('voice', voices[lang])
    engine.say(response)
    engine.runAndWait()

    return response

def sayResponse(response):
    engine = pyttsx3.init()
    engine.setProperty('voice', voice_engine)
    engine.setProperty('rate', 0)
    engine.say(response)
    engine.runAndWait()



if __name__ == 'main':
    app.run(debug=True)

