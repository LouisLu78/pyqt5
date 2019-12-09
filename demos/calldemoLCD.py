# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2019/12/9

import sys
from PyQt5.QtWidgets import QDialog, QApplication
from demos.demoLCD import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)

        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.showlcd)
        timer.start(100)


    def showlcd(self):
        time=QtCore.QTime.currentTime()
        text = time.toString('hh:mm')
        self.ui.lcdNumber.display(text)

if __name__=='__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())