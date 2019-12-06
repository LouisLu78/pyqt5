# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoCheckBox2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(523, 357)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(220, 10, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 40, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 170, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.labelAmount = QtWidgets.QLabel(Dialog)
        self.labelAmount.setGeometry(QtCore.QRect(150, 290, 201, 41))
        self.labelAmount.setText("")
        self.labelAmount.setObjectName("labelAmount")
        self.groupBoxIceCreams = QtWidgets.QGroupBox(Dialog)
        self.groupBoxIceCreams.setGeometry(QtCore.QRect(190, 70, 241, 121))
        self.groupBoxIceCreams.setTitle("")
        self.groupBoxIceCreams.setObjectName("groupBoxIceCreams")
        self.checkBoxRockyRoad = QtWidgets.QCheckBox(self.groupBoxIceCreams)
        self.checkBoxRockyRoad.setGeometry(QtCore.QRect(10, 70, 161, 21))
        self.checkBoxRockyRoad.setObjectName("checkBoxRockyRoad")
        self.checkBoxCookieDough = QtWidgets.QCheckBox(self.groupBoxIceCreams)
        self.checkBoxCookieDough.setGeometry(QtCore.QRect(10, 30, 161, 16))
        self.checkBoxCookieDough.setObjectName("checkBoxCookieDough")
        self.checkBoxChoclateAlmond = QtWidgets.QCheckBox(self.groupBoxIceCreams)
        self.checkBoxChoclateAlmond.setGeometry(QtCore.QRect(10, 50, 161, 21))
        self.checkBoxChoclateAlmond.setObjectName("checkBoxChoclateAlmond")
        self.checkBoxChoclateChips = QtWidgets.QCheckBox(self.groupBoxIceCreams)
        self.checkBoxChoclateChips.setGeometry(QtCore.QRect(10, 0, 181, 21))
        self.checkBoxChoclateChips.setObjectName("checkBoxChoclateChips")
        self.groupBoxDrinks = QtWidgets.QGroupBox(Dialog)
        self.groupBoxDrinks.setGeometry(QtCore.QRect(180, 210, 181, 111))
        self.groupBoxDrinks.setTitle("")
        self.groupBoxDrinks.setObjectName("groupBoxDrinks")
        self.checkBoxTea = QtWidgets.QCheckBox(self.groupBoxDrinks)
        self.checkBoxTea.setGeometry(QtCore.QRect(20, 80, 91, 21))
        self.checkBoxTea.setObjectName("checkBoxTea")
        self.checkBoxSoda = QtWidgets.QCheckBox(self.groupBoxDrinks)
        self.checkBoxSoda.setGeometry(QtCore.QRect(20, 50, 101, 21))
        self.checkBoxSoda.setObjectName("checkBoxSoda")
        self.checkBoxCoffee = QtWidgets.QCheckBox(self.groupBoxDrinks)
        self.checkBoxCoffee.setGeometry(QtCore.QRect(20, 20, 141, 16))
        self.checkBoxCoffee.setObjectName("checkBoxCoffee")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Menu"))
        self.label_2.setText(_translate("Dialog", "Select your IceCream"))
        self.label_3.setText(_translate("Dialog", "Select your drink"))
        self.checkBoxRockyRoad.setText(_translate("Dialog", "Rocky Road $5"))
        self.checkBoxCookieDough.setText(_translate("Dialog", "Cookie Dough $2"))
        self.checkBoxChoclateAlmond.setText(_translate("Dialog", "Choclate Almond $3"))
        self.checkBoxChoclateChips.setText(_translate("Dialog", "Mint Choclate Chips $4"))
        self.checkBoxTea.setText(_translate("Dialog", "Tea $1 "))
        self.checkBoxSoda.setText(_translate("Dialog", "Soda $3"))
        self.checkBoxCoffee.setText(_translate("Dialog", "Coffee $2"))
