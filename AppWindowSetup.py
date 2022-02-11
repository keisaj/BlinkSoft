# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AppWindowSetup.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AppWindow(object):
    def setupUi(self, AppWindow):
        AppWindow.setObjectName("AppWindow")
        AppWindow.resize(701, 896)

        self.centralwidget = QtWidgets.QWidget(AppWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.button1 = QtWidgets.QPushButton(self.centralwidget)
        self.button1.setGeometry(QtCore.QRect(10, 560, 120, 120))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.button1.setFont(font)
        self.button1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.button1.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/wc.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button1.setIcon(icon)
        self.button1.setIconSize(QtCore.QSize(100, 100))
        self.button1.setObjectName("button1")

        self.button2 = QtWidgets.QPushButton(self.centralwidget)
        self.button2.setGeometry(QtCore.QRect(150, 560, 120, 120))
        self.button2.setFont(font)
        self.button2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/food.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button2.setIcon(icon1)
        self.button2.setIconSize(QtCore.QSize(100, 100))
        self.button2.setObjectName("button2")

        self.button3 = QtWidgets.QPushButton(self.centralwidget)
        self.button3.setGeometry(QtCore.QRect(290, 560, 120, 120))
        self.button3.setFont(font)
        self.button3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/water.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button3.setIcon(icon2)
        self.button3.setIconSize(QtCore.QSize(100, 100))
        self.button3.setObjectName("button3")

        self.button4 = QtWidgets.QPushButton(self.centralwidget)
        self.button4.setGeometry(QtCore.QRect(430, 560, 120, 120))
        self.button4.setFont(font)
        self.button4.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/notepad.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button4.setIcon(icon3)
        self.button4.setIconSize(QtCore.QSize(100, 100))
        self.button4.setObjectName("button4")

        self.button5 = QtWidgets.QPushButton(self.centralwidget)
        self.button5.setGeometry(QtCore.QRect(570, 560, 120, 120))
        self.button5.setFont(font)
        self.button5.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/web.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button5.setIcon(icon4)
        self.button5.setIconSize(QtCore.QSize(100, 100))
        self.button5.setObjectName("button5")

        self.button6 = QtWidgets.QPushButton(self.centralwidget)
        self.button6.setGeometry(QtCore.QRect(10, 700, 120, 120))
        self.button6.setFont(font)
        self.button6.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/bed.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button6.setIcon(icon5)
        self.button6.setIconSize(QtCore.QSize(100, 100))
        self.button6.setObjectName("button6")

        self.button8 = QtWidgets.QPushButton(self.centralwidget)
        self.button8.setGeometry(QtCore.QRect(570, 700, 120, 120))
        self.button8.setFont(font)
        self.button8.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("images/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button8.setIcon(icon6)
        self.button8.setIconSize(QtCore.QSize(100, 100))
        self.button8.setObjectName("button8")

        self.button7 = QtWidgets.QPushButton(self.centralwidget)
        self.button7.setGeometry(QtCore.QRect(290, 700, 120, 120))
        self.button7.setFont(font)
        self.button7.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("images/emergency.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button7.setIcon(icon7)
        self.button7.setIconSize(QtCore.QSize(100, 100))
        self.button7.setObjectName("button7")

        self.videoLabel = QtWidgets.QLabel(self.centralwidget)
        self.videoLabel.setGeometry(QtCore.QRect(30, 40, 640, 480))
        self.videoLabel.setFrameShape(QtWidgets.QFrame.Panel)
        self.videoLabel.setLineWidth(2)
        self.videoLabel.setMidLineWidth(0)
        self.videoLabel.setText("")
        self.videoLabel.setObjectName("videoLabel")


        self.retranslateUi(AppWindow)
        QtCore.QMetaObject.connectSlotsByName(AppWindow)

    def retranslateUi(self, AppWindow):
        _translate = QtCore.QCoreApplication.translate
        AppWindow.setWindowTitle(_translate("AppWindow", "MainWindow"))

