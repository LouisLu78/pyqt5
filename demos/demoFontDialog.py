# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoFontDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.pushButtonFont = QtWidgets.QPushButton(Dialog)
        self.pushButtonFont.setGeometry(QtCore.QRect(140, 240, 101, 23))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(10)
        self.pushButtonFont.setFont(font)
        self.pushButtonFont.setObjectName("pushButtonFont")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(70, 20, 251, 211))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButtonFont.setText(_translate("Dialog", "choose font"))
