# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2019/12/25

import sqlite3, sys
from PyQt5.QtWidgets import QApplication, QDialog, QTableWidgetItem
from sqlite3 import Error
from demos.demoChangePassword import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButtonChangePass.clicked.connect(self.changepass)

    def changepass(self):
        selectStatement = "SELECT EmailAddress, Password FROM Users where EmailAddress like'"+\
                          self.ui.lineEditEmail.text() + "'and Password like '" +\
                          self.ui.lineEditOldPass.text() + "'"
        try:
            conn = sqlite3.connect("ECommerce.db")
            cur = conn.cursor()
            cur.execute(selectStatement)
            row=cur.fetchone()
            if row is None:
                self.ui.labelResponse.setText("Sorry, Incorrect email address or password")
            else:
                if self.ui.lineEditNewPass.text()==self.ui.lineEditRe_Pass.text():
                    updateStatement = "UPDATE Users set Password = '" +self.ui.lineEditNewPass.text() +\
                                      "' WHERE EmailAddress like'"+self.ui.lineEditEmail.text() + "'"
                    with conn:
                        cur.execute(updateStatement)
                        self.ui.labelResponse.setText('The password is successfully changed.')
                else:
                    self.ui.labelResponse.setText('The two passwords don\'t match.')

        except Error as e:
            self.ui.labelResponse.setText('Error in accessing the row')

        finally:
            conn.close()

if __name__=='__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
