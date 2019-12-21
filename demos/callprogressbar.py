# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2019/12/8

import sys
from PyQt5.QtWidgets import QDialog, QApplication
from demos.demoProgressBar import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButtonnStart.clicked.connect(self.updatebar)

    def updatebar(self):
        x = 0
        while x <= 100:
            x += 0.0001
            self.ui.progressBar.setValue(x)

if __name__=='__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
