# -*- coding: utf-8 -*-

import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QGridLayout, QVBoxLayout, QHBoxLayout,\
                            QLCDNumber, QTextEdit, QAction, QLabel
from PyQt5.QtCore import QCoreApplication, QTimer
from PyQt5.QtGui import QIcon
from stopwatch import Stopwatch


class Timenote(QMainWindow):

    def __init__(self):
        super().__init__()

        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)

        self.label_now_subject = QLabel
        self.layout_main = QHBoxLayout()
        self.layout_user = QVBoxLayout()
        self.layout_grid = QGridLayout()
        self.buttons_subject = []
        self.init_ui()

    def init_ui(self):
        self.layout_user.addWidget(self.label_now_subject)

        stopwatch = Stopwatch()
        self.layout_user.addLayout(stopwatch.layout_main)
        self.main_widget.setLayout(self.layout_user)

        labels_subject= ['Meeting', 'Implementation', 'Experiment',
                        'Research', 'Paper survey', 'Writing a paper',
                        'Making slides', 'Taking a class', 'Chores']

        positions_subject = [(i,j) for i in range(3) for j in range(3)]

        for position, subject in zip(positions_subject, labels_subject):
            button = QPushButton(subject)
            self.buttons_subject.append(button)
            self.layout_grid.addWidget(button, *position)

        self.layout_user.addLayout(self.layout_grid)

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