import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PIL import Image, ImageFilter, ImageEnhance
from designs.main_menu import Ui_MainWindow
from designs.others_menu import Ui_OtherWindow
import numpy as np
import os


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath("")
    return os.path.join(base_path, relative_path)


class MainWidget(QMainWindow, Ui_MainWindow):
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
        self.pushButton_1.clicked.connect(self.go_negative)
        self.pushButton_2.clicked.connect(self.go_sharpen)
        self.pushButton_3.clicked.connect(self.go_blur)
        self.pushButton_4.clicked.connect(self.embross)
        self.pushButton_5.clicked.connect(self.go_saturation)
        self.pushButton_6.clicked.connect(self.edges)
        self.pushButton_7.clicked.connect(self.go_arrange)
        self.pushButton_8.clicked.connect(self.go_bright)
        self.pushButton_9.clicked.connect(self.go_quantize)
        self.pushButton_10.clicked.connect(self.go_contrast)
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

    def go_negative(self):
        self.save_data_settings()
        negative_window = NegativeWidget()
        widget.addWidget(negative_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def go_blur(self):
        self.save_data_settings()
        blur_window = BlurWidget()
        widget.addWidget(blur_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def go_arrange(self):
        self.save_data_settings()
        arrange_window = ArrangeWidget()
        widget.addWidget(arrange_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def go_saturation(self):
        self.save_data_settings()
        saturation_window = SaturationWidget()
        widget.addWidget(saturation_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def go_bright(self):
        self.save_data_settings()
        bright_window = BrightWidget()
        widget.addWidget(bright_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def go_contrast(self):
        self.save_data_settings()
        contrast_window = ContrastWidget()
        widget.addWidget(contrast_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def go_quantize(self):
        self.save_data_settings()
        quantize_window = QuantizeWidget()
        widget.addWidget(quantize_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def go_sharpen(self):
        self.save_data_settings()
        sharpen_window = SharpenWidget()
        widget.addWidget(sharpen_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

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
        widget.close()


class NegativeWidget(QMainWindow, Ui_OtherWindow):
    def __init__(self):
        super().__init__()
        self.open_data_settings()
        self.setupUi(self)
        self.image_data()
        self.negative()
        self.negative_value_now = -256
        self.horizontalSlider.setMinimum(-256)
        self.horizontalSlider.setMaximum(255)
        self.horizontalSlider.setProperty("value", -256)
        self.pixmap = QPixmap(self.name)
        self.pixmap = self.pixmap.scaled(1420, 1024, QtCore.Qt.KeepAspectRatio)
        self.label_image.setPixmap(self.pixmap)

        self.horizontalSlider.valueChanged['int'].connect(self.negative_value)

        self.pushButton_1.clicked.connect(self.save_negative)
        self.pushButton_2.clicked.connect(self.exit_negative)

    def screen_update(self, image):
        if self.mode == 'RGBA':
            image = QImage(image, image.shape[1], image.shape[0], image.strides[0], QImage.Format_RGBA8888)
        else:
            image = QImage(image, image.shape[1], image.shape[0], image.strides[0], QImage.Format_RGB888)
        self.pixmap = QPixmap.fromImage(image)
        self.pixmap = self.pixmap.scaled(1420, 1024, QtCore.Qt.KeepAspectRatio)
        self.label_image.setPixmap(self.pixmap)

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

    def open_data_settings(self):
        with open(resource_path("system_data/data.txt"), 'r', encoding='utf8') as file:
            data = file.read().rstrip().split('\n')
            self.name = data[0]
            self.steps = int(data[1])

    def save_data_settings(self):
        s = self.name + '\n' + str(self.steps)
        with open(resource_path("system_data/data.txt"), 'w', encoding='utf8') as file:
            file.write(s)

    def negative_value(self, value):
        self.negative_value_now = value
        self.update()

    def change_negative(self, image, value):
        image = Image.fromarray(np.uint8(image))
        if self.mode == "RGBA":
            r, g, b, a = image.split()
        else:
            r, g, b = image.split()
        beta = Image.merge('RGB', (r, g, b))
        beta = np.asarray(image)
        beta = Image.fromarray(np.uint8(abs(value - beta)))
        beta = beta.convert('RGB')
        if self.mode == "RGBA":
            r, g, b = beta.split()
            result = Image.merge('RGBA', (r, g, b, a))
        else:
            result = beta
        result = np.asarray(result)
        return result

    def update(self):
        image = self.change_negative(self.image, self.negative_value_now)
        self.result = image
        self.screen_update(image)

    def negative(self):
        image = Image.open(self.name)
        self.image = np.asarray(image)
        image.close()
        self.screen_update(self.image)

    def save_negative(self):
        if self.steps < 100:
            image = Image.fromarray(np.uint8(self.result))
            self.steps += 1
            if self.steps < 10:
                self.name = resource_path(f'steps_images/res_0{self.steps}.{self.format}')
            else:
                self.name = resource_path(f'steps_images/res_{self.steps}.{self.format}')
            image.save(self.name)
            image.close()
            self.save_data_settings()
            self.exit_negative()
        else:
            self.statusBar.showMessage('Слишком много изменений. Откатите, пожалуйста, изменения назад.')

    def exit_negative(self):
        main_window = MainWidget()
        widget.addWidget(main_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class BlurWidget(QMainWindow, Ui_OtherWindow):
    def __init__(self):
        super().__init__()
        self.open_data_settings()
        self.setupUi(self)
        self.image_data()
        self.blur()
        self.blur_value_now = 0
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setMaximum(1000)
        self.horizontalSlider.setProperty("value", 0)
        self.label_2.setText(" Размытие")
        self.pixmap = QPixmap(self.name)
        self.pixmap = self.pixmap.scaled(1420, 1024, QtCore.Qt.KeepAspectRatio)
        self.label_image.setPixmap(self.pixmap)

        self.horizontalSlider.valueChanged['int'].connect(self.blur_value)

        self.pushButton_1.clicked.connect(self.save_blur)
        self.pushButton_2.clicked.connect(self.exit_blur)

    def screen_update(self, image):
        if self.mode == 'RGBA':
            image = QImage(image, image.shape[1], image.shape[0], image.strides[0], QImage.Format_RGBA8888)
        else:
            image = QImage(image, image.shape[1], image.shape[0], image.strides[0], QImage.Format_RGB888)
        self.pixmap = QPixmap.fromImage(image)
        self.pixmap = self.pixmap.scaled(1420, 1024, QtCore.Qt.KeepAspectRatio)
        self.label_image.setPixmap(self.pixmap)

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

    def open_data_settings(self):
        with open(resource_path("system_data/data.txt"), 'r', encoding='utf8') as file:
            data = file.read().rstrip().split('\n')
            self.name = data[0]
            self.steps = int(data[1])

    def save_data_settings(self):
        s = self.name + '\n' + str(self.steps)
        with open(resource_path("system_data/data.txt"), 'w', encoding='utf8') as file:
            file.write(s)

    def blur_value(self, value):
        self.blur_value_now = value
        self.update()

    def change_blur(self, image, value):
        image = Image.fromarray(np.uint8(image))
        result = image.filter(ImageFilter.GaussianBlur(radius=value / 100))
        result = np.asarray(result)
        return result

    def update(self):
        image = self.change_blur(self.image, self.blur_value_now)
        self.result = image
        self.screen_update(image)

    def blur(self):
        image = Image.open(self.name)
        self.image = np.asarray(image)
        image.close()
        self.screen_update(self.image)

    def save_blur(self):
        if self.steps < 100:
            image = Image.fromarray(np.uint8(self.result))
            self.steps += 1
            if self.steps < 10:
                self.name = resource_path(f'steps_images/res_0{self.steps}.{self.format}')
            else:
                self.name = resource_path(f'steps_images/res_{self.steps}.{self.format}')
            image.save(self.name)
            image.close()
            self.save_data_settings()
            self.exit_blur()
        else:
            self.statusBar.showMessage('Слишком много изменений. Откатите, пожалуйста, изменения назад.')

    def exit_blur(self):
        main_window = MainWidget()
        widget.addWidget(main_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class ArrangeWidget(QMainWindow, Ui_OtherWindow):
    def __init__(self):
        super().__init__()
        self.open_data_settings()
        self.setupUi(self)
        self.image_data()
        self.arrange()
        self.arrange_value_now = 0
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setMaximum(255)
        self.horizontalSlider.setProperty("value", 0)
        self.label_2.setText(" Цветовая гамма")
        self.pixmap = QPixmap(self.name)
        self.pixmap = self.pixmap.scaled(1420, 1024, QtCore.Qt.KeepAspectRatio)
        self.label_image.setPixmap(self.pixmap)

        self.horizontalSlider.valueChanged['int'].connect(self.arrange_value)

        self.pushButton_1.clicked.connect(self.save_arrange)
        self.pushButton_2.clicked.connect(self.exit_arrange)

    def screen_update(self, image):
        if self.mode == 'RGBA':
            image = QImage(image, image.shape[1], image.shape[0], image.strides[0], QImage.Format_RGBA8888)
        else:
            image = QImage(image, image.shape[1], image.shape[0], image.strides[0], QImage.Format_RGB888)
        self.pixmap = QPixmap.fromImage(image)
        self.pixmap = self.pixmap.scaled(1420, 1024, QtCore.Qt.KeepAspectRatio)
        self.label_image.setPixmap(self.pixmap)

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

    def open_data_settings(self):
        with open(resource_path("system_data/data.txt"), 'r', encoding='utf8') as file:
            data = file.read().rstrip().split('\n')
            self.name = data[0]
            self.steps = int(data[1])

    def save_data_settings(self):
        s = self.name + '\n' + str(self.steps)
        with open(resource_path("system_data/data.txt"), 'w', encoding='utf8') as file:
            file.write(s)

    def arrange_value(self, value):
        self.arrange_value_now = value
        self.update()

    def change_arrange(self, image, value):
        image = Image.fromarray(np.uint8(image))
        if self.mode == "RGBA":
            r, g, b, a = image.split()
        else:
            r, g, b = image.split()
        beta = image.convert('HSV')
        h, s, v = beta.split()
        h = h.point(lambda x: (x + value) % 256)
        beta = Image.merge('HSV', (h, s, v))
        beta = beta.convert('RGB')
        if self.mode == "RGBA":
            r, g, b = beta.split()
            result = Image.merge('RGBA', (r, g, b, a))
        else:
            result = beta
        result = np.asarray(result)
        return result

    def update(self):
        image = self.change_arrange(self.image, self.arrange_value_now)
        self.result = image
        self.screen_update(image)

    def arrange(self):
        image = Image.open(self.name)
        self.image = np.asarray(image)
        image.close()
        self.screen_update(self.image)

    def save_arrange(self):
        if self.steps < 100:
            image = Image.fromarray(np.uint8(self.result))
            self.steps += 1
            if self.steps < 10:
                self.name = resource_path(f'steps_images/res_0{self.steps}.{self.format}')
            else:
                self.name = resource_path(f'steps_images/res_{self.steps}.{self.format}')
            image.save(self.name)
            image.close()
            self.save_data_settings()
            self.exit_arrange()
        else:
            self.statusBar.showMessage('Слишком много изменений. Откатите, пожалуйста, изменения назад.')

    def exit_arrange(self):
        main_window = MainWidget()
        widget.addWidget(main_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class SaturationWidget(QMainWindow, Ui_OtherWindow):
    def __init__(self):
        super().__init__()
        self.open_data_settings()
        self.setupUi(self)
        self.image_data()
        self.saturation()
        self.arrange_value_now = 1000
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setMaximum(2000)
        self.horizontalSlider.setProperty("value", 1000)
        self.label_2.setText(" Насыщенность")
        self.pixmap = QPixmap(self.name)
        self.pixmap = self.pixmap.scaled(1420, 1024, QtCore.Qt.KeepAspectRatio)
        self.label_image.setPixmap(self.pixmap)

        self.horizontalSlider.valueChanged['int'].connect(self.saturation_value)

        self.pushButton_1.clicked.connect(self.save_saturation)
        self.pushButton_2.clicked.connect(self.exit_saturation)

    def screen_update(self, image):
        if self.mode == 'RGBA':
            image = QImage(image, image.shape[1], image.shape[0], image.strides[0], QImage.Format_RGBA8888)
        else:
            image = QImage(image, image.shape[1], image.shape[0], image.strides[0], QImage.Format_RGB888)
        self.pixmap = QPixmap.fromImage(image)
        self.pixmap = self.pixmap.scaled(1420, 1024, QtCore.Qt.KeepAspectRatio)
        self.label_image.setPixmap(self.pixmap)

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

    def open_data_settings(self):
        with open(resource_path("system_data/data.txt"), 'r', encoding='utf8') as file:
            data = file.read().rstrip().split('\n')
            self.name = data[0]
            self.steps = int(data[1])

    def save_data_settings(self):
        s = self.name + '\n' + str(self.steps)
        with open(resource_path("system_data/data.txt"), 'w', encoding='utf8') as file:
            file.write(s)

    def saturation_value(self, value):
        self.arrange_value_now = value
        self.update()

    def change_saturation(self, image, value):
        image = Image.fromarray(np.uint8(image))
        image = ImageEnhance.Color(image).enhance(value / 1000)
        result = np.asarray(image)
        result = np.asarray(result)
        return result

    def update(self):
        image = self.change_saturation(self.image, self.arrange_value_now)
        self.result = image
        self.screen_update(image)

    def saturation(self):
        image = Image.open(self.name)
        self.image = np.asarray(image)
        image.close()
        self.screen_update(self.image)

    def save_saturation(self):
        if self.steps < 100:
            image = Image.fromarray(np.uint8(self.result))
            self.steps += 1
            if self.steps < 10:
                self.name = resource_path(f'steps_images/res_0{self.steps}.{self.format}')
            else:
                self.name = resource_path(f'steps_images/res_{self.steps}.{self.format}')
            image.save(self.name)
            image.close()
            self.save_data_settings()
            self.exit_saturation()
        else:
            self.statusBar.showMessage('Слишком много изменений. Откатите, пожалуйста, изменения назад.')

    def exit_saturation(self):
        main_window = MainWidget()
        widget.addWidget(main_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class BrightWidget(QMainWindow, Ui_OtherWindow):
    def __init__(self):
        super().__init__()
        self.open_data_settings()
        self.setupUi(self)
        self.image_data()
        self.bright()
        self.bright_value_now = 1000
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setMaximum(2000)
        self.horizontalSlider.setProperty("value", 1000)
        self.label_2.setText(" Яркость")
        self.pixmap = QPixmap(self.name)
        self.pixmap = self.pixmap.scaled(1420, 1024, QtCore.Qt.KeepAspectRatio)
        self.label_image.setPixmap(self.pixmap)

        self.horizontalSlider.valueChanged['int'].connect(self.bright_value)

        self.pushButton_1.clicked.connect(self.save_bright)
        self.pushButton_2.clicked.connect(self.exit_bright)

    def screen_update(self, image):
        if self.mode == 'RGBA':
            image = QImage(image, image.shape[1], image.shape[0], image.strides[0], QImage.Format_RGBA8888)
        else:
            image = QImage(image, image.shape[1], image.shape[0], image.strides[0], QImage.Format_RGB888)
        self.pixmap = QPixmap.fromImage(image)
        self.pixmap = self.pixmap.scaled(1420, 1024, QtCore.Qt.KeepAspectRatio)
        self.label_image.setPixmap(self.pixmap)

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

    def open_data_settings(self):
        with open(resource_path("system_data/data.txt"), 'r', encoding='utf8') as file:
            data = file.read().rstrip().split('\n')
            self.name = data[0]
            self.steps = int(data[1])

    def save_data_settings(self):
        s = self.name + '\n' + str(self.steps)
        with open(resource_path("system_data/data.txt"), 'w', encoding='utf8') as file:
            file.write(s)

    def bright_value(self, value):
        self.bright_value_now = value
        self.update()

    def change_bright(self, image, value):
        if value >= 1000:
            image = Image.fromarray(np.uint8(image))
            image = ImageEnhance.Brightness(image).enhance(value / 1000)
            result = np.asarray(image)
            result = np.asarray(result)
            return result
        else:
            value = 1000 + (1000 - value)
            image = Image.fromarray(np.uint8(255 - image))
            image = ImageEnhance.Brightness(image).enhance(value / 1000)
            result = np.asarray(image)
            result = np.asarray(result)
            return 255 - result

    def update(self):
        image = self.change_bright(self.image, self.bright_value_now)
        self.result = image
        self.screen_update(image)

    def bright(self):
        image = Image.open(self.name)
        self.image = np.asarray(image)
        image.close()
        self.screen_update(self.image)

    def save_bright(self):
        if self.steps < 100:
            image = Image.fromarray(np.uint8(self.result))
            self.steps += 1
            if self.steps < 10:
                self.name = resource_path(f'steps_images/res_0{self.steps}.{self.format}')
            else:
                self.name = resource_path(f'steps_images/res_{self.steps}.{self.format}')
            image.save(self.name)
            image.close()
            self.save_data_settings()
            self.exit_bright()
        else:
            self.statusBar.showMessage('Слишком много изменений. Откатите, пожалуйста, изменения назад.')

    def exit_bright(self):
        main_window = MainWidget()
        widget.addWidget(main_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class ContrastWidget(QMainWindow, Ui_OtherWindow):
    def __init__(self):
        super().__init__()
        self.open_data_settings()
        self.setupUi(self)
        self.image_data()
        self.contrast()
        self.contrast_value_now = 1000
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setMaximum(2000)
        self.horizontalSlider.setProperty("value", 1000)
        self.label_2.setText(" Контрастность")
        self.pixmap = QPixmap(self.name)
        self.pixmap = self.pixmap.scaled(1420, 1024, QtCore.Qt.KeepAspectRatio)
        self.label_image.setPixmap(self.pixmap)

        self.horizontalSlider.valueChanged['int'].connect(self.contrast_value)

        self.pushButton_1.clicked.connect(self.save_contrast)
        self.pushButton_2.clicked.connect(self.exit_contrast)

    def screen_update(self, image):
        if self.mode == 'RGBA':
            image = QImage(image, image.shape[1], image.shape[0], image.strides[0], QImage.Format_RGBA8888)
        else:
            image = QImage(image, image.shape[1], image.shape[0], image.strides[0], QImage.Format_RGB888)
        self.pixmap = QPixmap.fromImage(image)
        self.pixmap = self.pixmap.scaled(1420, 1024, QtCore.Qt.KeepAspectRatio)
        self.label_image.setPixmap(self.pixmap)

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

    def open_data_settings(self):
        with open(resource_path("system_data/data.txt"), 'r', encoding='utf8') as file:
            data = file.read().rstrip().split('\n')
            self.name = data[0]
            self.steps = int(data[1])

    def save_data_settings(self):
        s = self.name + '\n' + str(self.steps)
        with open(resource_path("system_data/data.txt"), 'w', encoding='utf8') as file:
            file.write(s)

    def contrast_value(self, value):
        self.contrast_value_now = value
        self.update()

    def change_contrast(self, image, value):
        image = Image.fromarray(np.uint8(image))
        image = ImageEnhance.Contrast(image).enhance(value / 1000)
        result = np.asarray(image)
        result = np.asarray(result)
        return result

    def update(self):
        image = self.change_contrast(self.image, self.contrast_value_now)
        self.result = image
        self.screen_update(image)

    def contrast(self):
        image = Image.open(self.name)
        self.image = np.asarray(image)
        image.close()
        self.screen_update(self.image)

    def save_contrast(self):
        if self.steps < 100:
            image = Image.fromarray(np.uint8(self.result))
            self.steps += 1
            if self.steps < 10:
                self.name = resource_path(f'steps_images/res_0{self.steps}.{self.format}')
            else:
                self.name = resource_path(f'steps_images/res_{self.steps}.{self.format}')
            image.save(self.name)
            image.close()
            self.save_data_settings()
            self.exit_contrast()
        else:
            self.statusBar.showMessage('Слишком много изменений. Откатите, пожалуйста, изменения назад.')

    def exit_contrast(self):
        main_window = MainWidget()
        widget.addWidget(main_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class QuantizeWidget(QMainWindow, Ui_OtherWindow):
    def __init__(self):
        super().__init__()
        self.open_data_settings()
        self.setupUi(self)
        self.image_data()
        self.quantize()
        self.contrast_value_now = 255
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(255)
        self.horizontalSlider.setProperty("value", 255)
        self.label_2.setText(" Квуантиз")
        self.pixmap = QPixmap(self.name)
        self.pixmap = self.pixmap.scaled(1420, 1024, QtCore.Qt.KeepAspectRatio)
        self.label_image.setPixmap(self.pixmap)

        self.horizontalSlider.valueChanged['int'].connect(self.quantize_value)

        self.pushButton_1.clicked.connect(self.save_quantize)
        self.pushButton_2.clicked.connect(self.exit_quantize)

    def screen_update(self, image):
        if self.mode == 'RGBA':
            image = QImage(image, image.shape[1], image.shape[0], image.strides[0], QImage.Format_RGBA8888)
        else:
            image = QImage(image, image.shape[1], image.shape[0], image.strides[0], QImage.Format_RGB888)
        self.pixmap = QPixmap.fromImage(image)
        self.pixmap = self.pixmap.scaled(1420, 1024, QtCore.Qt.KeepAspectRatio)
        self.label_image.setPixmap(self.pixmap)

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

    def open_data_settings(self):
        with open(resource_path("system_data/data.txt"), 'r', encoding='utf8') as file:
            data = file.read().rstrip().split('\n')
            self.name = data[0]
            self.steps = int(data[1])

    def save_data_settings(self):
        s = self.name + '\n' + str(self.steps)
        with open(resource_path("system_data/data.txt"), 'w', encoding='utf8') as file:
            file.write(s)

    def quantize_value(self, value):
        self.contrast_value_now = value
        self.update()

    def change_quantize(self, image, value):
        image = Image.fromarray(np.uint8(image))
        if self.mode == "RGBA":
            r, g, b, a = image.split()
        else:
            r, g, b = image.split()
        beta = Image.merge('RGB', (r, g, b))
        beta = beta.quantize(value)
        beta = beta.convert('RGB')
        if self.mode == "RGBA":
            r, g, b = beta.split()
            result = Image.merge('RGBA', (r, g, b, a))
        else:
            result = beta
        result = np.asarray(result)
        return result

    def update(self):
        image = self.change_quantize(self.image, self.contrast_value_now)
        self.result = image
        self.screen_update(image)

    def quantize(self):
        image = Image.open(self.name)
        self.image = np.asarray(image)
        image.close()
        self.screen_update(self.image)

    def save_quantize(self):
        if self.steps < 100:
            image = Image.fromarray(np.uint8(self.result))
            self.steps += 1
            if self.steps < 10:
                self.name = resource_path(f'steps_images/res_0{self.steps}.{self.format}')
            else:
                self.name = resource_path(f'steps_images/res_{self.steps}.{self.format}')
            image.save(self.name)
            image.close()
            self.save_data_settings()
            self.exit_quantize()
        else:
            self.statusBar.showMessage('Слишком много изменений. Откатите, пожалуйста, изменения назад.')

    def exit_quantize(self):
        main_window = MainWidget()
        widget.addWidget(main_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class SharpenWidget(QMainWindow, Ui_OtherWindow):
    def __init__(self):
        super().__init__()
        self.open_data_settings()
        self.setupUi(self)
        self.image_data()
        self.sharpen()
        self.blur_value_now = 100
        self.horizontalSlider.setMinimum(100)
        self.horizontalSlider.setMaximum(1000)
        self.horizontalSlider.setProperty("value", 100)
        self.label_2.setText(" Резкость")
        self.pixmap = QPixmap(self.name)
        self.pixmap = self.pixmap.scaled(1420, 1024, QtCore.Qt.KeepAspectRatio)
        self.label_image.setPixmap(self.pixmap)

        self.horizontalSlider.valueChanged['int'].connect(self.sharpen_value)

        self.pushButton_1.clicked.connect(self.save_sharpen)
        self.pushButton_2.clicked.connect(self.exit_sharpen)

    def screen_update(self, image):
        if self.mode == 'RGBA':
            image = QImage(image, image.shape[1], image.shape[0], image.strides[0], QImage.Format_RGBA8888)
        else:
            image = QImage(image, image.shape[1], image.shape[0], image.strides[0], QImage.Format_RGB888)
        self.pixmap = QPixmap.fromImage(image)
        self.pixmap = self.pixmap.scaled(1420, 1024, QtCore.Qt.KeepAspectRatio)
        self.label_image.setPixmap(self.pixmap)

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

    def open_data_settings(self):
        with open(resource_path("system_data/data.txt"), 'r', encoding='utf8') as file:
            data = file.read().rstrip().split('\n')
            self.name = data[0]
            self.steps = int(data[1])

    def save_data_settings(self):
        s = self.name + '\n' + str(self.steps)
        with open(resource_path("system_data/data.txt"), 'w', encoding='utf8') as file:
            file.write(s)

    def sharpen_value(self, value):
        self.blur_value_now = value
        self.update()

    def change_sharpen(self, image, value):
        image = Image.fromarray(np.uint8(image))
        result = ImageEnhance.Sharpness(image).enhance(value / 100)
        result = np.asarray(result)
        return result

    def update(self):
        image = self.change_sharpen(self.image, self.blur_value_now)
        self.result = image
        self.screen_update(image)

    def sharpen(self):
        image = Image.open(self.name)
        self.image = np.asarray(image)
        image.close()
        self.screen_update(self.image)

    def save_sharpen(self):
        if self.steps < 100:
            image = Image.fromarray(np.uint8(self.result))
            self.steps += 1
            if self.steps < 10:
                self.name = resource_path(f'steps_images/res_0{self.steps}.{self.format}')
            else:
                self.name = resource_path(f'steps_images/res_{self.steps}.{self.format}')
            image.save(self.name)
            image.close()
            self.save_data_settings()
            self.exit_sharpen()
        else:
            self.statusBar.showMessage('Слишком много изменений. Откатите, пожалуйста, изменения назад.')

    def exit_sharpen(self):
        main_window = MainWidget()
        widget.addWidget(main_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWidget()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(main_window)
    widget.setGeometry(0, 0, 1920, 1080)
    widget.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    widget.show()
    sys.exit(app.exec_())