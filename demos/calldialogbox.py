# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2019/12/11

import sys
from PyQt5.QtWidgets import QDialog, QApplication, QInputDialog
from demos.demoInputDialog import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButtoncountry.clicked.connect(self.dispmessage)

    def dispmessage(self):
        countries = ("Albania", "Algeria", "Andorra", "Angola",
                     "Antigua and Barbuda", "Argentina", "Armenia", "Aruba",
                     "Australia", "Austria", "Azerbaijan")
        countryname, ok=QInputDialog.getItem(self, 'Input dialog', 'List of countries', countries, 0, True)
        if countryname and ok:
            self.ui.lineEditcountry.setText(countryname)

if __name__=='__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())