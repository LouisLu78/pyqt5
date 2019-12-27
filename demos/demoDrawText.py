# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoDrawText.ui'
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
        self.label.setGeometry(QtCore.QRect(20, 20, 361, 31))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.listWidgetFont = QtWidgets.QListWidget(Dialog)
        self.listWidgetFont.setGeometry(QtCore.QRect(20, 80, 141, 131))
        self.listWidgetFont.setObjectName("listWidgetFont")
        item = QtWidgets.QListWidgetItem()
        self.listWidgetFont.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetFont.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetFont.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetFont.addItem(item)
        self.pushButtonDrawText = QtWidgets.QPushButton(Dialog)
        self.pushButtonDrawText.setGeometry(QtCore.QRect(240, 230, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(10)
        self.pushButtonDrawText.setFont(font)
        self.pushButtonDrawText.setObjectName("pushButtonDrawText")
        self.comboBoxSize = QtWidgets.QComboBox(Dialog)
        self.comboBoxSize.setGeometry(QtCore.QRect(20, 230, 69, 22))
        self.comboBoxSize.setObjectName("comboBoxSize")
        self.comboBoxSize.addItem("")
        self.comboBoxSize.addItem("")
        self.comboBoxSize.addItem("")
        self.comboBoxSize.addItem("")
        self.comboBoxSize.addItem("")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(190, 80, 181, 131))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Enter some text in leftmost box, select font and size, \n"
"and click the Draw Text button"))
        __sortingEnabled = self.listWidgetFont.isSortingEnabled()
        self.listWidgetFont.setSortingEnabled(False)
        item = self.listWidgetFont.item(0)
        item.setText(_translate("Dialog", "Arial"))
        item = self.listWidgetFont.item(1)
        item.setText(_translate("Dialog", "Courier New"))
        item = self.listWidgetFont.item(2)
        item.setText(_translate("Dialog", "Times New Roman"))
        item = self.listWidgetFont.item(3)
        item.setText(_translate("Dialog", "Sans Serif"))
        self.listWidgetFont.setSortingEnabled(__sortingEnabled)
        self.pushButtonDrawText.setText(_translate("Dialog", "Draw Text"))
        self.comboBoxSize.setItemText(0, _translate("Dialog", "12"))
        self.comboBoxSize.setItemText(1, _translate("Dialog", "14"))
        self.comboBoxSize.setItemText(2, _translate("Dialog", "16"))
        self.comboBoxSize.setItemText(3, _translate("Dialog", "18"))
        self.comboBoxSize.setItemText(4, _translate("Dialog", "20"))
