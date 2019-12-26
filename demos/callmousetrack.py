# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2019/12/26
# Email: gq4350lu@hotmail.com

import sys
from PyQt5.QtWidgets import QDialog, QApplication
from demos.demoMousetrack import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
        self.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        x=event.x()
        y=event.y()
        text= 'x:{}, y:{}'.format(x,y)
        self.ui.labelCoordinate.setText(text)

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())


