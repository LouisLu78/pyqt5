# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2019/12/21

import sys, time
import asyncio
from PyQt5.QtWidgets import QDialog, QApplication
from quamash import QEventLoop
from demos.demoTwoProgressBarsAsync import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButtonStart.clicked.connect(self.invokeAsync)
        self.show()

    def invokeAsync(self):
