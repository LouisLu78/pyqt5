# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoListWidget2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(550, 357)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 30, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.labelTest = QtWidgets.QLabel(Dialog)
        self.labelTest.setGeometry(QtCore.QRect(20, 190, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(12)
        self.labelTest.setFont(font)
        self.labelTest.setObjectName("labelTest")
        self.listWidgetDiagnosis = QtWidgets.QListWidget(Dialog)
        self.listWidgetDiagnosis.setGeometry(QtCore.QRect(270, 20, 256, 131))
        self.listWidgetDiagnosis.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.listWidgetDiagnosis.setObjectName("listWidgetDiagnosis")
        item = QtWidgets.QListWidgetItem()
        self.listWidgetDiagnosis.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetDiagnosis.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetDiagnosis.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetDiagnosis.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetDiagnosis.addItem(item)
        self.listWidgetSelectedTests = QtWidgets.QListWidget(Dialog)
        self.listWidgetSelectedTests.setGeometry(QtCore.QRect(270, 200, 256, 131))
        self.listWidgetSelectedTests.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.listWidgetSelectedTests.setObjectName("listWidgetSelectedTests")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Choose the Diagnosis\n"
"Tests"))
        self.labelTest.setText(_translate("Dialog", "Selected tests are"))
        __sortingEnabled = self.listWidgetDiagnosis.isSortingEnabled()
        self.listWidgetDiagnosis.setSortingEnabled(False)
        item = self.listWidgetDiagnosis.item(0)
        item.setText(_translate("Dialog", "Urine Analysis $5"))
        item = self.listWidgetDiagnosis.item(1)
        item.setText(_translate("Dialog", "Chest X-Ray $100"))
        item = self.listWidgetDiagnosis.item(2)
        item.setText(_translate("Dialog", "Sugar Level test $3"))
        item = self.listWidgetDiagnosis.item(3)
        item.setText(_translate("Dialog", "Hemoglobin test $7"))
        item = self.listWidgetDiagnosis.item(4)
        item.setText(_translate("Dialog", "Thyroid Stimulating Harmone test $10"))
        self.listWidgetDiagnosis.setSortingEnabled(__sortingEnabled)
