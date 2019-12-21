# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoTwoProgressBarsLocks.ui'
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
        self.label.setGeometry(QtCore.QRect(40, 25, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.progressBarFileDownload = QtWidgets.QProgressBar(Dialog)
        self.progressBarFileDownload.setGeometry(QtCore.QRect(40, 70, 321, 31))
        self.progressBarFileDownload.setProperty("value", 24)
        self.progressBarFileDownload.setObjectName("progressBarFileDownload")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 130, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.progressBarVirusScan = QtWidgets.QProgressBar(Dialog)
        self.progressBarVirusScan.setGeometry(QtCore.QRect(40, 180, 321, 31))
        self.progressBarVirusScan.setProperty("value", 24)
        self.progressBarVirusScan.setObjectName("progressBarVirusScan")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Downloading the file"))
        self.label_2.setText(_translate("Dialog", "Scanning for Virus"))
