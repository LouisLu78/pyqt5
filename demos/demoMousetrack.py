# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoMousetrack.ui'
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
        self.label.setGeometry(QtCore.QRect(30, 20, 351, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.labelCoordinate = QtWidgets.QLabel(Dialog)
        self.labelCoordinate.setGeometry(QtCore.QRect(20, 240, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(10)
        self.labelCoordinate.setFont(font)
        self.labelCoordinate.setText("")
        self.labelCoordinate.setObjectName("labelCoordinate")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "This app will display x,y coordinates, \n"
"where mouse is moved on."))
