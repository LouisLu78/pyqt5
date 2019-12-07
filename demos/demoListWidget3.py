# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoListWidget3.ui'
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
        self.label.setGeometry(QtCore.QRect(10, 20, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEditFoodItem = QtWidgets.QLineEdit(Dialog)
        self.lineEditFoodItem.setGeometry(QtCore.QRect(210, 20, 151, 31))
        self.lineEditFoodItem.setObjectName("lineEditFoodItem")
        self.listWidgetSelectedItems = QtWidgets.QListWidget(Dialog)
        self.listWidgetSelectedItems.setGeometry(QtCore.QRect(140, 80, 256, 192))
        self.listWidgetSelectedItems.setObjectName("listWidgetSelectedItems")
        self.pushButtonAdd = QtWidgets.QPushButton(Dialog)
        self.pushButtonAdd.setGeometry(QtCore.QRect(30, 152, 75, 31))
        self.pushButtonAdd.setObjectName("pushButtonAdd")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Your favorite food item"))
        self.pushButtonAdd.setText(_translate("Dialog", "Add to list"))
