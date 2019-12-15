# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2019/12/15

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from demos.demoDockWidget import *

class Appwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = Appwindow()
    w.show()
    sys.exit(app.exec_())