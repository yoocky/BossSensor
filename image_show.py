# -*- coding: utf-8 -*-
import sys

from PyQt5.QtWidgets import QApplication,QLabel
from PyQt5.QtGui import QPixmap

def show_image(image_path='vscode.png'):
    app = QApplication(sys.argv)
    pixmap = QPixmap(image_path)
    screen = QLabel()
    screen.setPixmap(pixmap)
    screen.showFullScreen()
    sys.exit(app.exec_())


if __name__ == '__main__':
    show_image()
