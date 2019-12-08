# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoFontComboBox.ui'
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
        self.label.setGeometry(QtCore.QRect(10, 40, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 120, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.fontComboBox = QtWidgets.QFontComboBox(Dialog)
        self.fontComboBox.setGeometry(QtCore.QRect(170, 40, 213, 22))
        self.fontComboBox.setObjectName("fontComboBox")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(160, 150, 191, 101))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Select desired\n"
"font"))
        self.label_2.setText(_translate("Dialog", "Type some text"))
