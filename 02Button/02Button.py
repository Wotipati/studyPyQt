# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication, QToolTip
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QFont


class Button(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('this is <b>window widget<b>')

        quitButton = QPushButton("quit", self)
        quitButton.clicked.connect(QCoreApplication.instance().quit)
        quitButton.resize(quitButton.sizeHint())
        quitButton.move(20, 50)
        quitButton.setToolTip('You can quit this app')

        statusButton = QPushButton("myFirstButton", self)
        statusButton.clicked.connect(self.statusButtonClicked)
        statusButton.resize(statusButton.sizeHint())

        self.statusBar()

        self.setGeometry(200, 300, 200, 150)
        self.setWindowTitle('myFirstButton')
        self.show()

    def statusButtonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' is pushed')


def main():
    app = QApplication(sys.argv)
    window = Button()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
