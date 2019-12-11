# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoColorDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.pushButtoncolor = QtWidgets.QPushButton(Dialog)
        self.pushButtoncolor.setGeometry(QtCore.QRect(20, 50, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(12)
        self.pushButtoncolor.setFont(font)
        self.pushButtoncolor.setObjectName("pushButtoncolor")
        self.framecolor = QtWidgets.QFrame(Dialog)
        self.framecolor.setGeometry(QtCore.QRect(189, 50, 161, 131))
        self.framecolor.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.framecolor.setFrameShadow(QtWidgets.QFrame.Raised)
        self.framecolor.setObjectName("framecolor")
        self.labelcolor = QtWidgets.QLabel(Dialog)
        self.labelcolor.setGeometry(QtCore.QRect(43, 230, 311, 41))
        self.labelcolor.setText("")
        self.labelcolor.setObjectName("labelcolor")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButtoncolor.setText(_translate("Dialog", "choose color"))
