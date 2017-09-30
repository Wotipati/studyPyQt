# -*- coding: utf-8 -*-
import sys
import datetime
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication, QToolTip
from PyQt5.QtCore import QCoreApplication, QTimer
from PyQt5.QtGui import QFont


class StatusBar(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        QToolTip.setFont(QFont('SansSerif', 10))

        quit_button = QPushButton("quit", self)
        quit_button.clicked.connect(QCoreApplication.instance().quit)
        quit_button.resize(quit_button.sizeHint())
        quit_button.move(20, 50)
        quit_button.setToolTip('You can quit this app')

        self.statusBar()

        timer = QTimer()
        timer.timeout.connect(self.time_draw)
        timer.start(1000)

        self.setGeometry(200, 300, 200, 150)
        self.setWindowTitle('Status Bar')
        self.show()

    def time_draw(self):
        t = datetime.datetime.today()
        t_str = t.strftime("%Y-%m-%d %H:%M:%S")
        self.statusBar().showMessage(t_str)


def main():
    app = QApplication(sys.argv)
    window = StatusBar()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
