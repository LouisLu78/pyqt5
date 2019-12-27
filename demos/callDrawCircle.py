# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2019/12/27
# Email: gq4350lu@hotmail.com

import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPainter
from demos.demoDrawCircle import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
        self.pos1, self.pos2 = [0, 0], [0, 0]

    def paintEvent(self, event):
        width=self.pos2[0]-self.pos1[0]
        height=self.pos2[1]-self.pos1[1]
        qp=QPainter()
        qp.begin(self)
        rect=QRect(self.pos1[0],self.pos1[1],width,height)
        startAngle=0
        arcLength=360*16
        qp.drawArc(rect,startAngle,arcLength)
        qp.end()

    def mousePressEvent(self, event):
        if event.buttons() and Qt.LeftButton:
            self.pos1[0], self.pos1[1] = event.pos().x(), event.pos().y()

    def mouseReleaseEvent(self, event):
        self.pos2[0], self.pos2[1] = event.pos().x(), event.pos().y()
        self.update()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())

