# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2019/12/26
# Email: gq4350lu@hotmail.com

import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtCore import Qt
from demos.demoMouseClicks import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)

    def mousePressEvent(self, event):
        if event.buttons() & Qt.LeftButton:
            x = event.x()
            y = event.y()
            text = 'x:{}, y:{}'.format(x, y)
            self.ui.labelPress.setText('Mouse button pressed at ' +text)

    def mouseReleaseEvent(self, event):
        x = event.x()
        y = event.y()
        text = 'x:{}, y:{}'.format(x, y)
        self.ui.labelRelease.setText('Mouse button released at ' +text)

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())

