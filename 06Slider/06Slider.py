# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QSlider, QLabel, QStyle, QAction, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5.QtGui import QPixmap, QIcon


class Slider(QMainWindow):

    def __init__(self):
        super().__init__()

        self.color_slider = QSlider(Qt.Horizontal, self)
        self.color_label = QLabel(self)
        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)
        self.main_layout = QVBoxLayout()

        self.heat_maps_path = ['./heatMap/color0.png', './heatMap/color1.png', './heatMap/color2.png',
                               './heatMap/color3.png', './heatMap/color4.png', './heatMap/color5.png',
                               './heatMap/color6.png', './heatMap/color7.png', './heatMap/color8.png',
                               './heatMap/color9.png']

        self.heat_map_pix = []

        self.init_ui()

    def init_ui(self):
        for heat_map_path in self.heat_maps_path:
            pixmap = QPixmap(heat_map_path)
            pixmap_resized = pixmap.scaled(129, 16)
            self.heat_map_pix.append(pixmap_resized)

        self.color_slider.setFocusPolicy(Qt.NoFocus)
        self.color_slider.valueChanged[int].connect(self.change_value)

        self.color_label.setPixmap(self.heat_map_pix[0])

        color_slider_layout = QHBoxLayout()
        color_slider_layout.addWidget(self.color_slider)
        color_slider_layout.addWidget(self.color_label)

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
        for i, pixmap in enumerate(self.heat_map_pix, 1):
            if (i-1)*10 <= value and value < i*10:
                self.color_label.setPixmap(pixmap)
                break


def main():
    app = QApplication(sys.argv)
    window = Slider()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

