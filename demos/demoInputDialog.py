# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoInputDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.lineEditcountry = QtWidgets.QLineEdit(Dialog)
        self.lineEditcountry.setGeometry(QtCore.QRect(92, 99, 211, 31))
        self.lineEditcountry.setObjectName("lineEditcountry")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 40, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButtoncountry = QtWidgets.QPushButton(Dialog)
        self.pushButtoncountry.setGeometry(QtCore.QRect(130, 190, 121, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.pushButtoncountry.setFont(font)
        self.pushButtoncountry.setObjectName("pushButtoncountry")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Your Country:"))
        self.pushButtoncountry.setText(_translate("Dialog", "Choose country"))
