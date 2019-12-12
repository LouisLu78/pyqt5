# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2019/12/12

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QFileDialog
from demos.demoFileDialog import *

class MyForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.actionOpen.triggered.connect(self.openfiledialog)
        self.ui.actionSave.triggered.connect(self.savefiledialog)

    def openfiledialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file','/home')
        if fname[0]:
            with open(fname[0], 'r') as f:
                data = f.read()
            self.ui.textEdit.setText(data)

    def savefiledialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()","",""
                                                        "All Files(*);;Text Files(*.txt)", options = options)
        text = self.ui.textEdit.toPlainText()
        with open(fileName, 'w') as f:
            f.write(text)

if __name__=='__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())