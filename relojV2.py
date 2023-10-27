#convierte la voz en texto y lo lee
#libreria que permite convertir la voz en texto
#pip install SpeechRecognition
#libreria que permite convertir texto en voz
#pip install gTTS
#pip install playsound
#pip install SpeechRecognition
#pip install gTTS
#pip install playsound
#pip install pyttsx3
#pip install pyaudio

import speech_recognition as sr
from gtts import gTTS
import playsound
import random
import pyttsx3

recognizer = sr.Recognizer()
mic = sr.Microphone()

try:
    with mic as source:
        print("Habla algo...")
        audio = recognizer.listen(source)
        print("Audio capturado. Procesando...")

    text = recognizer.recognize_google(audio, language='es')
    print(f'Transcripción: {text}')

    tts = gTTS(text, lang='es')

    # Cambia el nombre aleatorio
    num_alet = random.randint(1, 100)
    tts.save("output.mp3")

    # Reproduce el archivo de audio
    playsound.playsound("output.mp3")

    # Crear un motor de texto a voz
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    
    # Cambia la voz que desees utilizando un índice
    # Puedes ajustar el índice para seleccionar una voz diferente
    # Por ejemplo, 0 para voz masculina, 1 para voz femenina, etc.
    engine.setProperty('voice', voices[1].id)

    # Reproduce el texto en voz
    engine.say(text)
    engine.runAndWait()

except sr.UnknownValueError:
    print("No se pudo entender lo que dijiste")
