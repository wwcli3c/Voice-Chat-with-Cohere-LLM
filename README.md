# Voice-Chat-with-Cohere-LLM

Voice Chat with Cohere LLM (Speech-to-Text & Text-to-Speech)
Description
A simple Python project that captures speech from your microphone, converts it to text, sends it to a Cohere language model (LLM), then converts the model's response back into speech and plays it.


Important Requirements pip install:
SpeechRecognition
gTTS
playsound==1.2.2
cohere
pyaudio
pipwin



Add your (Cohere API key) in the app.py file:
co = cohere.Client("YOUR_COHERE_API_KEY")


Run the main script:
Speak into your microphone and the app will respond using text-to-speech.

Notes:
If you do not have a microphone, you can modify the code to use a prerecorded .wav file instead.
Ensure pip is up to date to avoid installation problems.
