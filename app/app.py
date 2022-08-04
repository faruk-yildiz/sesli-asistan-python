from datetime import datetime
import webbrowser
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import random
import os


recognizer=sr.Recognizer()

def record(ask=False):
    if ask:
        print(ask)
    with sr.Microphone() as source:
        audioSource=recognizer.listen(source)
        voice=""
        try:
            voice=recognizer.recognize_google(audioSource,language='tr-TR')
        except sr.UnknownValueError:
            speak("Anlayamadım")
        except sr.RequestError:
            speak("Sistem arizali")
        return voice

def response(voice):
    if 'nasılsın' in voice:
        speak("iyi senden")
    if 'saat kaç' in voice:
        speak(datetime.now().strftime('%H:%M:%S'))
    if 'arama yap' in voice:
        arama=record("Ne aramak istersiniz")
        webbrowser.get().open("https://www.google.com/search?q="+arama)
        speak(arama + 'için bulduklarım')
    if 'bitti' in voice:
        speak("Bye bye")
        exit()

def speak(string):
    tts=gTTS(string,lang="tr")
    rand=random.randint(1,1000)
    file='audio-'+str(rand)+'.mp3'
    tts.save(file)
    playsound(file)
    os.remove(file)

while True:
    result=record()
    response(result)