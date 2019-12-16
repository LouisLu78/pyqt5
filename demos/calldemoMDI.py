# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2019/12/16

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QFileDialog
from demos.demoMDI import *

class MyForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.mdiArea.addSubWindow(self.ui.subwindow)
        self.ui.mdiArea.addSubWindow(self.ui.subwindow_2)
        self.ui.actionSubWindow_View.triggered.connect(self.SubWindow_View)
        self.ui.actionTab_View.triggered.connect(self.Tab_View)
        self.ui.actionCascade_View.triggered.connect(self.Cascade_View)
        self.ui.actionTile_View.triggered.connect(self.Tile_View)


    def SubWindow_View(self):
        self.ui.mdiArea.setViewMode(0)
    def Tab_View(self):
        self.ui.mdiArea.setViewMode(1)
    def Cascade_View(self):
        self.ui.mdiArea.cascadeSubWindows()
    def Tile_View(self):
        self.ui.mdiArea.tileSubWindows()

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())