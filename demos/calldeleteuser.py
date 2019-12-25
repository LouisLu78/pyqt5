# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2019/12/25

import sqlite3, sys
from PyQt5.QtWidgets import QApplication, QDialog, QTableWidgetItem
from sqlite3 import Error
from demos.demoDeleteUser import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButtonDeleteuser.clicked.connect(self.deleteuser)
        self.ui.pushButtonYes.clicked.connect(self.confirmdelete)
        self.ui.labelsure.hide()
        self.ui.pushButtonYes.hide()
        self.ui.pushButtonNo.hide()

    def deleteuser(self):
        selectStatement = "SELECT EmailAddress, Password FROM Users where EmailAddress like'" + \
                          self.ui.lineEditEmail.text() + "'and Password like '" + \
                          self.ui.lineEditPassword.text() + "'"
        try:
            conn = sqlite3.connect("ECommerce.db")
            cur = conn.cursor()
            cur.execute(selectStatement)
            row = cur.fetchone()
            if row is None:
                self.ui.labelsure.hide()
                self.ui.pushButtonYes.hide()
                self.ui.pushButtonNo.hide()
                self.ui.labelResponse.setText("Sorry, Incorrect email address or password")
            else:
                self.ui.labelsure.show()
                self.ui.pushButtonYes.show()
                self.ui.pushButtonNo.show()
                self.ui.labelResponse.setText('')
        except Error as e:
            self.ui.labelResponse.setText("Error in accessing user account")
        finally:
            conn.close()

    def confirmdelete(self):
        deleteStatement="DELETE FROM Users where EmailAddress like'" + \
                          self.ui.lineEditEmail.text() + "'and Password like '" + \
                          self.ui.lineEditPassword.text() + "'"
        try:
            conn = sqlite3.connect("ECommerce.db")
            cur = conn.cursor()
            cur.execute(deleteStatement)
            self.ui.labelResponse.setText("User successfully deleted")
        except Error as e:
            self.ui.labelResponse.setText("Error in deleting user account")
        finally:
            conn.close()

if __name__=='__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
