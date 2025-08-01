from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(QtCore.QSize(1920, 1080))
        MainWindow.setMaximumSize(QtCore.QSize(1920, 1080))
        MainWindow.setStyleSheet("background-color: rgb(50, 50, 50);\n"
"font: 16pt \"Arial\";\n"
"color:rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.background_label = QtWidgets.QLabel(self.centralwidget)
        self.background_label.setGeometry(QtCore.QRect(0, 0, 1920, 1022))
        self.background_label.setMinimumSize(QtCore.QSize(1920, 1022))
        self.background_label.setMaximumSize(QtCore.QSize(1920, 1022))
        self.background_label.setText("")
        self.background_label.setPixmap(QtGui.QPixmap("system_data/background_dark.png"))
        self.background_label.setScaledContents(True)
        self.background_label.setObjectName("background_label")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1920, 1022))
        self.widget.setMinimumSize(QtCore.QSize(1920, 1022))
        self.widget.setMaximumSize(QtCore.QSize(1920, 1022))
        self.widget.setStyleSheet("background-color: rgba(255, 0, 0, 0);")
        self.widget.setObjectName("widget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.main_menu_widget_2 = QtWidgets.QWidget(self.widget)
        self.main_menu_widget_2.setMinimumSize(QtCore.QSize(120, 1022))
        self.main_menu_widget_2.setMaximumSize(QtCore.QSize(120, 1022))
        self.main_menu_widget_2.setStyleSheet("background-color:rgb(40, 40, 40);")
        self.main_menu_widget_2.setObjectName("main_menu_widget_2")
        self.gridLayout = QtWidgets.QGridLayout(self.main_menu_widget_2)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_menu = QtWidgets.QLabel(self.main_menu_widget_2)
        self.label_menu.setMinimumSize(QtCore.QSize(90, 90))
        self.label_menu.setMaximumSize(QtCore.QSize(90, 90))
        self.label_menu.setText("")
        self.label_menu.setPixmap(QtGui.QPixmap("system_data/dark_icons/image (2).png"))
        self.label_menu.setScaledContents(True)
        self.label_menu.setObjectName("label_menu")
        self.horizontalLayout.addWidget(self.label_menu)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.exit_pushButton_2 = QtWidgets.QPushButton(self.main_menu_widget_2)
        self.exit_pushButton_2.setMinimumSize(QtCore.QSize(60, 60))
        self.exit_pushButton_2.setMaximumSize(QtCore.QSize(60, 60))
        self.exit_pushButton_2.setStyleSheet("background-color:rgb(60, 60, 60);\n"
"font: 20pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.exit_pushButton_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("system_data/dark_icons/image (4).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit_pushButton_2.setIcon(icon)
        self.exit_pushButton_2.setIconSize(QtCore.QSize(60, 60))
        self.exit_pushButton_2.setObjectName("exit_pushButton_2")
        self.horizontalLayout_2.addWidget(self.exit_pushButton_2)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.main_menu_widget_2, 0, 0, 1, 1)
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setMinimumSize(QtCore.QSize(500, 1022))
        self.widget_2.setMaximumSize(QtCore.QSize(500, 1022))
        self.widget_2.setStyleSheet("background-color:rgb(40, 40, 40);")
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_menu_2 = QtWidgets.QLabel(self.widget_2)
        self.label_menu_2.setMinimumSize(QtCore.QSize(90, 90))
        self.label_menu_2.setMaximumSize(QtCore.QSize(90, 90))
        self.label_menu_2.setText("")
        self.label_menu_2.setPixmap(QtGui.QPixmap("system_data/dark_icons/image (2).png"))
        self.label_menu_2.setScaledContents(True)
        self.label_menu_2.setObjectName("label_menu_2")
        self.horizontalLayout_3.addWidget(self.label_menu_2)
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setMinimumSize(QtCore.QSize(150, 90))
        self.label_2.setMaximumSize(QtCore.QSize(150, 90))
        self.label_2.setStyleSheet("font: 40pt \"Arial\";")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setMinimumSize(QtCore.QSize(0, 60))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 60))
        self.label_3.setStyleSheet("font: 28pt \"Arial\";")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_14.addWidget(self.label_3)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_14)
        self.scrollArea = QtWidgets.QScrollArea(self.widget_2)
        self.scrollArea.setMinimumSize(QtCore.QSize(480, 360))
        self.scrollArea.setMaximumSize(QtCore.QSize(480, 360))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 478, 358))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton_1 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_1.setMinimumSize(QtCore.QSize(224, 60))
        self.pushButton_1.setMaximumSize(QtCore.QSize(224, 60))
        self.pushButton_1.setStyleSheet("background-color:rgb(60, 60, 60);\n"
"font: 22pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.pushButton_1.setObjectName("pushButton_1")
        self.horizontalLayout_6.addWidget(self.pushButton_1)
        spacerItem7 = QtWidgets.QSpacerItem(4, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem7)
        self.pushButton_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_2.setMinimumSize(QtCore.QSize(224, 60))
        self.pushButton_2.setMaximumSize(QtCore.QSize(224, 60))
        self.pushButton_2.setStyleSheet("background-color:rgb(60, 60, 60);\n"
"font: 22pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_6.addWidget(self.pushButton_2)
        self.gridLayout_2.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pushButton_3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_3.setMinimumSize(QtCore.QSize(224, 60))
        self.pushButton_3.setMaximumSize(QtCore.QSize(224, 60))
        self.pushButton_3.setStyleSheet("background-color:rgb(60, 60, 60);\n"
"font: 22pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_7.addWidget(self.pushButton_3)
        spacerItem8 = QtWidgets.QSpacerItem(4, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem8)
        self.pushButton_4 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_4.setMinimumSize(QtCore.QSize(224, 60))
        self.pushButton_4.setMaximumSize(QtCore.QSize(224, 60))
        self.pushButton_4.setStyleSheet("background-color:rgb(60, 60, 60);\n"
"font: 22pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_7.addWidget(self.pushButton_4)
        self.gridLayout_2.addLayout(self.horizontalLayout_7, 1, 0, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.pushButton_5 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_5.setMinimumSize(QtCore.QSize(224, 60))
        self.pushButton_5.setMaximumSize(QtCore.QSize(224, 60))
        self.pushButton_5.setStyleSheet("background-color:rgb(60, 60, 60);\n"
"font: 22pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_8.addWidget(self.pushButton_5)
        spacerItem9 = QtWidgets.QSpacerItem(4, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem9)
        self.pushButton_6 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_6.setMinimumSize(QtCore.QSize(224, 60))
        self.pushButton_6.setMaximumSize(QtCore.QSize(224, 60))
        self.pushButton_6.setStyleSheet("background-color:rgb(60, 60, 60);\n"
"font: 22pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_8.addWidget(self.pushButton_6)
        self.gridLayout_2.addLayout(self.horizontalLayout_8, 2, 0, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.pushButton_7 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_7.setMinimumSize(QtCore.QSize(224, 60))
        self.pushButton_7.setMaximumSize(QtCore.QSize(224, 60))
        self.pushButton_7.setStyleSheet("background-color:rgb(60, 60, 60);\n"
"font: 22pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_9.addWidget(self.pushButton_7)
        spacerItem10 = QtWidgets.QSpacerItem(4, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem10)
        self.pushButton_8 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_8.setMinimumSize(QtCore.QSize(224, 60))
        self.pushButton_8.setMaximumSize(QtCore.QSize(224, 60))
        self.pushButton_8.setStyleSheet("background-color:rgb(60, 60, 60);\n"
"font: 22pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_9.addWidget(self.pushButton_8)
        self.gridLayout_2.addLayout(self.horizontalLayout_9, 3, 0, 1, 1)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.pushButton_9 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_9.setMinimumSize(QtCore.QSize(224, 60))
        self.pushButton_9.setMaximumSize(QtCore.QSize(224, 60))
        self.pushButton_9.setStyleSheet("background-color:rgb(60, 60, 60);\n"
"font: 22pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_10.addWidget(self.pushButton_9)
        spacerItem11 = QtWidgets.QSpacerItem(4, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem11)
        self.pushButton_10 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_10.setMinimumSize(QtCore.QSize(224, 60))
        self.pushButton_10.setMaximumSize(QtCore.QSize(224, 60))
        self.pushButton_10.setStyleSheet("background-color:rgb(60, 60, 60);\n"
"font: 22pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_10.addWidget(self.pushButton_10)
        self.gridLayout_2.addLayout(self.horizontalLayout_10, 4, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        self.label_4.setMinimumSize(QtCore.QSize(0, 60))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 60))
        self.label_4.setStyleSheet("font: 28pt \"Arial\";")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_15.addWidget(self.label_4)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem12)
        self.verticalLayout_2.addLayout(self.horizontalLayout_15)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.widget_2)
        self.scrollArea_2.setMinimumSize(QtCore.QSize(480, 240))
        self.scrollArea_2.setMaximumSize(QtCore.QSize(480, 240))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 478, 238))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.pushButton_15 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_15.setMinimumSize(QtCore.QSize(224, 60))
        self.pushButton_15.setMaximumSize(QtCore.QSize(224, 60))
        self.pushButton_15.setStyleSheet("background-color:rgb(60, 60, 60);\n"
"font: 22pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.pushButton_15.setObjectName("pushButton_15")
        self.horizontalLayout_13.addWidget(self.pushButton_15)
        spacerItem13 = QtWidgets.QSpacerItem(4, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem13)
        self.gridLayout_3.addLayout(self.horizontalLayout_13, 2, 0, 1, 1)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.pushButton_11 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_11.setMinimumSize(QtCore.QSize(224, 60))
        self.pushButton_11.setMaximumSize(QtCore.QSize(224, 60))
        self.pushButton_11.setStyleSheet("background-color:rgb(60, 60, 60);\n"
"font: 22pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.pushButton_11.setObjectName("pushButton_11")
        self.horizontalLayout_11.addWidget(self.pushButton_11)
        spacerItem14 = QtWidgets.QSpacerItem(4, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem14)
        self.pushButton_12 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_12.setMinimumSize(QtCore.QSize(224, 60))
        self.pushButton_12.setMaximumSize(QtCore.QSize(224, 60))
        self.pushButton_12.setStyleSheet("background-color:rgb(60, 60, 60);\n"
"font: 22pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.pushButton_12.setObjectName("pushButton_12")
        self.horizontalLayout_11.addWidget(self.pushButton_12)
        self.gridLayout_3.addLayout(self.horizontalLayout_11, 0, 0, 1, 1)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_13.setMinimumSize(QtCore.QSize(224, 60))
        self.pushButton_13.setMaximumSize(QtCore.QSize(224, 60))
        self.pushButton_13.setStyleSheet("background-color:rgb(60, 60, 60);\n"
"font: 22pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.pushButton_13.setObjectName("pushButton_13")
        self.horizontalLayout_12.addWidget(self.pushButton_13)
        spacerItem15 = QtWidgets.QSpacerItem(4, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem15)
        self.pushButton_14 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_14.setMinimumSize(QtCore.QSize(224, 60))
        self.pushButton_14.setMaximumSize(QtCore.QSize(224, 60))
        self.pushButton_14.setStyleSheet("background-color:rgb(60, 60, 60);\n"
"font: 22pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.pushButton_14.setObjectName("pushButton_14")
        self.horizontalLayout_12.addWidget(self.pushButton_14)
        self.gridLayout_3.addLayout(self.horizontalLayout_12, 1, 0, 1, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.addWidget(self.scrollArea_2)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem16)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem17)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.exit_pushButton = QtWidgets.QPushButton(self.widget_2)
        self.exit_pushButton.setMinimumSize(QtCore.QSize(200, 60))
        self.exit_pushButton.setMaximumSize(QtCore.QSize(200, 60))
        self.exit_pushButton.setStyleSheet("background-color:rgb(60, 60, 60);\n"
"font: 28pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.exit_pushButton.setIcon(icon)
        self.exit_pushButton.setIconSize(QtCore.QSize(60, 60))
        self.exit_pushButton.setObjectName("exit_pushButton")
        self.horizontalLayout_4.addWidget(self.exit_pushButton)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem18)
        self.back_pushButton = QtWidgets.QPushButton(self.widget_2)
        self.back_pushButton.setMinimumSize(QtCore.QSize(60, 60))
        self.back_pushButton.setMaximumSize(QtCore.QSize(60, 60))
        self.back_pushButton.setStyleSheet("background-color:rgb(60, 60, 60);\n"
"font: 20pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.back_pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("system_data/dark_icons/image (3).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back_pushButton.setIcon(icon1)
        self.back_pushButton.setIconSize(QtCore.QSize(60, 60))
        self.back_pushButton.setObjectName("back_pushButton")
        self.horizontalLayout_4.addWidget(self.back_pushButton)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem19)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.gridLayout_4.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.widget_2, 0, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setMinimumSize(QtCore.QSize(60, 1022))
        self.pushButton.setMaximumSize(QtCore.QSize(60, 1022))
        self.pushButton.setStyleSheet("background-color:rgb(40, 40, 40);")
        self.pushButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("system_data/dark_icons/image (6).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap("system_data/dark_icons/image (5).png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton.setIcon(icon2)
        self.pushButton.setIconSize(QtCore.QSize(60, 60))
        self.pushButton.setCheckable(True)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_5.addWidget(self.pushButton, 0, 2, 1, 1)
        self.label_image = QtWidgets.QLabel(self.widget)
        self.label_image.setMinimumSize(QtCore.QSize(0, 1022))
        self.label_image.setMaximumSize(QtCore.QSize(16777215, 1022))
        self.label_image.setObjectName("label_image")
        self.gridLayout_5.addWidget(self.label_image, 0, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 30))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("action_4")
        self.action_5 = QtWidgets.QAction(MainWindow)
        self.action_5.setObjectName("action_5")
        self.action_6 = QtWidgets.QAction(MainWindow)
        self.action_6.setObjectName("action_6")
        self.action_7 = QtWidgets.QAction(MainWindow)
        self.action_7.setObjectName("action_7")
        self.action_8 = QtWidgets.QAction(MainWindow)
        self.action_8.setObjectName("action_8")
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menu.addSeparator()
        self.menu.addAction(self.action_4)
        self.menu_2.addAction(self.action_5)
        self.menu_2.addAction(self.action_6)
        self.menu_2.addAction(self.action_7)
        self.menu_2.addAction(self.action_8)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        self.pushButton.toggled['bool'].connect(self.widget_2.setVisible) # type: ignore
        self.pushButton.toggled['bool'].connect(self.main_menu_widget_2.setHidden) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Witch of images"))
        self.label_2.setText(_translate("MainWindow", "Меню"))
        self.label_3.setText(_translate("MainWindow", " Фильтры:"))
        self.pushButton_1.setText(_translate("MainWindow", "Негатив"))
        self.pushButton_2.setText(_translate("MainWindow", "Резкость"))
        self.pushButton_3.setText(_translate("MainWindow", "Размытие"))
        self.pushButton_4.setText(_translate("MainWindow", "Эмбросс"))
        self.pushButton_5.setText(_translate("MainWindow", "Насыщенность"))
        self.pushButton_6.setText(_translate("MainWindow", "Контурное"))
        self.pushButton_7.setText(_translate("MainWindow", "Цветовая гамма"))
        self.pushButton_8.setText(_translate("MainWindow", "Яркость"))
        self.pushButton_9.setText(_translate("MainWindow", "Квуантиз"))
        self.pushButton_10.setText(_translate("MainWindow", "Контрастность"))
        self.label_4.setText(_translate("MainWindow", "Операции:"))
        self.pushButton_15.setText(_translate("MainWindow", "Стерео пара"))
        self.pushButton_11.setText(_translate("MainWindow", "Отзеркалить"))
        self.pushButton_12.setText(_translate("MainWindow", "Поворот"))
        self.pushButton_13.setText(_translate("MainWindow", "Обрезка"))
        self.pushButton_14.setText(_translate("MainWindow", "Переразмерить"))
        self.exit_pushButton.setText(_translate("MainWindow", "Выход"))
        self.label_image.setText(_translate("MainWindow", "TextLabel"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.menu_2.setTitle(_translate("MainWindow", "Информация об изображении"))
        self.action.setText(_translate("MainWindow", "Сохранить"))
        self.action.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.action_2.setText(_translate("MainWindow", "Убрать"))
        self.action_2.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.action_4.setText(_translate("MainWindow", "Загрузить"))
        self.action_4.setShortcut(_translate("MainWindow", "Ctrl+Space"))
        self.action_5.setText(_translate("MainWindow", "Имя:"))
        self.action_6.setText(_translate("MainWindow", "Формат:"))
        self.action_7.setText(_translate("MainWindow", "Размеры:"))
        self.action_8.setText(_translate("MainWindow", "Цветовая модель:"))
        self.main_menu_widget_2.setHidden(True)
