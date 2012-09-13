# -*- coding: utf-8 *-*

import sys

import sip
API_NAMES = ["QDate", "QString", "QTextStream", "QTime", "QUrl"]
API_VERSION = 2
for name in API_NAMES:
    sip.setapi(name, API_VERSION)

from PyQt4.QtGui import QApplication
from PyQt4.QtGui import QIcon
from PyQt4.QtGui import QMenu
from PyQt4.QtGui import QInputDialog
from PyQt4.QtGui import QSystemTrayIcon

import notifier


class Jarvis(QSystemTrayIcon):

    def __init__(self, parent=None):
        super(Jarvis, self).__init__(parent)
        icon = QIcon('icon.png')
        self.setIcon(icon)

        self.notif = notifier.Notifier()

        menu = QMenu()
        if len(sys.argv) > 1 and sys.argv[1] == '--debugging':
            create_notif = menu.addAction('Create Notification')
            create_notif.triggered.connect(self.create_notification)
        quit_jarvis = menu.addAction('Quit')
        app = QApplication.instance()
        quit_jarvis.triggered.connect(app.quit)
        self.setContextMenu(menu)

    def create_notification(self):
        text = QInputDialog.getText(None, 'Debugging', 'Notification Text:')
        self.notif.add_notification(text[0], say_it=True)


app = QApplication(sys.argv)
w = Jarvis()
w.show()

app.exec_()
