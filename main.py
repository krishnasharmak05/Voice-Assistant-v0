# File that will always be running in the background.


# Restructure this code such that no sound comes up when jarvis is not actively running aka listening and doesn't understand something(sr.UnknownValueError). However, if sr.UnknowValueError is raised after jarvis has been activated by saying the hotkey, sound should be heard.

# GET ONE THREAD TO DO ALL OF THE PRINTING. WHEN COMMAND IS TO "exit" or "wait", stop printing.
import Browse_the_web
import news
import os
import time
import keyboard
import pandas
from playsound import playsound
import speech_recognition as sr
import assets.jokes as jokes
import webbrowser
#from gtts import gTTS
import assets.TTSEngine_Handler as pyttse
from tkinter import * # type: ignore
from assets.jokes import event
import pygetwindow as gw
import keyboard
import WhatsApp_automation




def listen_for_commands()-> str | None:
    recogniser = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening for commands...")
        recogniser.adjust_for_ambient_noise(source)
        audio = recogniser.listen(source)
    try:
        command = recogniser.recognize_google(audio) #type: ignore
        print("You said: " + command)
        return command
    except sr.UnknownValueError:
        print("Could not understand audio")
        return None
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return None    




def get_path():
    df = pandas.read_excel(io = "paths.xlsx")
    print(df)

# IncompleteFunction
    
def open_command(command:str): # INCOMPLETE
    element_to_be_opened = command.removeprefix('open ')
    path_to_element_to_be_opened = ""
    os.startfile(path_to_element_to_be_opened)


def bg_listener():
    while True:
        hotkey = listen_for_commands()
        if hotkey:
            hotkey = hotkey.lower()
        if hotkey == "jarvis" or hotkey == "hey jarvis" or hotkey == "hello jarvis" or hotkey == "j":
            playsound("./sounds/hello.mp3")
            pyttse.engine.say("Hello! . How can I help you?")
            pyttse.engine.runAndWait()
            task_runner()
            break
        
def type_function(keywords:str):
    keywords = keywords.removeprefix("type ")
    if "terminal" in keywords:
        keywords = keywords.removeprefix("terminal ")
        keyboard.press_and_release('win+r')
        time.sleep(0.1)
        keyboard.write('cmd')
        keyboard.press_and_release("enter")
        while True:
            active_window = gw.getActiveWindow()
            if active_window:
                print(active_window.title)
                time.sleep(0.5)
                if active_window.title == r"C:\WINDOWS\system32\cmd.exe" or active_window.title == "Win32Window" or active_window.title == "Command Prompt":
                    break        
    keyboard.write(keywords)
    keyboard.press_and_release("enter")




    
    
def task_runner():
    while True:
        command = listen_for_commands()
        if command:
            lower_command = command.lower()
            if lower_command is not None:
                if 'cancel' in lower_command or lower_command == "exit":
                    playsound("./sounds/end.mp3")
                    pass # change pass into: await until bg_listener returns a variable saying hotkey = "jarvis" then pass
                elif lower_command.startswith("whatsapp") or lower_command.startswith("message") or lower_command.startswith("send a message"):
                    number = WhatsApp_automation.get_number(lower_command)
                    WhatsApp_automation.whatsapp_message(command, number)
                elif lower_command.startswith("make a call") or lower_command.startswith("make a whatsapp call"):
                    if "voice" in lower_command:
                        number = WhatsApp_automation.get_number(lower_command)
                        WhatsApp_automation.whatsapp_call('voice', number)
                    elif 'video' in lower_command:
                        number = WhatsApp_automation.get_number(lower_command)
                        WhatsApp_automation.whatsapp_call('video', number)
                elif lower_command == "make a joke" or "joke" in lower_command: 
                    jokes.make_a_joke(event)
                elif lower_command.startswith("open"):
                    open_command(lower_command)
                elif (lower_command.startswith("google") or lower_command.startswith("hey jarvis google") )  and lower_command != "google":
                    Browse_the_web.google_search(1, lower_command)
                elif lower_command == "stop listening" or lower_command == "wait":
                    pyttse.engine.say("Alright. Have a good day!")
                    pyttse.engine.runAndWait()
                    playsound("./sounds/end.mp3")
                    break
                elif "type" in lower_command:
                    type_function(lower_command)
                elif lower_command == 'clear':

                    os.system("cls")
                else:
                    dont_know_text = "I don't know how to do that. Do you want me to Google it?"
                    print(dont_know_text)
                    pyttse.engine.say(dont_know_text)
                    pyttse.engine.runAndWait()
                    google_or_not = listen_for_commands()
                    if google_or_not == "yes":
                        Browse_the_web.google_search(0, lower_command)
                    else:
                        playsound("./sounds/end.mp3") # Change this sound.

    pyttse.engine.stop()





# HAS A THREAD ISSUE!!!
if __name__ == "__main__":
    bg_listener()
#get_path()



# set timer, reminder, stopwatch, alarm
# show/say weather
# change settings
# Make to-do lists and such.


# Play some music - NOT DOABLE DUE TO LEGAL REASONS.
# Play stuff on YT - NOT DOABLE DUE TO LEGAL REASONS.


# Send a whatsapp message - DONE
# Make a whatsapp call - DONE
# Get news - DONE

# TO DB = to-do lists, jokes, reminders and alarms(, timers).
# TAKE CARE OF THAT "NONE" THAT IS RETURNED FROM listen_for_commands()