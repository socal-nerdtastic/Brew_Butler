#!/usr/bin/env python3

# import order per pep8 https://www.python.org/dev/peps/pep-0008/#imports
# standard library imports
import os
import datetime
import time
import threading
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror

# installed library imports
from gtts import gTTS
import speech_recognition as sr
import playsound

# module level imports
import grabber
import helper

class Tab1(ttk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        self.timer_obj = ' '

        # Note that we are *in* the Tab1 class, so we use plain 'self' as the master
        lbl = ttk.Label(self, text ="Timer")
        lbl.grid(column = 0, row = 0, padx = 30, pady = 30)

        # 2 lines not strictly required if unless you need the object later
        # but 2 lines are always preferred for readability
        # name 'btn' is generic, reuseable, throwaway name that I use. Could be anything.
        btn = ttk.Button(self, text ="Voice Command", command = self.get_command)
        btn.grid(column = 1, row = 1, padx = 30, pady = 30)

        ttk.Label(self, text = "Notes").grid(column = 2, row = 0, padx = 30, pady = 30)

        # 2 lines required here, because we want to use the Entry object later to get a value
        self.time = ttk.Entry(self)
        self.time.grid(column = 0, row = 1, padx = 30, pady = 30)

        self.notes = ttk.Entry(self)
        self.notes.grid(column = 2, row = 1, padx = 30, pady = 30)

        #note = str(ttk.Entry.get(self))

        #print("note = " + note)

        self.timer_btn = ttk.Button(self, text ="Start", command = self.start_pressed)
        self.timer_btn.grid(column = 0, row = 2, padx = 30, pady = 30)

        btn = ttk.Button(self, text ="Log", command = self.log_pressed)
        btn.grid(column = 2, row = 2, padx = 30, pady = 30)

    def get_command(self):
        helper.trigger_voice() # whatever

    def start_pressed(self):
        try:
            seconds = int(self.time.get())
            self.timer(seconds)
        except ValueError:
            showerror("Error", "Please enter an integer number of seconds")

    def timer(self, seconds_left=0):
        self.time.delete(0, tk.END)
        self.time.insert(tk.END, seconds_left)
        self.after_cancel(self.timer_obj)
        if seconds_left > 0:
            self.timer_obj = self.after(1000, self.timer, seconds_left-1)

    def log_pressed(self):
        log_name = datetime.datetime.now()
        log_name = ("Brew day " + str(log_name.month) + "-" + str(log_name.day) + "-" + str(log_name.year))
        with open(log_name, 'a') as log:
            log.write(self.notes.get() + '\n')
            print('Wrote note to log file')

class App(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title("TBD")

        self.tabControl = ttk.Notebook(self)

        self.tab1 = Tab1(self.tabControl)
        self.tab2 = ttk.Frame(self.tabControl)

        self.tabControl.add(self.tab1, text ='Home')
        self.tabControl.add(self.tab2, text ='Calculations')
        self.tabControl.pack(expand = 1, fill ="both", padx = 5)

def main():
    command_thread = threading.Thread(target=command)
    app = App()
    app.mainloop() # blocking. Program will not pass this line until the GUI is closed.

    return

    #helper.speak(helper.greeting())
    time.sleep(1)
    # Has the listen function run in the background like siri and can be called with the phrase "Hey Brew Butler".
    #while True:
        #if helper.listen() == True:
            #new_command = helper.get_command()
            #helper.execute_command(new_command)
        #else:
            #pass

def command():
    command = helper.get_command()
    helper.execute_command(command)
    command = ""

if __name__ == '__main__':
    main()
