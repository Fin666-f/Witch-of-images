import sys

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from designs.main_menu import Ui_MainWindow
import os


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath("")
    return os.path.join(base_path, relative_path)


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.setChecked(True)
        self.pixmap = QtGui.QPixmap(resource_path("steps_images/res_00.JPEG"))
        self.pixmap = self.pixmap.scaled(1420, 1022, QtCore.Qt.KeepAspectRatio)
        self.label_image.setPixmap(self.pixmap)

        self.pushButton.clicked.connect(self.screen_update)
        self.exit_pushButton_2.clicked.connect(self.exit)
        self.exit_pushButton.clicked.connect(self.exit)

    def screen_update(self):
        self.pixmap = QtGui.QPixmap(resource_path("steps_images/res_00.JPEG"))
        if self.pushButton.isChecked():
            self.pixmap = self.pixmap.scaled(1420, 1022, QtCore.Qt.KeepAspectRatio)
        else:
            self.pixmap = self.pixmap.scaled(1740, 1022, QtCore.Qt.KeepAspectRatio)
        self.label_image.setPixmap(self.pixmap)

    def exit(self):
        ex.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.setGeometry(0, 0, 1920, 1080)
    ex.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    ex.show()
    sys.exit(app.exec_())