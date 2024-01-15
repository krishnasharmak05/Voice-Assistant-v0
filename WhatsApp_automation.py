import random
import keyboard
from pynput.mouse import Button, Controller
import pygetwindow as gw
import time
import assets.TTSEngine_Handler as tts
from playsound import playsound

mouse = Controller()


def whatsapp_opener(lower_command: str, receiver) -> str:
    if lower_command.startswith("whatsapp"):
        message = lower_command.removeprefix("whatsapp ")
    elif lower_command.startswith("make a call to "):
        message = lower_command.removeprefix("make a call ")
    else:
        message = lower_command
    tts.engine.say("I got, Please wait until you hear the request for confirmation.")
    tts.engine.runAndWait()
    whatsapp_open = check_if_whatsapp_open()
    if not whatsapp_open:
        keyboard.press_and_release('win')
        time.sleep(1)
        keyboard.write('WhatsApp')
        time.sleep(1)
        keyboard.press_and_release('enter')
        time.sleep(2)
    time.sleep(1)
    keyboard.press_and_release('ctrl+f')
    time.sleep(0.5)
    keyboard.write(str(receiver))
    time.sleep(0.5)
    mouse.position = (193, 190)
    time.sleep(0.5)
    mouse.click(Button.left)
    time.sleep(2)
    return message


def whatsapp_message(lower_command:str, receiver:str|int):
    message = whatsapp_opener(lower_command, receiver)
    write_with_animation(message, receiver)



def write_with_animation(message:str|int,  receiver:str|int, time_delay:float=0.08):
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    message = str(message)
    for letter in message:
        rand_time = random.choices(range(1,10))[0]
        rand_num = random.choices(range(0,25))[0]
        if int(time.time()) % rand_time == 0:
            random_letter = alpha[rand_num]
            keyboard.write(random_letter[0])
            time.sleep(0.5)
            keyboard.press_and_release('backspace')
        keyboard.write(letter)
        time.sleep(time_delay)
    
    confirmation = confirmation_fx(message, receiver)
    if confirmation:
        keyboard.press_and_release('enter')
    else:
        playsound("./sounds/end.mp3")

def confirmation_fx(message, reciever):
    tts.engine.say(f"I got, {message} to be sent to, {reciever}. Is that correct?")
    tts.engine.runAndWait()
    confirm = input()
    if confirm.lower() == "yes" or confirm.lower() == "y" or confirm.lower() == "affirmative":
        return True
    return False


def check_if_whatsapp_open()->bool:
    active = gw.getAllWindows()
    active_titles = [i.title for i in active]
    if "WhatsApp" not in active_titles:
        return False
    whatsapp = gw.getWindowsWithTitle("WhatsApp")[-1]
    whatsapp.activate()
    return True

def get_number(lower_command)-> int | str:
    index = 0
    if "to" in lower_command.split():
        index = lower_command.split().index("to") + 1
    number = lower_command.split()[index]
    return number


def whatsapp_call(lower_command:str, call_type):
    number = get_number(lower_command)
    lower_command = whatsapp_opener(lower_command=lower_command, receiver=number)
    if call_type.startswith("voice"):
        mouse.position = (1184, 67)
        time.sleep(0.8)
        mouse.click(Button.left)
    elif call_type.startswith("video"):
        mouse.position = (1131, 70)
        time.sleep(0.8)
        mouse.click(Button.left)
    else:
        tts.engine.say("I don't know that type of call. Please repeat the whole command, and mention the type of WhatsApp call you want to make. Your options are: voice call, video call")
        tts.engine.runAndWait()
