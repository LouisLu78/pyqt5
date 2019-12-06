# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoCalculator.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.labelFirstNumber = QtWidgets.QLabel(Dialog)
        self.labelFirstNumber.setGeometry(QtCore.QRect(30, 30, 161, 20))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(10)
        self.labelFirstNumber.setFont(font)
        self.labelFirstNumber.setObjectName("labelFirstNumber")
        self.labelSecondNumber = QtWidgets.QLabel(Dialog)
        self.labelSecondNumber.setGeometry(QtCore.QRect(30, 60, 161, 20))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(10)
        self.labelSecondNumber.setFont(font)
        self.labelSecondNumber.setObjectName("labelSecondNumber")
        self.labelResult = QtWidgets.QLabel(Dialog)
        self.labelResult.setGeometry(QtCore.QRect(70, 220, 241, 41))
        self.labelResult.setText("")
        self.labelResult.setObjectName("labelResult")
        self.lineEditFirstNumber = QtWidgets.QLineEdit(Dialog)
        self.lineEditFirstNumber.setGeometry(QtCore.QRect(200, 19, 161, 31))
        self.lineEditFirstNumber.setObjectName("lineEditFirstNumber")
        self.lineEditSecondNumber = QtWidgets.QLineEdit(Dialog)
        self.lineEditSecondNumber.setGeometry(QtCore.QRect(200, 60, 161, 31))
        self.lineEditSecondNumber.setObjectName("lineEditSecondNumber")
        self.pushButtonPlus = QtWidgets.QPushButton(Dialog)
        self.pushButtonPlus.setGeometry(QtCore.QRect(20, 162, 75, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.pushButtonPlus.setFont(font)
        self.pushButtonPlus.setObjectName("pushButtonPlus")
        self.pushButtonSubtract = QtWidgets.QPushButton(Dialog)
        self.pushButtonSubtract.setGeometry(QtCore.QRect(110, 160, 75, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.pushButtonSubtract.setFont(font)
        self.pushButtonSubtract.setObjectName("pushButtonSubtract")
        self.pushButtonMultiply = QtWidgets.QPushButton(Dialog)
        self.pushButtonMultiply.setGeometry(QtCore.QRect(200, 160, 75, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.pushButtonMultiply.setFont(font)
        self.pushButtonMultiply.setObjectName("pushButtonMultiply")
        self.pushButtonDevide = QtWidgets.QPushButton(Dialog)
        self.pushButtonDevide.setGeometry(QtCore.QRect(290, 160, 75, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.pushButtonDevide.setFont(font)
        self.pushButtonDevide.setObjectName("pushButtonDevide")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.labelFirstNumber.setText(_translate("Dialog", "Enter First Number"))
        self.labelSecondNumber.setText(_translate("Dialog", "Enter Second Number"))
        self.pushButtonPlus.setText(_translate("Dialog", "+"))
        self.pushButtonSubtract.setText(_translate("Dialog", "_"))
        self.pushButtonMultiply.setText(_translate("Dialog", "*"))
        self.pushButtonDevide.setText(_translate("Dialog", "/"))
