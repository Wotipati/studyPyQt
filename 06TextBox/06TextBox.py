# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QLabel, QAction, QVBoxLayout, QHBoxLayout,\
                            QLineEdit, QTextEdit, QPushButton
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon


class Textbox(QMainWindow):

    def __init__(self):
        super().__init__()

        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)
        self.main_layout = QVBoxLayout()
        self.text_box_layout = QHBoxLayout()
        self.main_text_box = QLineEdit()
        self.sub_text_box = QTextEdit()
        self.label = QLabel()
        self.label_history = QLabel('history')

        self.init_ui()

    def init_ui(self):

        add_button = QPushButton("Add", self)
        add_button.clicked.connect(self.add_history)

        self.main_text_box.textChanged.connect(self.change_text)

        self.text_box_layout.addWidget(self.main_text_box)
        self.text_box_layout.addWidget(add_button)
        self.main_layout.addLayout(self.text_box_layout)
        self.main_layout.addWidget(self.label)
        self.main_layout.addWidget(self.label_history)
        self.main_layout.addWidget(self.sub_text_box)
        self.main_widget.setLayout(self.main_layout)

        exit_action = QAction(QIcon('./icon/exit.png'), '&Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit Application')
        exit_action.triggered.connect(QCoreApplication.instance().quit)

        toolbar = self.addToolBar('&Toolbar')
        toolbar.addAction(exit_action)

        self.setGeometry(500, 500, 300, 200)
        self.setWindowTitle('textBox')
        self.show()

    def change_text(self, text):
        self.label.setText(text)
        self.label.adjustSize()

    def add_history(self):
        self.sub_text_box.append(self.main_text_box.text())
        self.main_text_box.clear()


def main():
    app = QApplication(sys.argv)
    window = Textbox()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()


