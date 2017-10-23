# -*- coding: utf-8 -*-

import sys
import datetime
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QLabel, QAction, QVBoxLayout,\
                            QLCDNumber, QTextEdit
from PyQt5.QtCore import QCoreApplication, QTimer
from PyQt5.QtGui import QIcon


class Timenote(QMainWindow):

    def __init__(self):
        super().__init__()

        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)

        self.time_history = QTextEdit()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.time_count)
        self.sec  = 00
        self.min  = 00
        self.hour = 00
        self.start_time = None
        self.lcd = QLCDNumber(self)

        self.init_ui()

    def init_ui(self):
        time = "{0}:{1}:{2}".format(self.hour, self.min, self.sec)
        self.lcd.setDigitCount(len(time))
        self.lcd.display(time)

        button_start = QPushButton("start", self)
        button_start.clicked.connect(self.timer_start)

        button_stop = QPushButton("stop", self)
        button_stop.clicked.connect(lambda: self.timer.stop())

        button_reset = QPushButton("reset", self)
        button_reset.clicked.connect(self.timer_reset)

        layout_main = QVBoxLayout()
        layout_main.addWidget(self.lcd)
        layout_main.addWidget(button_start)
        layout_main.addWidget(button_stop)
        layout_main.addWidget(button_reset)

        self.main_widget.setLayout(layout_main)

        exit_action = QAction(QIcon('./icon/exit.png'), '&Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit Application')
        exit_action.triggered.connect(QCoreApplication.instance().quit)

        toolbar = self.addToolBar('&Toolbar')
        toolbar.addAction(exit_action)

        self.setGeometry(500, 500, 300, 200)
        self.setWindowTitle('stop watch')
        self.show()

    def timer_start(self):
        self.timer.start(1000)

    def timer_reset(self):
        self.timer.stop()
        self.sec  = 00
        self.min  = 00
        self.hour = 00

        time = "{0}:{1}:{2}".format(self.hour, self.min, self.sec)
        self.lcd.setDigitCount(len(time))
        self.lcd.display(time)

    def time_count(self):
        if self.sec < 59:
            self.sec += 1

        else:
            if self.min < 59:
                self.sec = 00
                self.min += 1

            elif self.min == 59:
                self.hour += 1
                self.min = 00
                self.sec = 00

        time = "{0}:{1}:{2}".format(self.hour, self.min, self.sec)
        self.lcd.setDigitCount(len(time))
        self.lcd.display(time)


def main():
    app = QApplication(sys.argv)
    window = Timenote()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()