# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2019/12/6

import sys
from PyQt5.QtWidgets import QDialog, QApplication
from demos.demoListWidget1 import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.listWidgetDiagnosis.itemClicked.connect(self.dispSelectedTest)

    def dispSelectedTest(self):
        self.ui.labelTest.setText('You have selected:\n '
                                  +self.ui.listWidgetDiagnosis.currentItem().text())

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
