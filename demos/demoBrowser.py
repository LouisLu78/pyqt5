# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoBrowser.ui'
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
        self.label.setGeometry(QtCore.QRect(10, 20, 54, 12))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEditURL = QtWidgets.QLineEdit(Dialog)
        self.lineEditURL.setGeometry(QtCore.QRect(60, 10, 251, 41))
        self.lineEditURL.setObjectName("lineEditURL")
        self.pushButtonGO = QtWidgets.QPushButton(Dialog)
        self.pushButtonGO.setGeometry(QtCore.QRect(330, 10, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(12)
        self.pushButtonGO.setFont(font)
        self.pushButtonGO.setObjectName("pushButtonGO")
        self.widget = QtWebEngineWidgets.QWebEngineView(Dialog)
        self.widget.setGeometry(QtCore.QRect(20, 60, 361, 231))
        self.widget.setObjectName("widget")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "URL:"))
        self.pushButtonGO.setText(_translate("Dialog", "Go"))
from PyQt5 import QtWebEngineWidgets

