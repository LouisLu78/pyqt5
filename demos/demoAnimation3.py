# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoAnimation3.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.labelpic = QtWidgets.QLabel(Dialog)
        self.labelpic.setGeometry(QtCore.QRect(223, 210, 131, 61))
        self.labelpic.setText("")
        self.labelpic.setPixmap(QtGui.QPixmap("C:/Users/Basanwei/Pictures/d34155665ead4d8eabf2f3e7a0a19663.jpeg"))
        self.labelpic.setObjectName("labelpic")
        self.pushButtonBounce = QtWidgets.QPushButton(Dialog)
        self.pushButtonBounce.setGeometry(QtCore.QRect(30, 20, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(12)
        self.pushButtonBounce.setFont(font)
        self.pushButtonBounce.setObjectName("pushButtonBounce")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButtonBounce.setText(_translate("Dialog", "Bounce"))
