# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2019/12/22

import sqlite3, sys
from PyQt5.QtWidgets import QApplication, QDialog
from sqlite3 import Error
from demos.demoDatabase import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
        self.show()
        self.ui.pushButtonCreateDB.clicked.connect(self.createdatabase)

    def createdatabase(self):
        try:
            conn=sqlite3.connect(self.ui.lineEditDBName.text()+'.db')
            self.ui.labelResponse.setText('The database is created.')

        except Error as e:
            self.ui.labelResponse.setText('Some mistakes have occured.')

        finally:
            conn.close()

if __name__=='__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())