import tkinter as tk
from time import strftime
from tkinter import ttk
import speech_recognition as sr
from gtts import gTTS
import playsound
import random

# Create the main window
root = tk.Tk()
root.title("Tamagochi Chafa")

# Create a label for the clock (keep this part)
clock_label = tk.Label(root, text="Clock will go here")
clock_label.pack()

# Create a frame for the mascot display (keep this part)
mascot_frame = tk.Frame(root, width=200, height=200, bg="black")
mascot_frame.pack()

# Create a text area for notes and input/output
text_area = tk.Text(root, height=10, width=40)
text_area.pack()

# Function to update the clock (keep this part)
def update_clock():
    clock_label.config(text=strftime("%H:%M:%S"))
    root.after(1000, update_clock)

update_clock()

# Function to capture and recognize speech
def recognize_speech():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    try:
        with mic as source:
            print("Habla algo...")
            audio = recognizer.listen(source)
            print("Audio capturado. Procesando...")

        # Recognize speech and set it in the text area
        recognized_text = recognizer.recognize_google(audio, language='es')
        text_area.delete(1.0, tk.END)  # Clear previous text
        text_area.insert(tk.END, recognized_text)

        # Convert the recognized text to voice and play it
    #    tts = gTTS(recognized_text, lang='es')
    #    tts.save("output.mp3")
    #    playsound.playsound("output.mp3")

    except sr.UnknownValueError:
        pass
    #    text_area.delete(1.0, tk.END)  # Clear previous text
    #    text_area.insert(tk.END, "No se pudo entender lo que dijiste")

# Create a button to trigger speech recognition
speech_button = ttk.Button(root, text="Speech Recognition", command=recognize_speech)
speech_button.pack()

root.mainloop()