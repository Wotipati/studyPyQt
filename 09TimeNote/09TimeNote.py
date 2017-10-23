# -*- coding: utf-8 -*-

import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QVBoxLayout,\
                            QLCDNumber, QTextEdit
from PyQt5.QtCore import QCoreApplication, QTimer
from PyQt5.QtGui import QIcon

from stopwatch import Stopwatch

class Timenote(QMainWindow):

    def __init__(self):
        super().__init__()

        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)

        self.layout_main = QVBoxLayout()

        self.init_ui()

    def init_ui(self):
        stopwatch = Stopwatch()
        self.main_widget.setLayout(stopwatch.layout_main)

        exit_action = QAction(QIcon('./icon/exit.png'), '&Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit Application')
        exit_action.triggered.connect(QCoreApplication.instance().quit)

        toolbar = self.addToolBar('&Toolbar')
        toolbar.addAction(exit_action)

        self.setGeometry(500, 500, 300, 200)
        self.setWindowTitle('stop watch')
        self.show()


def main():
    app = QApplication(sys.argv)
    window = Timenote()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()