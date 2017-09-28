# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication, QWidget


class Button(QtWidgets.QMainWindow):
    def __init__(self):
        super(Button, self).__init__()
        self.initUI()

    def initUI(self):
        button = QPushButton("")
def main():
    app = QApplication(sys.argv)
    window = QWidget()
    window.resize(150,300)
    button = QPushButton("myFirstButton")
    window.setCentral