# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoSpinner.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(632, 300)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(13, 50, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 121, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.labelTotalAmount = QtWidgets.QLabel(Dialog)
        self.labelTotalAmount.setGeometry(QtCore.QRect(340, 230, 161, 31))
        self.labelTotalAmount.setText("")
        self.labelTotalAmount.setObjectName("labelTotalAmount")
        self.spinBoxBookQty = QtWidgets.QSpinBox(Dialog)
        self.spinBoxBookQty.setGeometry(QtCore.QRect(290, 60, 42, 22))
        self.spinBoxBookQty.setObjectName("spinBoxBookQty")
        self.doubleSpinBoxSugarWeight = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBoxSugarWeight.setGeometry(QtCore.QRect(290, 130, 62, 22))
        self.doubleSpinBoxSugarWeight.setObjectName("doubleSpinBoxSugarWeight")
        self.lineEditBookPrice = QtWidgets.QLineEdit(Dialog)
        self.lineEditBookPrice.setGeometry(QtCore.QRect(150, 60, 113, 20))
        self.lineEditBookPrice.setObjectName("lineEditBookPrice")
        self.lineEditBookAmount = QtWidgets.QLineEdit(Dialog)
        self.lineEditBookAmount.setEnabled(False)
        self.lineEditBookAmount.setGeometry(QtCore.QRect(380, 60, 113, 20))
        self.lineEditBookAmount.setObjectName("lineEditBookAmount")
        self.lineEditSugarPrice = QtWidgets.QLineEdit(Dialog)
        self.lineEditSugarPrice.setGeometry(QtCore.QRect(150, 130, 113, 20))
        self.lineEditSugarPrice.setObjectName("lineEditSugarPrice")
        self.lineEditSugarAmount = QtWidgets.QLineEdit(Dialog)
        self.lineEditSugarAmount.setEnabled(False)
        self.lineEditSugarAmount.setGeometry(QtCore.QRect(380, 130, 113, 20))
        self.lineEditSugarAmount.setObjectName("lineEditSugarAmount")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Book Price value"))
        self.label_2.setText(_translate("Dialog", "Sugar Price value"))
