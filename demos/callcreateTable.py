# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2019/12/22

import sqlite3, sys
from PyQt5.QtWidgets import QApplication, QDialog
from sqlite3 import Error
from demos.demoCreateTable import *

tabledefinition=''
class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButtonCreateTable.clicked.connect(self.createtable)
        self.ui.pushButtonAddColumn.clicked.connect(self.addcolumn)

    def addcolumn(self):
        global tabledefinition
        if tabledefinition=='':
            tabledefinition='Create Table if not exists'+ self.ui.lineEditTableName.text()+'('\
                            +self.ui.lineEditColumnName.text()+'  '+\
                            self.ui.comboBoxDataType.itemText(self.ui.comboBoxDataType.currentIndex())
        else:
            tabledefinition+=','+self.ui.lineEditColumnName.text()+'  '+\
                            self.ui.comboBoxDataType.itemText(self.ui.comboBoxDataType.currentIndex())
            self.ui.lineEditColumnName.setText("")
            self.ui.lineEditColumnName.setFocus()

    def createtable(self):
        global tabledefinition
        try:
            conn=sqlite3.connect(self.ui.lineEditDBName.text()+'.db')
            self.ui.labelResponse.setText('The database is connected.')
            c=conn.cursor()
            tabledefinition+=');'
            c.execute(tabledefinition)

        except Error as e:
            self.ui.labelResponse.setText('Some mistakes have occured.')

        finally:
            conn.close()

if __name__=='__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())