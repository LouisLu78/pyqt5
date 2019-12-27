# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2019/12/27
# Email: gq4350lu@hotmail.com

import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen
from demos.demoDrawDiffLine import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
        self.lineType='Solid Line'
        self.pos1, self.pos2 = [0, 0], [0, 0]

    def paintEvent(self, event):
        qp=QPainter()
        qp.begin(self)
        pen=QPen(Qt.red,4)
        self.lineTypeFormat=self.lineType
        if self.lineTypeFormat=='Solid Line':
            pen.setStyle(Qt.SolidLine)
        elif self.lineTypeFormat=='Dash Line':
            pen.setStyle(Qt.DashLine)
        elif self.lineTypeFormat=='Dash Dot Line':
            pen.setStyle(Qt.DashDotLine)
        elif self.lineTypeFormat=="Dot Line":
            pen.setStyle(Qt.DotLine)
        elif self.lineTypeFormat=='Dash Dot Dot Line':
            pen.setStyle(Qt.DashDotDotLine)
        qp.setPen(pen)
        qp.drawLine(self.pos1[0], self.pos1[1], self.pos2[0], self.pos2[1])
        qp.end()

    def mousePressEvent(self, event):
        if event.buttons() and Qt.LeftButton:
            self.pos1[0], self.pos1[1]=event.pos().x(), event.pos().y()

    def mouseReleaseEvent(self, event):
        self.lineType=self.ui.listWidgetLineType.currentItem().text()
        self.pos2[0], self.pos2[1]=event.pos().x(), event.pos().y()
        self.update()

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
