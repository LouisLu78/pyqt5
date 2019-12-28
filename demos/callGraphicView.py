# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2019/12/28
# Email: gq4350lu@hotmail.com


import sys
from PyQt5.QtWidgets import QDialog, QApplication, QGraphicsScene, QGraphicsPixmapItem
from PyQt5.QtGui import QPixmap
from demos.demoGraphicsView import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
        self.scene=QGraphicsScene(self)
        pixmap=QPixmap()
        pixmap.load(r"C:\Users\Basanwei\Pictures\1454533979.jpg")
        item=QGraphicsPixmapItem(pixmap)
        self.scene.addItem(item)
        self.ui.graphicsView.setScene(self.scene)

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())