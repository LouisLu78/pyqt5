# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoListWidgetOp.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(636, 289)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 40, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(150, 39, 151, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButtonAdd = QtWidgets.QPushButton(Dialog)
        self.pushButtonAdd.setGeometry(QtCore.QRect(180, 90, 75, 23))
        self.pushButtonAdd.setObjectName("pushButtonAdd")
        self.pushButtonEdit = QtWidgets.QPushButton(Dialog)
        self.pushButtonEdit.setGeometry(QtCore.QRect(310, 230, 71, 21))
        self.pushButtonEdit.setObjectName("pushButtonEdit")
        self.pushButtonDelete = QtWidgets.QPushButton(Dialog)
        self.pushButtonDelete.setGeometry(QtCore.QRect(400, 230, 75, 23))
        self.pushButtonDelete.setObjectName("pushButtonDelete")
        self.pushButtonDeleteAll = QtWidgets.QPushButton(Dialog)
        self.pushButtonDeleteAll.setGeometry(QtCore.QRect(480, 230, 81, 21))
        self.pushButtonDeleteAll.setObjectName("pushButtonDeleteAll")
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(310, 20, 256, 192))
        self.listWidget.setObjectName("listWidget")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Enter an item"))
        self.pushButtonAdd.setText(_translate("Dialog", "Add"))
        self.pushButtonEdit.setText(_translate("Dialog", "Edit"))
        self.pushButtonDelete.setText(_translate("Dialog", "Delete"))
        self.pushButtonDeleteAll.setText(_translate("Dialog", "Delete All"))
