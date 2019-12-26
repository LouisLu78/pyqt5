# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoMouseClicks.ui'
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
        self.label.setGeometry(QtCore.QRect(20, 10, 351, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.labelPress = QtWidgets.QLabel(Dialog)
        self.labelPress.setGeometry(QtCore.QRect(20, 100, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(10)
        self.labelPress.setFont(font)
        self.labelPress.setText("")
        self.labelPress.setObjectName("labelPress")
        self.labelRelease = QtWidgets.QLabel(Dialog)
        self.labelRelease.setGeometry(QtCore.QRect(30, 200, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(10)
        self.labelRelease.setFont(font)
        self.labelRelease.setText("")
        self.labelRelease.setObjectName("labelRelease")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Displays the x,y coordinates where \n"
"mouse is pressed and released"))
