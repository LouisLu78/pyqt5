# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2019/12/5

import sys
from PyQt5.QtWidgets import QDialog, QApplication
from demos.demoCalculator import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButtonPlus.clicked.connect(self.addtwonum)
        self.ui.pushButtonSubtract.clicked.connect(self.subtracttwonum)
        self.ui.pushButtonMultiply.clicked.connect(self.multiplytwonum)
        self.ui.pushButtonDevide.clicked.connect(self.devidetwonum)

    def addtwonum(self):
        a = eval(self.ui.lineEditFirstNumber.text()) if len(self.ui.lineEditFirstNumber.text()) else 0
        b = eval(self.ui.lineEditSecondNumber.text()) if len(self.ui.lineEditSecondNumber.text()) else 0
        sum=a+b
        return self.ui.labelResult.setText('Addition: '+str(sum))

    def subtracttwonum(self):
        a = eval(self.ui.lineEditFirstNumber.text()) if len(self.ui.lineEditFirstNumber.text()) else 0
        b = eval(self.ui.lineEditSecondNumber.text()) if len(self.ui.lineEditSecondNumber.text()) else 0
        diff = a - b
        return self.ui.labelResult.setText("Substraction: " + str(diff))

    def multiplytwonum(self):
        a = eval(self.ui.lineEditFirstNumber.text()) if len(self.ui.lineEditFirstNumber.text()) else 0
        b = eval(self.ui.lineEditSecondNumber.text()) if len(self.ui.lineEditSecondNumber.text()) else 0
        mul=a*b
        return self.ui.labelResult.setText("Multiplication: " + str(mul))

    def devidetwonum(self):
        a = eval(self.ui.lineEditFirstNumber.text()) if len(self.ui.lineEditFirstNumber.text()) else 0
        b = eval(self.ui.lineEditSecondNumber.text()) if len(self.ui.lineEditSecondNumber.text()) else 0
        div = a / b
        return self.ui.labelResult.setText("Division: " + str(div))

if __name__=='__main__':
    app=QApplication(sys.argv)
    w=MyForm()
    w.show()
    sys.exit(app.exec_())
