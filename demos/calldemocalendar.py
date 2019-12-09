# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2019/12/9

import sys
from PyQt5.QtWidgets import QDialog, QApplication
from demos.demoCalendar import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.calendarWidget.selectionChanged.connect(self.dispdate)

    def dispdate(self):
        self.ui.dateEdit.setDate(self.ui.calendarWidget.selectedDate())

if __name__=='__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())