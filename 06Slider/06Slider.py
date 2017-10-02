# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QSlider, QLabel, QStyle, QAction, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5.QtGui import QPixmap, QIcon


class Slider(QMainWindow):

    def __init__(self):
        super().__init__()

        self.color_slider = QSlider(Qt.Horizontal, self)
        self.label = QLabel(self)
        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)
        self.main_layout = QVBoxLayout()

        self.heat_maps_path = ['./pixmap/orange.png', './pixmap/orange.png', './pixmap/orange.png', './pixmap/orange.png',
                            './pixmap/orange.png', './pixmap/orange.png', './pixmap/orange.png', './pixmap/orange.png',
                            './pixmap/orange.png', './pixmap/orange.png']

        self.init_ui()

    def init_ui(self):
        self.color_slider.setFocusPolicy(Qt.NoFocus)
        self.color_slider.valueChanged[int].connect(self.change_value)

        pixmap = QPixmap('./pixmap/orange.png')
        pixmap_resized = pixmap.scaled(128, 64)
        self.label.setPixmap(pixmap_resized)

        color_slider_layout = QHBoxLayout()
        color_slider_layout.addWidget(self.color_slider)
        color_slider_layout.addWidget(self.label)

        exit_action = QAction(QIcon('./icon/exit.png'), '&Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit Application')
        exit_action.triggered.connect(QCoreApplication.instance().quit)

        toolbar = self.addToolBar('&toolbar')
        toolbar.addAction(exit_action)

        self.main_layout.addLayout(color_slider_layout)
        self.main_widget.setLayout(self.main_layout)

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('slider')
        self.show()

    def change_value(self, value):
        if value == 0:
            self.label.setPixmap(QPixmap('./pixmap/orange.png'))

        elif value > 0 and value <= 30:
            self.label.setPixmap(QPixmap('yellow.png'))

        elif value > 30 and value < 80:
            self.label.setPixmap(QPixmap('green.png'))

        else:
            self.label.setPixmap(QPixmap('blue.png'))


def main():
    app = QApplication(sys.argv)
    window = Slider()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

