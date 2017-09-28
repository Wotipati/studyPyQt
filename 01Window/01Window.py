# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

def main():
    app = QApplication(sys.argv)
    window = QWidget()
    window.resize(300, 150)
    window.setWindowTitle('QtFirstWindow')
    window.setWindowIcon(QIcon('pythonlogo.png'))
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()