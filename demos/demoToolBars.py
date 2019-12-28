# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoToolBars.ui'
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
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionCircle = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/Basanwei/Pictures/1454533979.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCircle.setIcon(icon)
        self.actionCircle.setObjectName("actionCircle")
        self.actionRectangle = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/Basanwei/Pictures/d34155665ead4d8eabf2f3e7a0a19663.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRectangle.setIcon(icon1)
        self.actionRectangle.setObjectName("actionRectangle")
        self.actionLine = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:/Users/Basanwei/Pictures/IMG_20181230_162821.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLine.setIcon(icon2)
        self.actionLine.setObjectName("actionLine")
        self.toolBar.addAction(self.actionCircle)
        self.toolBar.addAction(self.actionRectangle)
        self.toolBar.addAction(self.actionLine)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionCircle.setText(_translate("MainWindow", "Circle"))
        self.actionCircle.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionRectangle.setText(_translate("MainWindow", "Rectangle"))
        self.actionRectangle.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.actionLine.setText(_translate("MainWindow", "Line"))
        self.actionLine.setShortcut(_translate("MainWindow", "Ctrl+L"))
