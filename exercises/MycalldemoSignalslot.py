# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2019/12/30
# Email: gq4350lu@hotmail.com
# If not explicitly pointed out, all the codes are written by myself.

import sys
from PyQt5.QtWidgets import QDialog, QApplication
from exercises.Mydemosignalslot import *


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
        self.show()

if __name__=='__main__':
    app=QApplication(sys.argv)
    w=MyForm()
    w.show()
    sys.exit(app.exec_())