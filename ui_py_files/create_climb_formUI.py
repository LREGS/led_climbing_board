# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_climb_formUI.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpinBox, QTextEdit,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(268, 218)
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(0, 0, 261, 158))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.climb_nam = QLineEdit(self.formLayoutWidget)
        self.climb_nam.setObjectName(u"climb_nam")
        self.climb_nam.setText('Climb Name')

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.climb_nam)

        self.label_3 = QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_3)

        self.Grade = QSpinBox(self.formLayoutWidget)
        self.Grade.setObjectName(u"Grade")
        self.Grade.setMaximum(16)
        self.Grade.setValue(0)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.Grade)

        self.textEdit = QTextEdit(self.formLayoutWidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setReadOnly(True)
        self.textEdit.setPlainText('Route')

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.textEdit)

        self.saveClimb = QPushButton(Form)
        self.saveClimb.setObjectName(u"saveClimb")
        self.saveClimb.setGeometry(QRect(0, 160, 261, 25))
        self.cancelcreation = QPushButton(Form)
        self.cancelcreation.setObjectName(u"cancelcreation")
        self.cancelcreation.setGeometry(QRect(0, 190, 261, 25))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Route", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Name", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Grade", None))
        self.saveClimb.setText(QCoreApplication.translate("Form", u"Save Climb", None))
        self.cancelcreation.setText(QCoreApplication.translate("Form", u"Cancel", None))
    # retranslateUi

