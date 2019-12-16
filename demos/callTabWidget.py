# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2019/12/16

import sys
from PyQt5.QtWidgets import QDialog, QApplication
from demos.demoTabwidget import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)

if __name__=='__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())