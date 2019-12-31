# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2019/12/27
# Email: gq4350lu@hotmail.com
# If not explicitly pointed out, all the codes are written by myself.

import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen
from exercises.MydemoDrawDiffLine import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Draw_Lines")
        self.lineType='SolidLine'
        self.pos1, self.pos2 = [0, 0], [0, 0]

    def paintEvent(self, event):
        qp=QPainter()
        qp.begin(self)
        pen=QPen(Qt.red, 4)
        pen.setStyle(eval('Qt.'+self.lineType))
        qp.setPen(pen)
        qp.drawLine(self.pos1[0], self.pos1[1], self.pos2[0], self.pos2[1])
        qp.end()

    def mousePressEvent(self, event):
        if event.buttons() and Qt.LeftButton:
            self.pos1[0], self.pos1[1]=event.pos().x(), event.pos().y()

    def mouseReleaseEvent(self, event):
        self.lineType = self.ui.listWidgetLineType.currentItem().text()
        self.pos2[0], self.pos2[1]=event.pos().x(), event.pos().y()
        self.update()

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())