from gtts import gTTS
import os
import speech_recognition as sr
import datetime
import helper
import time
import playsound
import threading
import grabber


def main():
    command_thread = threading.Thread(target=command)
    log_name = datetime.datetime.now()
    log_name = ("Brew day " + str(log_name.month) + "-" + str(log_name.day) + "-" + str(log_name.year))
    log = open(log_name, 'a')
    
    helper.speak(helper.greeting())
    time.sleep(1)
    #command_thread.start()
    #TODO make the listen function run in the background like siri or google assistant and be called in the same manner.
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
