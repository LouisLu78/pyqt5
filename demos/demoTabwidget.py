# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoTabwidget.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(567, 379)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 541, 361))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.checkBox = QtWidgets.QCheckBox(self.tab)
        self.checkBox.setGeometry(QtCore.QRect(10, 30, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(12)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 70, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(12)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_3.setGeometry(QtCore.QRect(10, 120, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(12)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_4.setGeometry(QtCore.QRect(10, 160, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(12)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setObjectName("checkBox_4")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(60, 212, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.radioButton = QtWidgets.QRadioButton(self.tab_2)
        self.radioButton.setGeometry(QtCore.QRect(20, 30, 161, 41))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.tab_2)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 80, 161, 41))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.tab_2)
        self.radioButton_3.setGeometry(QtCore.QRect(20, 130, 171, 41))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.tab_2)
        self.radioButton_4.setGeometry(QtCore.QRect(20, 180, 181, 61))
        self.radioButton_4.setObjectName("radioButton_4")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label = QtWidgets.QLabel(self.tab_3)
        self.label.setGeometry(QtCore.QRect(20, 30, 111, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab_3)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 101, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab_3)
        self.label_3.setGeometry(QtCore.QRect(20, 140, 121, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab_3)
        self.label_4.setGeometry(QtCore.QRect(20, 190, 141, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab_3)
        self.label_5.setGeometry(QtCore.QRect(20, 230, 141, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab_3)
        self.label_6.setGeometry(QtCore.QRect(10, 280, 141, 41))
        self.label_6.setObjectName("label_6")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit.setGeometry(QtCore.QRect(160, 30, 321, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 80, 321, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_3.setGeometry(QtCore.QRect(160, 130, 321, 41))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_4.setGeometry(QtCore.QRect(160, 180, 321, 41))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_5.setGeometry(QtCore.QRect(160, 230, 321, 41))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_6.setGeometry(QtCore.QRect(160, 280, 321, 41))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.tabWidget.addTab(self.tab_3, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.checkBox.setText(_translate("Dialog", "Cell Phone $150"))
        self.checkBox_2.setText(_translate("Dialog", "Laptop $500"))
        self.checkBox_3.setText(_translate("Dialog", "Camera $250"))
        self.checkBox_4.setText(_translate("Dialog", "Shoes $200"))
        self.pushButton.setText(_translate("Dialog", "Add to Cart"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Product Listing"))
        self.radioButton.setText(_translate("Dialog", "Debit Card"))
        self.radioButton_2.setText(_translate("Dialog", "Credit Card"))
        self.radioButton_3.setText(_translate("Dialog", "Net Banking"))
        self.radioButton_4.setText(_translate("Dialog", "Cash On Delivery"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Payment Method"))
        self.label.setText(_translate("Dialog", "Address 1"))
        self.label_2.setText(_translate("Dialog", "Address 2"))
        self.label_3.setText(_translate("Dialog", "State"))
        self.label_4.setText(_translate("Dialog", "Country"))
        self.label_5.setText(_translate("Dialog", "Zip Code"))
        self.label_6.setText(_translate("Dialog", "Contact Number"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "Delivery Address"))