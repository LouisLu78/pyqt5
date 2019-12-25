# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoChangePassword.ui'
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
        self.label.setGeometry(QtCore.QRect(20, 10, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 90, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 130, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEditEmail = QtWidgets.QLineEdit(Dialog)
        self.lineEditEmail.setGeometry(QtCore.QRect(130, 10, 221, 31))
        self.lineEditEmail.setObjectName("lineEditEmail")
        self.lineEditOldPass = QtWidgets.QLineEdit(Dialog)
        self.lineEditOldPass.setGeometry(QtCore.QRect(130, 50, 221, 31))
        self.lineEditOldPass.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.lineEditOldPass.setObjectName("lineEditOldPass")
        self.lineEditNewPass = QtWidgets.QLineEdit(Dialog)
        self.lineEditNewPass.setGeometry(QtCore.QRect(130, 90, 221, 31))
        self.lineEditNewPass.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.lineEditNewPass.setObjectName("lineEditNewPass")
        self.lineEditRe_Pass = QtWidgets.QLineEdit(Dialog)
        self.lineEditRe_Pass.setGeometry(QtCore.QRect(130, 130, 221, 31))
        self.lineEditRe_Pass.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.lineEditRe_Pass.setObjectName("lineEditRe_Pass")
        self.pushButtonChangePass = QtWidgets.QPushButton(Dialog)
        self.pushButtonChangePass.setGeometry(QtCore.QRect(150, 192, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButtonChangePass.setFont(font)
        self.pushButtonChangePass.setObjectName("pushButtonChangePass")
        self.labelResponse = QtWidgets.QLabel(Dialog)
        self.labelResponse.setGeometry(QtCore.QRect(40, 240, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(12)
        self.labelResponse.setFont(font)
        self.labelResponse.setText("")
        self.labelResponse.setObjectName("labelResponse")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Email"))
        self.label_2.setText(_translate("Dialog", "Old Password"))
        self.label_3.setText(_translate("Dialog", "New Password"))
        self.label_4.setText(_translate("Dialog", "Re_enter \n"
"New Password"))
        self.pushButtonChangePass.setText(_translate("Dialog", "Change Password"))
