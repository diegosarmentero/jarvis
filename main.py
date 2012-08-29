# -*- coding: utf-8 *-*

import sys

from PyQt4.QtGui import QApplication
from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import Qt
from PyQt4.QtCore import QUrl
from PyQt4.QtDeclarative import QDeclarativeView


class Window(QMainWindow):

    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setStyleSheet("background:transparent;")
        self.setWindowFlags(Qt.FramelessWindowHint)
        # Create the QML user interface.
        view = QDeclarativeView()
        view.setSource(QUrl('Bubble.qml'))
        view.setResizeMode(QDeclarativeView.SizeRootObjectToView)
        self.setCentralWidget(view)


app = QApplication(sys.argv)
w = Window()
w.show()

app.exec_()
