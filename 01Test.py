#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import *


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        button = QPushButton('button')

        layout = QGridLayout()
        layout.addWidget(button)
        self.setLayout(layout)
        self.setWindowTitle("Button")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()

    main_window.show()
    sys.exit(app.exec_())


    main.window