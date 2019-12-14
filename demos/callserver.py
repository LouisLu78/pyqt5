# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2019/12/14

import sys, time
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtCore import QCoreApplication
import socket
from threading import Thread
from socketserver import ThreadingMixIn
conn=None
from demos.demoServer import *

class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.textEditMessages = self.ui.textEditMessage
        self.ui.pushButtonSend.clicked.connect(self.dispMessage)

    def dispMessage(self):
        text=self.ui.lineEditMessage.text()
        global conn
        conn.send(text.encode('utf-8'))
        self.ui.textEditMessage.append("Server:"+self.ui.lineEditMessage.text())
        self.ui.lineEditMessage.setText('')

class ServerThread(Thread):
    def __init__(self, window):
        Thread.__init__(self)
        self.window=window

    def run(self):
        TCP_IP = '0.0.0.0'
        TCP_PORT = 80
        BUFFER_SIZE = 1024
        tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        tcpServer.bind((TCP_IP, TCP_PORT))
        threads = []
        tcpServer.listen(4)
        while True:
            global conn
            (conn, (ip, port)) = tcpServer.accept()
            newthread = ClientThread(ip, port, self.window)
            newthread.start()
            threads.append(newthread)
            for t in threads:
                t.join()

class ClientThread(Thread):
    def __init__(self, ip, port, window):
        Thread.__init__(self)
        self.window, self.ip, self.port=window, ip, port

    def run(self):
        while True:
            global conn
            data=conn.recv(1024)
            self.window.textEditMessage.append('Client:'+data.decode('utf-8'))

if __name__=="__main__":
    app = QApplication(sys.argv)
    window = Window()
    serverThread=ServerThread(window)
    serverThread.start()
    window.exec()
    sys.exit(app.exec_())














