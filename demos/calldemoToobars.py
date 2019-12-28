# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2019/12/28
# Email: gq4350lu@hotmail.com

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPainter
from demos.demoToolBars import *

class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Draw_Sipmle_Figure')
        self.toDo=''
        self.pos1, self.pos2 = [0, 0], [0, 0]
        self.ui.actionCircle.triggered.connect(self.drawCircle)
        self.ui.actionRectangle.triggered.connect(self.drawRect)
        self.ui.actionLine.triggered.connect(self.drawLine)

    def paintEvent(self, event):
        qp=QPainter()
        qp.begin(self)
        width = self.pos2[0] - self.pos1[0]
        height = self.pos2[1] - self.pos1[1]

        if self.toDo == "rectangle":
            qp.drawRect(self.pos1[0], self.pos1[1], width, height)

        if self.toDo=="circle":
            rect =QRect(self.pos1[0], self.pos1[1], width, height)
            startAngle = 0
            arcLength = 360 * 16
            qp.drawArc(rect, startAngle, arcLength)

        if self.toDo=="line":
            qp.drawLine(self.pos1[0], self.pos1[1], self.pos2[0], self.pos2[1])

        qp.end()

    def mousePressEvent(self, event):
        if event.buttons() and Qt.LeftButton:
            self.pos1[0], self.pos1[1]=event.pos().x(), event.pos().y()

    def mouseReleaseEvent(self, event):
        self.pos2[0], self.pos2[1]=event.pos().x(), event.pos().y()
        self.update()

    def drawCircle(self):
        self.toDo="circle"

    def drawRect(self):
        self.toDo="rectangle"

    def drawLine(self):
        self.toDo="line"

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = AppWindow()
    w.show()
    sys.exit(app.exec_())

