# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2019/12/11

import sys
from PyQt5.QtWidgets import QDialog, QApplication, QColorDialog
from PyQt5.QtGui import QColor
from demos.demoColorDialog import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)

        col = QColor(0, 0, 0)
        self.ui.framecolor.setStyleSheet("QWidget{background-color: %s}" % col.name())
        self.ui.pushButtoncolor.clicked.connect(self.dispcolor)

    def dispcolor(self):
        col = QColorDialog.getColor()
        if col.isValid():
            self.ui.framecolor.setStyleSheet("QWidget{background-color: %s}" % col.name())
            self.ui.labelcolor.setText("You have selected the color with code: " + str(col.name()))

if __name__=='__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
