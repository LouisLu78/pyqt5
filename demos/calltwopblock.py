# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2019/12/21

import sys, threading, time
from PyQt5.QtWidgets import QDialog, QApplication
from demos.demoTwoProgressBarsLocks import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
        self.show()

class MyThread(threading.Thread):
    counter=0
    def __init__(self, w, ProgressBar):
        threading.Thread.__init__(self)
        self.w=w
        self.counter=0
        self.ProgressBar=ProgressBar

    def run(self):
        print("Starting " + self.name + "n")
        lock=threading.Lock()
        lock.acquire()
        while self.counter <= 100:
            time.sleep(1)
            self.ProgressBar.setValue(self.counter)
            self.counter+=10
            lock.release()
            print("Exiting " + self.name+ 'n')

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    thread1=MyThread(w, w.ui.progressBarFileDownload)
    thread2=MyThread(w, w.ui.progressBarVirusScan)
    thread1.start()
    thread2.start()
    w.exec()
    thread1.join()
    thread2.join()
    sys.exit(app.exec_())