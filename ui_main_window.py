# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from ButtonCommands import *

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(525, 386)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.image_label = QtWidgets.QLabel(Form)
        self.image_label.setObjectName("image_label")
        self.verticalLayout.addWidget(self.image_label)
        self.control_bt = QtWidgets.QPushButton(Form)
        self.control_bt.setObjectName("control_bt")
        self.verticalLayout.addWidget(self.control_bt)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(Form)

        self.createComandButtons(Form)

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Cam view"))
        #self.image_label.setText(_translate("Form", "TextLabel"))
        self.control_bt.setText(_translate("Form", "Start"))

    def createComandButtons(self, Form):
        _translate = QtCore.QCoreApplication.translate
        buttonLabels = [
                        "WC needed", "I'm hungry", "I'm thirsty",
                        "Open Notepad", "Open Browser", "I want to rest",
                        "Exit program", "EMERGENCY Please Help!!!"
                    ]

        commandList = [ButtonCommands.command1, ButtonCommands.command2, ButtonCommands.command3,
                       ButtonCommands.command4, ButtonCommands.command5, ButtonCommands.command6,
                       ButtonCommands.command7, ButtonCommands.command8]
        self.buttonList = []
        for label, command in zip(buttonLabels, commandList):

            self.command_button = QtWidgets.QPushButton(Form)
            self.command_button.setObjectName(label)
            self.verticalLayout.addWidget(self.command_button)
            self.command_button.setText(_translate("Form", label))
            self.command_button.clicked.connect(command)
            self.buttonList.append(self.command_button)

        return self.buttonList




