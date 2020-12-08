import subprocess as sp
import os
import webbrowser




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
        os.system("osk")

    def command5(self):
        webbrowser.open("https://google.com")
        os.system("osk")

    def command6(self):
        print("I want to rest")

    def command7(self):
        print("Exiting program...")

    def command8(self):
        print("EMERGENCY Please Help!!!")