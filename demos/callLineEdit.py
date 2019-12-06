# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2019/12/2
#The codes below are copied from textbook.

import sys

from PyQt5.QtWidgets import QDialog, QApplication
from demos.demoLineEdit import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.ButtonClickMe.clicked.connect(self.dispmessage)
        self.show()
    def dispmessage(self):
        self.ui.labelResponse.setText("Hello "
        +self.ui.lineEditName.text())
if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())


