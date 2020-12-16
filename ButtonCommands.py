import subprocess as sp
import os
import webbrowser
import asyncio




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
        asyncio.create_subprocess_exec("osk")


    def command5(self):
        webbrowser.open("https://google.com")
        os.system("osk")

    def command6(self):
        print("I want to rest")

    def command7(self):
        print("EMERGENCY Please Help!!!")

    def command8(self):
        print("Exiting program...")
