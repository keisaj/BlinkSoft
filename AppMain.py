import sys

# import some PyQt5 modules
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer

import dlib
from scipy.spatial import distance

from guiLoop import guiLoop

from pynput import keyboard
from pynput.keyboard import Key, Controller


import cv2

import datetime as dt
import time

from ButtonCommands import *
from AppWindowSetup4 import *

flaga = False

class AppMain(QWidget):


    def __init__(self):

        super().__init__()
        self.ui =Ui_AppWindow()
        self.ui.setupUi(self)

        self.keyboard = Controller()

        self.hog_face_detector = dlib.get_frontal_face_detector()
        self.dlib_facelandmark = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

        self.timer = QTimer()
        self.timer.timeout.connect(self.viewCam)
        self.controlTimer()



        self.ui.button1.clicked.connect(ButtonCommands.command1)
        self.ui.button2.clicked.connect(ButtonCommands.command2)
        self.ui.button3.clicked.connect(ButtonCommands.command3)
        self.ui.button4.clicked.connect(ButtonCommands.command4)
        self.ui.button5.clicked.connect(ButtonCommands.command5)
        self.ui.button6.clicked.connect(ButtonCommands.command6)
        self.ui.button7.clicked.connect(ButtonCommands.command7)
        self.ui.button8.clicked.connect(ButtonCommands.command8)




    @guiLoop
    def buttonLoop(self):
        self.buttonList = [self.ui.button1, self.ui.button2, self.ui.button3, self.ui.button4, self.ui.button5,
                           self.ui.button6, self.ui.button7, self.ui.button8]
        while 1:
            for button in self.buttonList:
                button.setStyleSheet("background-color : red")
                button.setFocus()
                self.selectedButton = button
                yield 2
                button.setStyleSheet("background-color : light gray")


    def viewCam(self):

        _, frame = self.cap.read()
        frame = cv2.flip(frame, 1)
        self.draw_eyes(frame)
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # get image infos
        height, width, channel = cv2image.shape
        step = channel * width
        # create QImage from image
        qImg = QImage(cv2image.data, width, height, step, QImage.Format_RGB888)
        # show image in img_label
        self.ui.videoLabel.setPixmap(QPixmap.fromImage(qImg))

    def controlTimer(self):

        if not self.timer.isActive():

            self.cap = cv2.VideoCapture(0)
            self.timer.start(20)

        else:

            self.timer.stop()
            self.cap.release()


    def draw_eyes(self, frame):
        """
        Draws lines trough eye landmarks and detects if eyes are closed or not
        """
        global flaga
        self.frame = frame
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = self.hog_face_detector(gray)

        for face in faces:

            face_landmarks = self.dlib_facelandmark(gray, face)
            leftEye = [] # left eye coordinates array
            rightEye = [] # right eye coordinates array

            for n in range(36, 42):
                # drawing line through left eye points and appending point's coordinates to the array
                x = face_landmarks.part(n).x
                y = face_landmarks.part(n).y
                leftEye.append((x, y))
                next_point = n + 1
                if n == 41:
                    next_point = 36
                x2 = face_landmarks.part(next_point).x
                y2 = face_landmarks.part(next_point).y
                cv2.line(frame, (x, y), (x2, y2), (0, 255, 0), 1) # drawing line through eye points

            for n in range(42, 48):
                # drawing line through right eye points and appending point's coordinates to the array
                x = face_landmarks.part(n).x
                y = face_landmarks.part(n).y
                rightEye.append((x, y))
                next_point = n + 1
                if n == 47:
                    next_point = 42
                x2 = face_landmarks.part(next_point).x
                y2 = face_landmarks.part(next_point).y
                cv2.line(frame, (x, y), (x2, y2), (0, 255, 0), 1) # drawing line through eye points

            left_ear = self.calculate_EAR(leftEye)
            right_ear = self.calculate_EAR(rightEye)

            EAR = (left_ear + right_ear) / 2
            EAR = round(EAR, 2)

            if EAR < 0.26:
                cv2.putText(frame, "Eyes closed", (20, 100),
                            cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 255), 4)
                cv2.putText(frame, "Sensing signal", (20, 400),
                            cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 4)
                #print("Eyes closed")
                if flaga == False:
                    self.keyboard.press(Key.space)
                    self.keyboard.release(Key.space)
                    flaga = True
            else:
                flaga = False
            #print(EAR)

    def calculate_EAR(self, eye):
        """
        Calculates Eye Aspect Ratio
        """
        self.eye = eye
        A = distance.euclidean(self.eye[1], self.eye[5])
        B = distance.euclidean(self.eye[2], self.eye[4])
        C = distance.euclidean(self.eye[0], self.eye[3])
        self.eye_aspect_ratio = (A + B) / (2.0 * C)
        return self.eye_aspect_ratio

if __name__ == '__main__':
    app = QApplication(sys.argv)

    mainWindow = AppMain()
    mainWindow.show()
    mainWindow.buttonLoop()


    sys.exit(app.exec_())