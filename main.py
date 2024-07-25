import sys

from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PIL import Image, ImageFilter
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
        self.open_data_settings()
        self.setupUi(self)
        self.image_data()
        self.pushButton.setChecked(True)
        self.screen_update()

        self.action_4.triggered.connect(self.load_image)
        self.action_2.triggered.connect(self.remove_image)
        self.action.triggered.connect(self.save_image)

        self.pushButton.clicked.connect(self.screen_update)
        self.pushButton_2.clicked.connect(self.sharpen)
        self.pushButton_5.clicked.connect(self.white_black)
        self.pushButton_4.clicked.connect(self.embross)
        self.pushButton_6.clicked.connect(self.edges)
        self.back_pushButton.clicked.connect(self.back)
        self.exit_pushButton_2.clicked.connect(self.exit)
        self.exit_pushButton.clicked.connect(self.exit)

    def open_data_settings(self):
        with open(resource_path("system_data/data.txt"), 'r', encoding='utf8') as file:
            data = file.read().rstrip().split('\n')
            self.name = data[0]
            self.steps = int(data[1])

    def save_data_settings(self):
        s = self.name + '\n' + str(self.steps)
        with open(resource_path("system_data/data.txt"), 'w', encoding='utf8') as file:
            file.write(s)

    def screen_update(self):
        pixmap = QtGui.QPixmap(resource_path(self.name))
        if self.pushButton.isChecked():
            pixmap = pixmap.scaled(1420, 1022, QtCore.Qt.KeepAspectRatio)
        else:
            pixmap = pixmap.scaled(1740, 1022, QtCore.Qt.KeepAspectRatio)
        self.label_image.setPixmap(pixmap)

    def image_data(self):
        image = Image.open(resource_path(self.name))
        self.format = image.format
        self.mode = image.mode
        self.x, self.y = image.size
        image.close()
        if self.steps < 10:
            name = f'res_0{self.steps}.{self.format}'
        else:
            name = f'res_{self.steps}.{self.format}'
        self.action_5.setText(f'Имя: {name}')
        self.action_6.setText(f'Формат: {self.format}')
        self.action_7.setText(f'Размеры: {self.x} * {self.y}')
        self.action_8.setText(f'Цветовая модель: {self.mode}')

    def load_image(self):
        if self.steps < 100:
            name = QFileDialog.getOpenFileName(self, 'Choose image', '', 'Images (*.png *.jpg *.jpeg *.jfif *.gif *.bmp)')[0]
            if name != '':
                self.steps += 1
                image_1 = Image.open(name)
                self.format = image_1.format
                image_2 = image_1.copy()
                image_1.close()
                if self.steps < 10:
                    self.name = resource_path(f'steps_images/res_0{self.steps}.{self.format}')
                else:
                    self.name = resource_path(f'steps_images/res_{self.steps}.{self.format}')
                image_2.save(self.name)
                self.screen_update()
                self.image_data()
                self.save_data_settings()
        else:
            self.statusBar.showMessage('Слишком много изменений. Откатите, пожалуйста, изменения назад.')

    def white_black(self):
        if self.steps < 100:
            image = Image.open(resource_path(self.name))
            if self.mode == 'RGB' or self.mode == 'L':
                image = image.convert('L')
                image = image.convert('RGB')
            elif self.mode == 'RGBA' or self.mode == 'LA':
                image = image.convert('LA')
                image = image.convert('RGBA')
            self.steps += 1
            if self.steps < 10:
                self.name = resource_path(f'steps_images/res_0{self.steps}.{self.format}')
            else:
                self.name = resource_path(f'steps_images/res_{self.steps}.{self.format}')
            image.save(self.name)
            image.close()
            self.screen_update()
            self.image_data()
            self.save_data_settings()
        else:
            self.statusBar.showMessage('Слишком много изменений. Откатите, пожалуйста, изменения назад.')

    def embross(self):
        if self.steps < 100:
            self.image_data()
            image = Image.open(resource_path(self.name))
            if image.mode == "RGBA":
                r, g, b, a = image.split()
            else:
                r, g, b = image.split()
            beta = Image.merge('RGB', (r, g, b))
            beta = beta.filter(ImageFilter.SMOOTH)
            beta = beta.filter(ImageFilter.EMBOSS)
            if image.mode == "RGBA":
                r, g, b = beta.split()
                result = Image.merge('RGBA', (r, g, b, a))
            else:
                result = beta
            self.steps += 1
            if self.steps < 10:
                self.name = resource_path(f'steps_images/res_0{self.steps}.{self.format}')
            else:
                self.name = resource_path(f'steps_images/res_{self.steps}.{self.format}')
            result.save(self.name)
            result.close()
            image.close()
            self.screen_update()
            self.image_data()
            self.save_data_settings()
        else:
            self.statusBar.showMessage('Слишком много изменений. Откатите, пожалуйста, изменения назад.')

    def edges(self):
        if self.steps < 100:
            self.image_data()
            image = Image.open(resource_path(self.name))
            if image.mode == "RGBA":
                r, g, b, a = image.split()
            else:
                r, g, b = image.split()
            beta = Image.merge('RGB', (r, g, b))
            beta = beta.filter(ImageFilter.SMOOTH)
            beta = beta.filter(ImageFilter.FIND_EDGES)
            if image.mode == "RGBA":
                r, g, b = beta.split()
                result = Image.merge('RGBA', (r, g, b, a))
            else:
                result = beta
            self.steps += 1
            if self.steps < 10:
                self.name = resource_path(f'steps_images/res_0{self.steps}.{self.format}')
            else:
                self.name = resource_path(f'steps_images/res_{self.steps}.{self.format}')
            result.save(self.name)
            result.close()
            image.close()
            self.screen_update()
            self.image_data()
            self.save_data_settings()
        else:
            self.statusBar.showMessage('Слишком много изменений. Откатите, пожалуйста, изменения назад.')

    def sharpen(self):
        if self.steps < 100:
            self.image_data()
            image = Image.open(resource_path(self.name))
            image = image.filter(ImageFilter.SHARPEN)
            self.steps += 1
            if self.steps < 10:
                self.name = resource_path(f'steps_images/res_0{self.steps}.{self.format}')
            else:
                self.name = resource_path(f'steps_images/res_{self.steps}.{self.format}')
            image.save(self.name)
            image.close()
            self.screen_update()
            self.image_data()
            self.save_data_settings()
        else:
            self.statusBar.showMessage('Слишком много изменений. Откатите, пожалуйста, изменения назад.')

    def remove_image(self):
        images = os.listdir(resource_path('steps_images'))
        images = sorted(images)
        for i in images:
            if i != 'res_00.JPEG':
                os.remove(resource_path(f'steps_images/{i}'))
        self.name = 'steps_images/res_00.JPEG'
        self.steps = 0
        self.save_data_settings()
        self.image_data()
        self.screen_update()

    def save_image(self):
        image = Image.open(resource_path(self.name))
        name = self.name
        self.name, ok = QFileDialog.getSaveFileName(self, 'Save image', resource_path(''), f"{self.format} files (*.{self.format.lower()})")
        if ok:
            image.save(self.name)
        self.name = name
        image.close()

    def keyPressEvent(self, event):
        if int(event.modifiers()) == (Qt.ControlModifier):
            if event.key() == Qt.Key_Z:
                self.back()

    def back(self):
        images = os.listdir(resource_path('steps_images'))
        images = sorted(images)
        if len(images) > 1:
            self.name = resource_path('steps_images/' + images[-2])
            os.remove(resource_path('steps_images/' + images[-1]))
            self.screen_update()
            self.steps -= 1
            self.save_data_settings()
            self.image_data()

    def exit(self):
        self.name = 'steps_images/res_00.JPEG'
        self.steps = 0
        self.remove_image()
        self.save_data_settings()
        ex.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.setGeometry(0, 0, 1920, 1080)
    ex.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    ex.show()
    sys.exit(app.exec_())