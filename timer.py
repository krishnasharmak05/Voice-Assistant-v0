# Written with the idea that I would also make a clock app. Haven't gotten around to it yet. Hence, some code on this might be broken.


import customtkinter as ctk
from threading import Thread
import time
import os
import simpleaudio as sa

class Timer_screen(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title = "Timer"
        self.geometry("300x300")
        self.button = ctk.CTkButton(self, command = self.end_sound, text = "Stop")
        self.button.grid(row = 0, column = 0, padx = 100, pady = 100)
        # self.app_reference = None

    def end_sound(self):
        # if self.app_reference:
            # self.app_reference.destroy()
            self.destroy()
            print("Button Clicked")
            self.play_obj.stop()

    def set_play_obj(self, play_obj):
        self.play_obj = play_obj


if not os.path.exists("%USERPROFILE%/Program Files/Clock/clock.exe"):
    CLOCK_APP = False
else:
    CLOCK_APP = True
sound = True


def timer(time_for_timer:int, lower_command:str):
    time.sleep(time_for_timer)
    app = Timer_screen()    
    # app.app_reference = app
    if "timer" in lower_command:
        Thread(target=timer_player, args=(app,)).start()
    elif "alarm" in lower_command:
        Thread(target=alarm_player, args=(app,)).start()
    app.mainloop()  
     

def alarm_player(app):
    wave_obj = sa.WaveObject.from_wave_file("C:/Users/krish/Downloads/mixkit-morning-clock-alarm-1003.wav")
    play_obj = wave_obj.play()
    app.set_play_obj(play_obj)
    play_obj.wait_done()

def timer_player(app):
    wave_obj = sa.WaveObject.from_wave_file("C:/Users/krish/Downloads/myalarm.wav")
    play_obj = wave_obj.play()
    app.set_play_obj(play_obj)
    play_obj.wait_done()

def set_timer(timer_time, lower_command:str):
    if CLOCK_APP:
        import clock_app
        clock_app.timer(timer_time)
    else:
        timer(timer_time, lower_command)


set_timer(1, "timer")
