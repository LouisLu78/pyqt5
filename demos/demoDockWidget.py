# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoDockWidget.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget_2 = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget_2.setObjectName("dockWidget_2")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.label = QtWidgets.QLabel(self.dockWidgetContents_2)
        self.label.setGeometry(QtCore.QRect(190, 50, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.dockWidgetContents_2)
        self.label_2.setGeometry(QtCore.QRect(20, 150, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.dockWidgetContents_2)
        self.label_3.setGeometry(QtCore.QRect(20, 220, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.dockWidgetContents_2)
        self.lineEdit.setGeometry(QtCore.QRect(140, 150, 321, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.dockWidgetContents_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 220, 321, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.dockWidgetContents_2)
        self.pushButton.setGeometry(QtCore.QRect(240, 370, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.dockWidget_2.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget_2)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.dockWidget_2.setWindowTitle(_translate("MainWindow", "Dock sign in form"))
        self.label.setText(_translate("MainWindow", "Sign In"))
        self.label_2.setText(_translate("MainWindow", "Email"))
        self.label_3.setText(_translate("MainWindow", "Password"))
        self.pushButton.setText(_translate("MainWindow", "Sign In"))
