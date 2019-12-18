# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2019/12/18

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter
from demos.demoMenuBar import *

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.pos1=[0,0]
        self.pos2=[0,0]
        self.toDraw=''
        self.ui.actionDraw_Circle.triggered.connect(self.drawCircle)
        self.ui.actionDraw_Line.triggered.connect(self.drawLine)
        self.ui.actionDraw_Rectangle.triggered.connect(self.drawRect)
        self.ui.actionPage_Setup.triggered.connect(self.pagesetup)
        self.ui.actionSet_Password.triggered.connect(self.password)
        self.ui.actionCopy.triggered.connect(self.copyMethod)
        self.ui.actionCut.triggered.connect(self.cutMethod)
        self.ui.actionPaste.triggered.connect(self.pasteMethod)

    def paintEvent(self, event):
        qp=QPainter()
        qp.begin(self)
        if self.toDraw=='rectangle':
            width=self.pos2[0]-self.pos1[0]
            height=self.pos2[1]-self.pos1[1]
            qp.drawRect(self.pos1[0], self.pos1[1], width, height)

        if self.toDraw=='line':
            qp.drawLine(self.pos1[0], self.pos1[1], self.pos2[0],
                        self.pos2[1])

        if self.toDraw=='circle':
            width = self.pos2[0] - self.pos1[0]
            height = self.pos2[1] - self.pos1[1]
            rect = QtCore.QRect(self.pos1[0], self.pos1[1], width, height)
            startAngle = 0
            arcLength = 360 * 16
            qp.drawArc(rect, startAngle, arcLength)
        qp.end()

    def mousePressEvent(self, event):
        if event.buttons() & QtCore.Qt.LeftButton:
            self.pos1[0], self.pos1[1] = event.pos().x(), event.pos().y()

    def mouseReleaseEvent(self, event):
        self.pos2[0], self.pos2[1] = event.pos().x(), event.pos().y()
        self.update()

    def drawCircle(self):
        self.ui.label.setText("")
        self.toDraw = "circle"

    def drawLine(self):
        self.ui.label.setText("")
        self.toDraw = "line"

    def drawRect(self):
        self.ui.label.setText("")
        self.toDraw = "rectangle"

    def pagesetup(self):
        self.ui.label.setText("Page Setup menu item is selected")

    def password(self):
        self.ui.label.setText("Password Setup menu item is selected")

    def copyMethod(self):
        self.ui.label.setText("Copy menu item is selected")

    def cutMethod(self):
        self.ui.label.setText("Cut menu item is selected")

    def pasteMethod(self):
        self.ui.label.setText("Paste menu item is selected")

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = App()
    w.show()
    sys.exit(app.exec_())







