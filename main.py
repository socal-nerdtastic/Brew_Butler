from gtts import gTTS
import os
import speech_recognition as sr
import datetime
import helper
import time
import playsound
import threading
import grabber
import tkinter as tk


class App(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.start()

    def callback(self):
        self.root.quit()

    def run(self):
        self.root = tk.Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.callback)
        self.root.title("Brew Butler")

        label = tk.Label(self.root, text="Hello World")
        label.pack()

        self.root.mainloop()


app = App()
def main():
    command_thread = threading.Thread(target=command)
    log_name = datetime.datetime.now()
    log_name = ("Brew day " + str(log_name.month) + "-" + str(log_name.day) + "-" + str(log_name.year))
    log = open(log_name, 'a')
    
    #helper.speak(helper.greeting())
    time.sleep(1)
    # Has the listen function run in the background like siri and can be called with the phrase "Hey Brew Butler".
    while True:
        if helper.listen() == True:
            new_command = helper.get_command()
            helper.execute_command(new_command)
        else:
            pass

    





    log.close()

def command():
    command = helper.get_command()
    helper.execute_command(command)
    command = ""



main()
