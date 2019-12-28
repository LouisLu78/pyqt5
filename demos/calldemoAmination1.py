# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2019/12/28
# Email: gq4350lu@hotmail.com

import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtCore import QRect, QPropertyAnimation
from demos.demoAnimation1 import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButtonMoveDown.clicked.connect(self.startAmination)

    def startAmination(self):
        self.anim=QPropertyAnimation(self.ui.labelpic, b'geometry')
        self.anim.setDuration(10000)
        self.anim.setStartValue(QRect(160, 70, 80, 80))
        self.anim.setEndValue(QRect(160, 70, 320, 460))
        self.anim.start()

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())