# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'testBoardui.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QWidget)

from HoldButtonWidget import clickableLabel

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 400)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        self.label.setGeometry(QRect(10, 0, 481, 501))
        self.label.setPixmap(QPixmap(u"../board400x400.png"))
        self.label.setScaledContents(True)
        self.label_2 = clickableLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(380, 50, 31, 16))
        self.label_2.setPixmap(QPixmap(u"../TESThold11.png"))
        self.label_2.setScaledContents(True)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(390, 50, 31, 20))
        self.label_3.setPixmap(QPixmap(u"TESThold11.png"))
        self.label_3.setScaledContents(True)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
        self.label_2.setText("")
        self.label_3.setText("")
    # retranslateUi

