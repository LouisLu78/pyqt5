# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2019/12/23

import sqlite3, sys
from PyQt5.QtWidgets import QApplication, QDialog, QTableWidgetItem
from sqlite3 import Error
from demos.demoDisplayRowsOfTable import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButtonDispRow.clicked.connect(self.displayrow)

    def displayrow(self):
        sqlStatement = 'Select From '+ self.ui.lineEditTableName.text()

        try:
            conn = sqlite3.connect(self.ui.lineEditDBName.text() + '.db')
            cur = conn.cursor()
            cur.execute(sqlStatement)
            rows=cur.fetchall()
            rowNo=0
            for tuple in rows:
                self.ui.labelResponse.setText("")
                colNo = 0
                for columns in tuple:
                    oneColumn = QTableWidgetItem(columns)
                    self.ui.tableWidget.setItem(rowNo, colNo, oneColumn)
                    colNo += 1
                rowNo += 1

        except Error as e:
            self.ui.tableWidget.clear()
            self.ui.labelResponse.setText("Error in accessing table")

        finally:
            conn.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
