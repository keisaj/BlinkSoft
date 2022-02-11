import subprocess as sp
import webbrowser
from PyQt5.QtWidgets import QApplication
from pynput import keyboard
import threading
import sys
import pyautogui
import os



class ButtonCommands(object):
    @staticmethod
    def thread_osk():
        osk = sp.Popen("osk", stdout=sp.PIPE, shell=True, creationflags=sp.CREATE_NEW_PROCESS_GROUP)

    @staticmethod
    def on_press(key):
        if key == keyboard.Key.esc:
            print("Exiting onscreen keyboard...")
            pyautogui.keyDown('alt')
            pyautogui.press('f4')
            pyautogui.keyUp('alt')
            os.system('taskkill /im osk.exe')
            pyautogui.keyDown('Enter')
            pyautogui.keyUp('Enter')
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
        print("I need to use a bathroom")

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
        ButtonCommands.thread_keyboard_listener()
        ButtonCommands.browsercount = 0
        x = threading.Thread(target=ButtonCommands.thread_osk)
        webbrowser.open("https://google.com")
        x.start()

    def command6(self):
        print("I want to rest")

    def command7(self):
        print("EMERGENCY Please Help!!!")

    def command8(self):
        print("Exiting program...")
        app = QApplication(sys.argv)
        sys.exit(app.exec_())

