# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

from BoardWidget import BoardWidget
from create_climb_form_widget import CreateClimbForm

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = BoardWidget()
        self.widget.setObjectName(u"Board Widget")
        self.widget.setGeometry(QRect(0, 0, 391, 411))
        self.centralwidget.layout().addWidget.widget
        self.widget_2 = CreateClimbForm()
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(0, 410, 391, 61))
        self.centralwidget.layout().addWidget.widget_2
        self.create_climb = QPushButton(self.centralwidget)
        self.create_climb.setObjectName(u"create_climb")
        self.create_climb.setGeometry(QRect(0, 470, 121, 81))
        self.save_climb = QPushButton(self.centralwidget)
        self.save_climb.setObjectName(u"save_climb")
        self.save_climb.setGeometry(QRect(120, 470, 121, 81))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.create_climb.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.save_climb.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    # retranslateUi

