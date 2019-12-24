# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoShowRecords.ui'
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
        self.label.setGeometry(QtCore.QRect(23, 19, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(23, 80, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.labelResponse = QtWidgets.QLabel(Dialog)
        self.labelResponse.setGeometry(QtCore.QRect(30, 220, 291, 51))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(10)
        self.labelResponse.setFont(font)
        self.labelResponse.setText("")
        self.labelResponse.setObjectName("labelResponse")
        self.lineEditEmail = QtWidgets.QLineEdit(Dialog)
        self.lineEditEmail.setGeometry(QtCore.QRect(130, 20, 211, 41))
        self.lineEditEmail.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.lineEditEmail.setObjectName("lineEditEmail")
        self.lineEditPassword = QtWidgets.QLineEdit(Dialog)
        self.lineEditPassword.setGeometry(QtCore.QRect(132, 70, 211, 41))
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.pushButtonFirst = QtWidgets.QPushButton(Dialog)
        self.pushButtonFirst.setGeometry(QtCore.QRect(30, 180, 81, 23))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(10)
        self.pushButtonFirst.setFont(font)
        self.pushButtonFirst.setObjectName("pushButtonFirst")
        self.pushButtonPrevious = QtWidgets.QPushButton(Dialog)
        self.pushButtonPrevious.setGeometry(QtCore.QRect(120, 180, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(10)
        self.pushButtonPrevious.setFont(font)
        self.pushButtonPrevious.setObjectName("pushButtonPrevious")
        self.pushButtonNext = QtWidgets.QPushButton(Dialog)
        self.pushButtonNext.setGeometry(QtCore.QRect(210, 180, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(10)
        self.pushButtonNext.setFont(font)
        self.pushButtonNext.setObjectName("pushButtonNext")
        self.pushButtonLast = QtWidgets.QPushButton(Dialog)
        self.pushButtonLast.setGeometry(QtCore.QRect(300, 180, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(10)
        self.pushButtonLast.setFont(font)
        self.pushButtonLast.setObjectName("pushButtonLast")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Email"))
        self.label_2.setText(_translate("Dialog", "Password"))
        self.pushButtonFirst.setText(_translate("Dialog", "First Row"))
        self.pushButtonPrevious.setText(_translate("Dialog", "Previous"))
        self.pushButtonNext.setText(_translate("Dialog", "Next"))
        self.pushButtonLast.setText(_translate("Dialog", "Last Row"))
