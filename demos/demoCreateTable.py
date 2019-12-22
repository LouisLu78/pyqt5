# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoCreateTable.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(659, 543)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 30, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(130, 150, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(310, 150, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.labelResponse = QtWidgets.QLabel(Dialog)
        self.labelResponse.setGeometry(QtCore.QRect(90, 380, 491, 41))
        self.labelResponse.setText("")
        self.labelResponse.setObjectName("labelResponse")
        self.lineEditDBName = QtWidgets.QLineEdit(Dialog)
        self.lineEditDBName.setGeometry(QtCore.QRect(200, 30, 351, 31))
        self.lineEditDBName.setObjectName("lineEditDBName")
        self.lineEditTableName = QtWidgets.QLineEdit(Dialog)
        self.lineEditTableName.setGeometry(QtCore.QRect(200, 90, 351, 31))
        self.lineEditTableName.setObjectName("lineEditTableName")
        self.lineEditColumnName = QtWidgets.QLineEdit(Dialog)
        self.lineEditColumnName.setGeometry(QtCore.QRect(122, 179, 121, 31))
        self.lineEditColumnName.setObjectName("lineEditColumnName")
        self.comboBoxDataType = QtWidgets.QComboBox(Dialog)
        self.comboBoxDataType.setGeometry(QtCore.QRect(310, 180, 71, 31))
        self.comboBoxDataType.setObjectName("comboBoxDataType")
        self.pushButtonAddColumn = QtWidgets.QPushButton(Dialog)
        self.pushButtonAddColumn.setGeometry(QtCore.QRect(470, 180, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(10)
        self.pushButtonAddColumn.setFont(font)
        self.pushButtonAddColumn.setObjectName("pushButtonAddColumn")
        self.pushButtonCreateTable = QtWidgets.QPushButton(Dialog)
        self.pushButtonCreateTable.setGeometry(QtCore.QRect(270, 290, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(10)
        self.pushButtonCreateTable.setFont(font)
        self.pushButtonCreateTable.setObjectName("pushButtonCreateTable")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Enter Database Name"))
        self.label_2.setText(_translate("Dialog", "Enter Table Name"))
        self.label_3.setText(_translate("Dialog", "Column Name"))
        self.label_4.setText(_translate("Dialog", "Data Type"))
        self.pushButtonAddColumn.setText(_translate("Dialog", "Add Column"))
        self.pushButtonCreateTable.setText(_translate("Dialog", "Create Table"))
