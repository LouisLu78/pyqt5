# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoAnimation4.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.pushButtonMoveCurve = QtWidgets.QPushButton(Dialog)
        self.pushButtonMoveCurve.setGeometry(QtCore.QRect(170, 160, 101, 31))
        self.pushButtonMoveCurve.setObjectName("pushButtonMoveCurve")
        self.labelpic = QtWidgets.QLabel(Dialog)
        self.labelpic.setGeometry(QtCore.QRect(0, 10, 141, 151))
        self.labelpic.setText("")
        self.labelpic.setPixmap(QtGui.QPixmap("C:/Users/Basanwei/Pictures/dog.jpg"))
        self.labelpic.setObjectName("labelpic")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButtonMoveCurve.setText(_translate("Dialog", "Move with Curve"))
