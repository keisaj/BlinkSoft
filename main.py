"""
In this example, we demonstrate how to create simple camera viewer using Opencv3 and PyQt5
Author: Berrouba.A
Last edited: 21 Feb 2018
"""

# import system module
import sys

# import some PyQt5 modules
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer

import dlib
from scipy.spatial import distance

# import Opencv module
import cv2

from ui_main_window import *


class MainWindow(QWidget):
    # class constructor
    def __init__(self):
        # call QWidget constructor
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.hog_face_detector = dlib.get_frontal_face_detector()
        self.dlib_facelandmark = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")


        # create a timer
        self.timer = QTimer()
        # set timer timeout callback function
        self.timer.timeout.connect(self.viewCam)
        # set control_bt callback clicked  function
        self.ui.control_bt.clicked.connect(self.controlTimer)
        self.iterating = True
    # view camera
    def viewCam(self):
        # read image in BGR format
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
        self.ui.image_label.setPixmap(QPixmap.fromImage(qImg))

    def draw_eyes(self, frame):
        """
        Draws lines trough eye landmarks and detects if eyes are closed or not
        """
        self.frame = frame
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = self.hog_face_detector(gray)
        for face in faces:

            face_landmarks = self.dlib_facelandmark(gray, face)
            leftEye = []
            rightEye = []

            for n in range(36, 42):
                x = face_landmarks.part(n).x
                y = face_landmarks.part(n).y
                leftEye.append((x, y))
                next_point = n + 1
                if n == 41:
                    next_point = 36
                x2 = face_landmarks.part(next_point).x
                y2 = face_landmarks.part(next_point).y
                cv2.line(frame, (x, y), (x2, y2), (0, 255, 0), 1)

            for n in range(42, 48):
                x = face_landmarks.part(n).x
                y = face_landmarks.part(n).y
                rightEye.append((x, y))
                next_point = n + 1
                if n == 47:
                    next_point = 42
                x2 = face_landmarks.part(next_point).x
                y2 = face_landmarks.part(next_point).y
                cv2.line(frame, (x, y), (x2, y2), (0, 255, 0), 1)

            left_ear = self.calculate_EAR(leftEye)
            right_ear = self.calculate_EAR(rightEye)

            EAR = (left_ear + right_ear) / 2
            EAR = round(EAR, 2)
            if EAR < 0.26:
                cv2.putText(frame, "Eyes closed", (20, 100),
                            cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 255), 4)
                cv2.putText(frame, "Sensing signal", (20, 400),
                            cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 4)
                print("Eyes closed")
            print(EAR)

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

    # start/stop timer
    def controlTimer(self):
        # if timer is stopped
        if not self.timer.isActive():
            # create video capture
            self.cap = cv2.VideoCapture(0)
            # start timer
            self.timer.start(20)
            # update control_bt text
            self.ui.control_bt.setText("Stop")
        # if timer is started
        else:
            # stop timer
            self.timer.stop()
            # release video capture
            self.cap.release()
            # update control_bt text
            self.ui.control_bt.setText("Start")

    """def iterateThroughButtons(self):

        while self.iterating:

            for button in self.ui.buttonList:
                button"""



if __name__ == '__main__':
    app = QApplication(sys.argv)

    # create and show mainWindow
    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec_())