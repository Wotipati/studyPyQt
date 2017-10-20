# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QSlider, QLabel, QAction, QVBoxLayout,\
                            QHBoxLayout, QLCDNumber, QLineEdit
from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5.QtGui import QPixmap, QIcon


class Textbox(QMainWindow):

    def __init__(self):
        super().__init__()

        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)
        self.main_layout = QVBoxLayout()
        self.text_box = QLineEdit()
        self.label = QLabel()

        self.init_ui()

    def init_ui(self):

        self.text_box.textChanged.connect(self.change_text)

        self.main_layout.addWidget(self.text_box)
        self.main_layout.addWidget(self.label)
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


def main():
    app = QApplication(sys.argv)
    window = Textbox()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()


