# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2019/12/13

import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtWebEngineWidgets import QWebEngineView
from demos.demoBrowser import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButtonGO.clicked.connect(self.dispSite)

    def dispSite(self):
        self.ui.widget.load(QUrl(self.ui.lineEditURL.text()))

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())