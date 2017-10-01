# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QPushButton, QHBoxLayout, QVBoxLayout, QWidget
from PyQt5.QtCore import QCoreApplication


class Buttons(QMainWindow):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):

        wid = QWidget(self)
        self.setCentralWidget(wid)

        button1 = QPushButton('No.1', self)
        button1.clicked.connect(QCoreApplication.instance().quit)
        button1.resize(button1.sizeHint())

        button2 = QPushButton('No.2', self)
        button2.clicked.connect(QCoreApplication.instance().quit)
        button2.resize(button2.sizeHint())

        button3 = QPushButton('No.3', self)
        button3.clicked.connect(QCoreApplication.instance().quit)
        button3.resize(button3.sizeHint())

        layout_row = QHBoxLayout()
        layout_row.addWidget(button1)
        layout_row.addWidget(button2)
        layout_row.addWidget(button3)
        wid.setLayout(layout_row)

        self.setGeometry(200, 300, 800, 450)
        self.setWindowTitle('Layout')
        self.show()


def main():
    app = QApplication(sys.argv)
    window = Buttons()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
