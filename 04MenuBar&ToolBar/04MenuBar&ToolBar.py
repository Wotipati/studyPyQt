# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QStyle
from PyQt5.QtCore import QCoreApplication


class Bars(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):

        exit_gui = QApplication.style().standardIcon(QStyle.SP_TitleBarCloseButton)
        exit_action = QAction(exit_gui, '&Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit Application')
        exit_action.triggered.connect(QCoreApplication.instance().quit)

        qt_info_gui = QApplication.style().standardIcon(QStyle.SP_TitleBarMenuButton)
        qt_info_action = QAction(qt_info_gui, 'about Qt', self)
        qt_info_action.setShortcut('ctrl+I')
        qt_info_action.setStatusTip('show Qt info')
        qt_info_action.triggered.connect(QCoreApplication.instance().quit)

        self.statusBar()

        menubar = self.menuBar()
        file_menu = menubar.addMenu('&File')
        file_menu.addAction(exit_action)
        file_menu.addAction(qt_info_action)

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exit_action)
        toolbar.addAction(qt_info_action)

        self.setGeometry(200, 300, 400, 300)
        self.setWindowTitle('Menu and Tool Bars')
        self.show()


def main():
    app = QApplication(sys.argv)
    window =Bars()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
