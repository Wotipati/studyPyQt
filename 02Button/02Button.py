# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication, QToolTip
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QFont


class Button(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):

        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('this is <b>window widget<b>')

        quit_button = QPushButton("quit", self)
        quit_button.clicked.connect(QCoreApplication.instance().quit)
        quit_button.resize(quit_button.sizeHint())
        quit_button.move(20, 50)
        quit_button.setToolTip('You can quit this app')

        status_button = QPushButton("myFirstButton", self)
        status_button.clicked.connect(self.button_clicked)
        status_button.resize(status_button.sizeHint())

        self.statusBar()

        self.setGeometry(200, 300, 200, 150)
        self.setWindowTitle('myFirstButton')
        self.show()

    def button_clicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' is pushed')


def main():
    app = QApplication(sys.argv)
    window = Button()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
