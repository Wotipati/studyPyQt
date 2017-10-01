# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QHBoxLayout, QVBoxLayout, QWidget
from PyQt5.QtCore import QCoreApplication


class Buttons(QMainWindow):

    def __init__(self):
        super().__init__()

        self.button1 = QPushButton('No.1', self)
        self.button2 = QPushButton('No.2', self)
        self.button3 = QPushButton('No.3', self)
        self.button_row = QPushButton('row')
        self.button_line = QPushButton('line')

        self.main_layout = QVBoxLayout()
        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)

        self.init_ui()

    def init_ui(self):

        self.button1.clicked.connect(QCoreApplication.instance().quit)
        self.button1.resize(self.button1.sizeHint())

        self.button2.clicked.connect(QCoreApplication.instance().quit)
        self.button2.resize(self.button2.sizeHint())

        self.button3.clicked.connect(QCoreApplication.instance().quit)
        self.button3.resize(self.button3.sizeHint())

        self.button_row.clicked.connect(self.change_layout_row)
        self.button_row.resize(self.button_row.sizeHint())

        self.button_line.clicked.connect(self.change_layout_line)
        self.button_line.resize(self.button_line.sizeHint())

        select_button_layout = QHBoxLayout()
        select_button_layout.addWidget(self.button_line)
        select_button_layout.addWidget(self.button_row)
        self.main_layout.addLayout(select_button_layout)

        self.change_layout_line()

        self.main_widget.setLayout(self.main_layout)

        self.setGeometry(200, 300, 800, 450)
        self.setWindowTitle('Layout')
        self.show()

    def change_layout_row(self):
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.button1)
        button_layout.addWidget(self.button2)
        button_layout.addWidget(self.button3)
        self.main_layout.addLayout(button_layout)

        self.button_row.setStyleSheet('QPushButton{color: red}')
        self.button_line.setStyleSheet('QPushButton{color: black}')

    def change_layout_line(self):
        button_layout = QVBoxLayout()
        button_layout.addWidget(self.button1)
        button_layout.addWidget(self.button2)
        button_layout.addWidget(self.button3)
        self.main_layout.addLayout(button_layout)

        self.button_row.setStyleSheet('QPushButton{color: black}')
        self.button_line.setStyleSheet('QPushButton{color: red}')


def main():
    app = QApplication(sys.argv)
    window = Buttons()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
