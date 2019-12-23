# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2019/12/23

import sqlite3, sys
from PyQt5.QtWidgets import QApplication, QDialog
from sqlite3 import Error
from demos.demoInsertRowsInTable import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButtonInsertRow.clicked.connect(self.insertrows)

    def insertrows(self):
        sqlStatement='Insert Into' + self.ui.lineEditTableName.text()+\
                     "VALUES('"+self.ui.lineEditEmail.text()+"','"+self.ui.lineEditPassword.text()+"')"

        try:
            conn = sqlite3.connect(self.ui.lineEditDBName.text() + '.db')
            with conn:
                cur = conn.cursor()
                cur.execute(sqlStatement)
                self.ui.labelResponse.setText('The row is successfully inserted.')

        except Error as e:
            self.ui.labelResponse.setText('Error occured in inserting the row.')

        finally:
            conn.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
