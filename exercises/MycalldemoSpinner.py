# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2019/12/6
# If not explicitly pointed out, all the codes are written by myself.

import sys
from PyQt5.QtWidgets import QDialog, QApplication
from exercises.MydemoSpinner import *

class MyForm(QDialog):

    def __init__(self):
        super().__init__()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.spinBoxBookQty.editingFinished.connect(self.result1)
        self.ui.doubleSpinBoxSugarWeight.editingFinished.connect(self.result2)
        self.ui.pushButton.clicked.connect(self.total)

    def result1(self):
        bookPrice = eval(self.ui.lineEditBookPrice.text()) if len(self.ui.lineEditBookPrice.text()) else 0
        totalBookAmount = self.ui.spinBoxBookQty.value() * bookPrice
        self.ui.lineEditBookAmount.setText(str(round(totalBookAmount,2)))
        return totalBookAmount

    def result2(self):
        sugarPrice = eval(self.ui.lineEditSugarPrice.text()) if len(self.ui.lineEditSugarPrice.text()) else 0
        totalSugarAmount = self.ui.doubleSpinBoxSugarWeight.value() * sugarPrice
        self.ui.lineEditSugarAmount.setText(str(round(totalSugarAmount, 2)))
        return totalSugarAmount

    def total(self):
        totalAmount =self.result1() + self.result2()
        self.ui.labelTotalAmount.setText(str(round(totalAmount,2)))

if __name__=='__main__':
    app=QApplication(sys.argv)
    w=MyForm()
    w.show()
    sys.exit(app.exec_())