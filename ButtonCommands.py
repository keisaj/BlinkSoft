import subprocess as sp

import webbrowser

from pynput import keyboard
import threading

import time
import os
import signal


        

class ButtonCommands(object):

    @classmethod
    def thread_osk(cls):
        cls.osk = sp.Popen("osk", stdout=sp.PIPE, shell=True, creationflags=sp.CREATE_NEW_PROCESS_GROUP)



    @staticmethod
    def on_press(key):
        if key == keyboard.Key.esc:
            print("escapin")
            return False



    @staticmethod
    def keyboard_listener():
        with keyboard.Listener(
                on_press=ButtonCommands.on_press) as listener:
            listener.join()

    @staticmethod
    def thread_keyboard_listener():
        y = threading.Thread(target=ButtonCommands.keyboard_listener)
        y.start()


    def command1(self):
        print("I need to use bathroom")

    def command2(self):
        print("I'm hungry.")

    def command3(self):
        print("I'm thirsty")

    def command4(self):
        programName = "notepad.exe"
        fileName = "file.txt"
        file = open(fileName, 'w')
        file.close()
        notepad = sp.Popen([programName, fileName])

        ButtonCommands.thread_keyboard_listener()

        x = threading.Thread(target=ButtonCommands.thread_osk)
        x.start()


    def command5(self):
        x = threading.Thread(target=ButtonCommands.thread_osk)
        webbrowser.open("https://google.com")
        x.start()


    def command6(self):
        print("I want to rest")

    def command7(self):
        print("EMERGENCY Please Help!!!")

    def command8(self):
        print("Exiting program...")
