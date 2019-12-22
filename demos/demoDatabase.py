# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoDatabase.ui'
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
        self.label.setGeometry(QtCore.QRect(10, 30, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.labelResponse = QtWidgets.QLabel(Dialog)
        self.labelResponse.setGeometry(QtCore.QRect(60, 180, 271, 31))
        self.labelResponse.setText("")
        self.labelResponse.setObjectName("labelResponse")
        self.lineEditDBName = QtWidgets.QLineEdit(Dialog)
        self.lineEditDBName.setGeometry(QtCore.QRect(140, 30, 241, 31))
        self.lineEditDBName.setObjectName("lineEditDBName")
        self.pushButtonCreateDB = QtWidgets.QPushButton(Dialog)
        self.pushButtonCreateDB.setGeometry(QtCore.QRect(180, 110, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(10)
        self.pushButtonCreateDB.setFont(font)
        self.pushButtonCreateDB.setObjectName("pushButtonCreateDB")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Enter database \n"
"name"))
        self.pushButtonCreateDB.setText(_translate("Dialog", "Create Database"))
