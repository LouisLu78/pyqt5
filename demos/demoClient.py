# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoClient.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(170, 0, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textEditMessage = QtWidgets.QTextEdit(Dialog)
        self.textEditMessage.setGeometry(QtCore.QRect(20, 20, 281, 221))
        self.textEditMessage.setObjectName("textEditMessage")
        self.lineEditMessage = QtWidgets.QLineEdit(Dialog)
        self.lineEditMessage.setGeometry(QtCore.QRect(20, 250, 281, 31))
        self.lineEditMessage.setObjectName("lineEditMessage")
        self.pushButtonSend = QtWidgets.QPushButton(Dialog)
        self.pushButtonSend.setGeometry(QtCore.QRect(310, 250, 75, 31))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(12)
        self.pushButtonSend.setFont(font)
        self.pushButtonSend.setObjectName("pushButtonSend")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Client"))
        self.pushButtonSend.setText(_translate("Dialog", "Send"))
