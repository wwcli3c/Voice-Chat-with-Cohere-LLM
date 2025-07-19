import speech_recognition as sr
from gtts import gTTS
import os
from playsound import playsound
import cohere

co = cohere.Client("YOUR_COHERE_API_KEY")

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ تكلم الآن...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language='ar-SA')
        print(f"📝 النص: {text}")
        return text
    except Exception as e:
        print(" لم أستطع التعرف على الصوت:", e)
        return None

def query_llm(prompt):
    response = co.generate(
        model='command-r-plus',
        prompt=prompt,
        max_tokens=200,
        temperature=0.6,
    )
    reply = response.generations[0].text.strip()
    print(f"🤖 الرد: {reply}")
    return reply

def text_to_speech(text):
    tts = gTTS(text, lang='ar')
    tts.save("response.mp3")
    playsound("response.mp3")

if __name__ == "__main__":
    prompt = speech_to_text()
    if prompt:
        response = query_llm(prompt)
        text_to_speech(response)
