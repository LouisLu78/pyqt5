# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2019/12/19

import sys, threading, time
from PyQt5.QtWidgets import QDialog, QApplication
from demos.demoProgressBarThread import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)

class MyThread(threading.Thread):
    counter=0
    def __init__(self,w):
        threading.Thread.__init__(self)
        self.w=w
        self.counter=0

    def run(self):
        print("Starting " + self.name)
        while self.counter <= 100:
            time.sleep(1)
            w.ui.progressBar.setValue(self.counter)
            self.counter+=10
            print("Exiting " + self.name)

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    thread1 = MyThread(w)
    thread1.start()
    w.exec()
    sys.exit(app.exec_())


