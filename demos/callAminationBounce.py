# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2019/12/28
# Email: gq4350lu@hotmail.com

import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtCore import QRect, QPropertyAnimation
from demos.demoAnimation3 import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButtonBounce.clicked.connect(self.startAnimation)

    def startAnimation(self):
        self.anim = QPropertyAnimation(self.ui.labelpic, b'geometry')
        self.anim.setDuration(10000)
        self.anim.setKeyValueAt(0, QRect(0,0, 100, 80));
        self.anim.setKeyValueAt(0.5, QRect(160, 160, 200, 80))
        self.anim.setKeyValueAt(0, QRect(400, 0, 100, 80))
        self.anim.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())