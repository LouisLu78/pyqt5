# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2019/12/8

import sys
from PyQt5.QtWidgets import QDialog, QApplication
from demos.demoComboBox import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.comboBoxAccountType.currentIndexChanged.connect(self.dispAccountType)

    def dispAccountType(self):
        self.ui.labellAccountType.setText("You have selected "+
                                         self.ui.comboBoxAccountType.itemText
                                         (self.ui.comboBoxAccountType.currentIndex())+'.')

if __name__=='__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())