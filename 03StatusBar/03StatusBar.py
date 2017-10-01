# -*- coding: utf-8 -*-
import sys
import datetime
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication, QToolTip
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QCoreApplication


class StatusBar(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.time_draw)
        self.timer.start(10)

    def init_ui(self):

        QToolTip.setFont(QFont('SansSerif', 10))

        quit_button = QPushButton("quit", self)
        quit_button.clicked.connect(QCoreApplication.instance().quit)
        quit_button.resize(quit_button.sizeHint())
        quit_button.move(20, 50)
        quit_button.setToolTip('You can quit this app')

        self.statusBar()

        self.setGeometry(200, 300, 200, 150)
        self.setWindowTitle('Status Bar')
        self.show()

    def time_draw(self):
        t = datetime.datetime.today()
        t_str = t.strftime("%Y-%m-%d %H:%M:%S:%f")
        self.statusBar().showMessage(t_str)


def main():
    app = QApplication(sys.argv)
    window = StatusBar()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
