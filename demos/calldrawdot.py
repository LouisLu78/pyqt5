# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2019/12/26
# Email: gq4350lu@hotmail.com

import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen
from demos.demoDrawDot import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
        self.pos1=[0,0]

    def paintEvent(self, event):
        qp=QPainter()
        qp.begin(self)
        pen=QPen(Qt.black, 5)
        qp.setPen(pen)
        qp.drawPoint(self.pos1[0],self.pos1[1])
        qp.end()

    def mousePressEvent(self, event):
        if event.buttons() and Qt.LeftButton:
            self.pos1[0],self.pos1[1]=event.pos().x(),event.pos().y()
            self.update()

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())


