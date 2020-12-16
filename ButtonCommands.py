import subprocess as sp
import os
import webbrowser
import asyncio

import threading

def thread_osk():
    os.system("osk")
    
    while True:
        pass
        

class ButtonCommands(object):
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
        sp.Popen([programName, fileName])

        x = threading.Thread(target=thread_osk)
        x.start()



    def command5(self):
        x = threading.Thread(target=thread_osk)
        webbrowser.open("https://google.com")
        x.start()

    def command6(self):
        print("I want to rest")

    def command7(self):
        print("EMERGENCY Please Help!!!")

    def command8(self):
        print("Exiting program...")
