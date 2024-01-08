# File that will always be running in the background.
from distutils.command.build_scripts import first_line_re
from io import BytesIO
import os
import keyboard
from playsound import playsound
import speech_recognition as sr
import webbrowser
#from gtts import gTTS
import TTSEngine_Handler as pyttse
from tkinter import *
import sys
sys.path.append("C:/Users/krish/Downloads/snack2210-tcl")


def listen_for_commands()-> str | None:
    recogniser = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening for commands...")
        recogniser.adjust_for_ambient_noise(source)
        audio = recogniser.listen(source)
    try:
        command = recogniser.recognize_google(audio) #type: ignore
        print("You said: " + command)
        return command.lower()
    except sr.UnknownValueError:
        print("Could not understand audio")
        return None
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return None

def remove_prefix(temp_query:str, number_of_words_to_be_removed:int = 3):
    query = ""
    for i in range(len(temp_query.split())):
        if i < number_of_words_to_be_removed:
            pass
        else:
            query += temp_query.split()[i] + " "
    if not query:
        query = temp_query
    return query 
    

def google_search(remove_prefix, value: int, query_from_speech:str):
    removed_prefix = remove_prefix(query_from_speech, value)
    base_url = "https://www.google.com/search?q="
    final_url = base_url + removed_prefix
    webbrowser.open_new_tab(final_url)

def open_command():
    pass


def bg_listner():
    while True:
        hotkey = listen_for_commands()
        if hotkey == "jarvis" or "hey jarvis" or "hello jarvis":
            playsound("C:/Users/krish/Downloads/Audio Files/hello.mp3")
            pyttse.engine.say("Hello! . How can I help you?")
            pyttse.engine.runAndWait()
            hotkey == ""
            task_runner()
            break
        


def type():
    pass #keyboard.

    
def task_runner():
    while True:
        lower_command = listen_for_commands()
        if lower_command is not None:
            if 'cancel' in lower_command or lower_command == "exit":
                playsound("C:/Users/krish/Downloads/Audio Files/end.mp3")
                break
            elif lower_command.startswith("open"):
                open_command()
            elif (lower_command.startswith("google") or lower_command.startswith("hey jarvis google") )  and lower_command != "google":
                google_search(remove_prefix,1, lower_command)
            elif lower_command == "stop listening":
                pyttse.engine.say("Alright. Have a good day!")
                pyttse.engine.runAndWait()
                playsound("C:/Users/krish/Downloads/Audio Files/end.mp3")
                break
            else:
                dont_know_text = "I don't know how to do that. Do you want me to Google it?"
                print(dont_know_text)
                pyttse.engine.say(dont_know_text)
                pyttse.engine.runAndWait()
                google_or_not = listen_for_commands()
                if google_or_not == "yes":
                    google_search(remove_prefix,1, lower_command)
                else:
                    playsound("C:/Users/krish/Downloads/Audio Files/end.mp3")

    pyttse.engine.stop()



bg_listner()



