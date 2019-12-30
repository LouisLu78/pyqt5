# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Mydemosignalslot.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.pushButtonClose = QtWidgets.QPushButton(Dialog)
        self.pushButtonClose.setGeometry(QtCore.QRect(134, 210, 91, 23))
        self.pushButtonClose.setObjectName("pushButtonClose")

        self.retranslateUi(Dialog)
        self.pushButtonClose.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButtonClose.setText(_translate("Dialog", "Close Window"))
