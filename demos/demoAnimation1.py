# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoAnimation1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.pushButtonMoveDown = QtWidgets.QPushButton(Dialog)
        self.pushButtonMoveDown.setGeometry(QtCore.QRect(10, 20, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(12)
        self.pushButtonMoveDown.setFont(font)
        self.pushButtonMoveDown.setObjectName("pushButtonMoveDown")
        self.labelpic = QtWidgets.QLabel(Dialog)
        self.labelpic.setGeometry(QtCore.QRect(160, 190, 101, 71))
        self.labelpic.setText("")
        self.labelpic.setPixmap(QtGui.QPixmap("C:/Users/Basanwei/Pictures/1454533979.jpg"))
        self.labelpic.setObjectName("labelpic")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButtonMoveDown.setText(_translate("Dialog", "Move Down"))
