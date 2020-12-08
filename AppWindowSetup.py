from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont


class Ui_AppWindow(object):

    def setupUi(self, AppWindow):
        AppWindow.setObjectName("AppWindow")
        AppWindow.resize(700, 680)

        self.horizontalLayout = QtWidgets.QHBoxLayout(AppWindow)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.videoLabel = QtWidgets.QLabel(AppWindow)
        self.verticalLayout.addWidget(self.videoLabel)
        self.videoLabel.setText("")
        self.videoLabel.setObjectName("videoLabel")

        self.button1 = QtWidgets.QPushButton(AppWindow)
        self.button1.setGeometry(200, 150, 100, 30)
        self.verticalLayout.addWidget(self.button1)
        self.button1.setObjectName("button1")

        self.button2 = QtWidgets.QPushButton(AppWindow)
        self.verticalLayout.addWidget(self.button2)
        self.button2.setObjectName("button2")

        self.button3 = QtWidgets.QPushButton(AppWindow)
        self.verticalLayout.addWidget(self.button3)
        self.button3.setObjectName("button3")

        self.button4 = QtWidgets.QPushButton(AppWindow)
        self.verticalLayout.addWidget(self.button4)
        self.button4.setObjectName("button4")

        self.button5 = QtWidgets.QPushButton(AppWindow)
        self.verticalLayout.addWidget(self.button5)
        self.button5.setObjectName("button5")

        self.button6 = QtWidgets.QPushButton(AppWindow)
        self.verticalLayout.addWidget(self.button6)
        self.button6.setObjectName("button6")

        self.button7 = QtWidgets.QPushButton(AppWindow)
        self.verticalLayout.addWidget(self.button7)
        self.button7.setObjectName("button7")

        self.button8 = QtWidgets.QPushButton(AppWindow)
        self.verticalLayout.addWidget(self.button8)
        self.button8.setObjectName("button8")

        self.buttonFeatures()

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(AppWindow)
        QtCore.QMetaObject.connectSlotsByName(AppWindow)

    def buttonFeatures(self):
        self.buttonList = [self.button1, self.button2, self.button3, self.button4, self.button5,
                           self.button6, self.button7, self.button8]
        for button in self.buttonList:
            button.setFont(QFont('Arial', 15))
            #button.setStyleSheet("background-color : white")

    def retranslateUi(self, AppWindow):
        _translate = QtCore.QCoreApplication.translate
        AppWindow.setWindowTitle(_translate("AppWindow", "MainWindow"))
        self.button1.setText(_translate("AppWindow", "WC needed"))
        self.button2.setText(_translate("AppWindow", "I\'m hungry"))
        self.button3.setText(_translate("AppWindow", "I\'m thirsty"))
        self.button4.setText(_translate("AppWindow", "Open Notepad"))
        self.button5.setText(_translate("AppWindow", "Open Browser"))
        self.button6.setText(_translate("AppWindow", "I want to rest"))
        self.button7.setText(_translate("AppWindow", "Exit program"))
        self.button8.setText(_translate("AppWindow", "EMERGENCY Please Help!!!"))



