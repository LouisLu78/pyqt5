# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoDisplayRowsOfTable.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(608, 411)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(13, 20, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.labelResponse = QtWidgets.QLabel(Dialog)
        self.labelResponse.setGeometry(QtCore.QRect(60, 360, 461, 41))
        self.labelResponse.setText("")
        self.labelResponse.setObjectName("labelResponse")
        self.lineEditDBName = QtWidgets.QLineEdit(Dialog)
        self.lineEditDBName.setGeometry(QtCore.QRect(210, 20, 351, 31))
        self.lineEditDBName.setObjectName("lineEditDBName")
        self.lineEditTableName = QtWidgets.QLineEdit(Dialog)
        self.lineEditTableName.setGeometry(QtCore.QRect(210, 70, 351, 31))
        self.lineEditTableName.setObjectName("lineEditTableName")
        self.pushButtonDispRow = QtWidgets.QPushButton(Dialog)
        self.pushButtonDispRow.setGeometry(QtCore.QRect(190, 120, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(10)
        self.pushButtonDispRow.setFont(font)
        self.pushButtonDispRow.setObjectName("pushButtonDispRow")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(80, 160, 351, 201))
        self.tableWidget.setRowCount(3)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Enter database name"))
        self.label_2.setText(_translate("Dialog", "Enter table name"))
        self.pushButtonDispRow.setText(_translate("Dialog", "Display Rows"))
