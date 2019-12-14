# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoServer.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(12)
        Dialog.setFont(font)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(170, 0, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEditMessage = QtWidgets.QLineEdit(Dialog)
        self.lineEditMessage.setGeometry(QtCore.QRect(10, 260, 281, 31))
        self.lineEditMessage.setObjectName("lineEditMessage")
        self.textEditMessage = QtWidgets.QTextEdit(Dialog)
        self.textEditMessage.setGeometry(QtCore.QRect(13, 30, 331, 221))
        self.textEditMessage.setObjectName("textEditMessage")
        self.pushButtonSend = QtWidgets.QPushButton(Dialog)
        self.pushButtonSend.setGeometry(QtCore.QRect(310, 260, 75, 31))
        self.pushButtonSend.setObjectName("pushButtonSend")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Server"))
        self.pushButtonSend.setText(_translate("Dialog", "Send"))
