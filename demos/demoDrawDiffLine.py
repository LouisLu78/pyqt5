# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoDrawDiffLine.ui'
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
        self.label.setGeometry(QtCore.QRect(30, 11, 331, 31))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.listWidgetLineType = QtWidgets.QListWidget(Dialog)
        self.listWidgetLineType.setGeometry(QtCore.QRect(20, 60, 141, 111))
        self.listWidgetLineType.setObjectName("listWidgetLineType")
        item = QtWidgets.QListWidgetItem()
        self.listWidgetLineType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetLineType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetLineType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetLineType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetLineType.addItem(item)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Select the style from the list and then \n"
"click and drag to draw a line"))
        __sortingEnabled = self.listWidgetLineType.isSortingEnabled()
        self.listWidgetLineType.setSortingEnabled(False)
        item = self.listWidgetLineType.item(0)
        item.setText(_translate("Dialog", "Solid Line"))
        item = self.listWidgetLineType.item(1)
        item.setText(_translate("Dialog", "Dash Line"))
        item = self.listWidgetLineType.item(2)
        item.setText(_translate("Dialog", "Dash Dot Line"))
        item = self.listWidgetLineType.item(3)
        item.setText(_translate("Dialog", "Dot Line"))
        item = self.listWidgetLineType.item(4)
        item.setText(_translate("Dialog", "Dash Dot Dot Line"))
        self.listWidgetLineType.setSortingEnabled(__sortingEnabled)
