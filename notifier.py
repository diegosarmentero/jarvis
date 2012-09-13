# -*- coding: utf-8 *-*
from PyQt4.QtGui import QApplication
from PyQt4.QtGui import QFrame
from PyQt4.QtGui import QVBoxLayout
from PyQt4.QtCore import QTimer
from PyQt4.QtCore import QProcess
from PyQt4.QtCore import Qt
from PyQt4.QtCore import QUrl
from PyQt4.QtDeclarative import QDeclarativeView


class Notifier(object):

    def __init__(self):
        self.notifications = []

    def add_notification(self, msg='', say_it=False):
        notification = Notification()
        app = QApplication.instance()
        desktop = app.desktop()
        rect = desktop.screenGeometry(desktop.primaryScreen())
        x = rect.width() - 20
        y = 40
        if len(self.notifications) > 0:
            for item in self.notifications:
                y += item.height() - 10
        self.notifications.append(notification)
        notification.show()
        notification.move(x, y)
        notification.move(x, y)
        if say_it:
            self.say_notification(msg, notification)
        QTimer.singleShot(4000, self.clean_notification)

    def say_notification(self, msg='', parent=None):
        proc = QProcess(parent)
        proc.start('espeak', ['-s', '150', '-p', '99', '-v', 'es-la', msg])
        #lang: '-v', 'es-la'

    def clean_notification(self):
        for item in self.notifications:
            item.close()


class Notification(QFrame):

    def __init__(self):
        super(Notification, self).__init__()
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setStyleSheet("background:transparent;")
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setMinimumHeight(120)
        # Create the QML user interface.
        view = QDeclarativeView()
        view.setSource(QUrl('Bubble.qml'))
        view.setResizeMode(QDeclarativeView.SizeRootObjectToView)
        vbox = QVBoxLayout(self)
        vbox.addWidget(view)
