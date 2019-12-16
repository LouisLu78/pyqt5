# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoMDI.ui'
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
        self.mdiArea = QtWidgets.QMdiArea(self.centralwidget)
        self.mdiArea.setGeometry(QtCore.QRect(80, 10, 601, 511))
        self.mdiArea.setObjectName("mdiArea")
        self.subwindow = QtWidgets.QWidget()
        self.subwindow.setObjectName("subwindow")
        self.label = QtWidgets.QLabel(self.subwindow)
        self.label.setGeometry(QtCore.QRect(20, 0, 131, 20))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.subwindow_2 = QtWidgets.QWidget()
        self.subwindow_2.setObjectName("subwindow_2")
        self.label_2 = QtWidgets.QLabel(self.subwindow_2)
        self.label_2.setGeometry(QtCore.QRect(40, 0, 131, 20))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menu_SubWindow_View = QtWidgets.QMenu(self.menubar)
        self.menu_SubWindow_View.setObjectName("menu_SubWindow_View")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionTab_View = QtWidgets.QAction(MainWindow)
        self.actionTab_View.setObjectName("actionTab_View")
        self.actionCascade_View = QtWidgets.QAction(MainWindow)
        self.actionCascade_View.setObjectName("actionCascade_View")
        self.actionTile_View = QtWidgets.QAction(MainWindow)
        self.actionTile_View.setObjectName("actionTile_View")
        self.actionSubWindow_View = QtWidgets.QAction(MainWindow)
        self.actionSubWindow_View.setObjectName("actionSubWindow_View")
        self.menu_SubWindow_View.addAction(self.actionSubWindow_View)
        self.menu_SubWindow_View.addAction(self.actionTab_View)
        self.menu_SubWindow_View.addAction(self.actionCascade_View)
        self.menu_SubWindow_View.addAction(self.actionTile_View)
        self.menubar.addAction(self.menu_SubWindow_View.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.subwindow.setWindowTitle(_translate("MainWindow", "Subwindow"))
        self.label.setText(_translate("MainWindow", "First Subwindow"))
        self.subwindow_2.setWindowTitle(_translate("MainWindow", "Subwindow"))
        self.label_2.setText(_translate("MainWindow", "Second Subwindow"))
        self.menu_SubWindow_View.setTitle(_translate("MainWindow", " Windows"))
        self.actionTab_View.setText(_translate("MainWindow", "Tabbed View"))
        self.actionCascade_View.setText(_translate("MainWindow", "Cascade  View"))
        self.actionTile_View.setText(_translate("MainWindow", "Tile View"))
        self.actionSubWindow_View.setText(_translate("MainWindow", "SubWindow View"))
