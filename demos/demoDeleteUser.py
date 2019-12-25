# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoDeleteUser.ui'
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
        self.label.setGeometry(QtCore.QRect(10, 30, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.labelsure = QtWidgets.QLabel(Dialog)
        self.labelsure.setGeometry(QtCore.QRect(20, 190, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(10)
        self.labelsure.setFont(font)
        self.labelsure.setObjectName("labelsure")
        self.labelResponse = QtWidgets.QLabel(Dialog)
        self.labelResponse.setGeometry(QtCore.QRect(40, 250, 321, 31))
        self.labelResponse.setText("")
        self.labelResponse.setObjectName("labelResponse")
        self.lineEditEmail = QtWidgets.QLineEdit(Dialog)
        self.lineEditEmail.setGeometry(QtCore.QRect(160, 30, 171, 31))
        self.lineEditEmail.setObjectName("lineEditEmail")
        self.lineEditPassword = QtWidgets.QLineEdit(Dialog)
        self.lineEditPassword.setGeometry(QtCore.QRect(160, 70, 171, 31))
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.pushButtonDeleteuser = QtWidgets.QPushButton(Dialog)
        self.pushButtonDeleteuser.setGeometry(QtCore.QRect(180, 120, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(10)
        self.pushButtonDeleteuser.setFont(font)
        self.pushButtonDeleteuser.setObjectName("pushButtonDeleteuser")
        self.pushButtonYes = QtWidgets.QPushButton(Dialog)
        self.pushButtonYes.setGeometry(QtCore.QRect(160, 190, 61, 23))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(10)
        self.pushButtonYes.setFont(font)
        self.pushButtonYes.setObjectName("pushButtonYes")
        self.pushButtonNo = QtWidgets.QPushButton(Dialog)
        self.pushButtonNo.setGeometry(QtCore.QRect(260, 190, 61, 23))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(10)
        self.pushButtonNo.setFont(font)
        self.pushButtonNo.setObjectName("pushButtonNo")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Email"))
        self.label_2.setText(_translate("Dialog", "Password"))
        self.labelsure.setText(_translate("Dialog", "Are you sure?"))
        self.pushButtonDeleteuser.setText(_translate("Dialog", "Delete User"))
        self.pushButtonYes.setText(_translate("Dialog", "Yes"))
        self.pushButtonNo.setText(_translate("Dialog", "No"))
