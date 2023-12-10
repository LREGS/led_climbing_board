# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'save_climb_popup.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFormLayout, QLabel, QLineEdit, QSizePolicy,
    QSpinBox, QWidget)

class Ui_input_climb_data(object):
    def setupUi(self, input_climb_data):
        if not input_climb_data.objectName():
            input_climb_data.setObjectName(u"input_climb_data")
        input_climb_data.resize(394, 154)
        self.buttonBox = QDialogButtonBox(input_climb_data)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 110, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.formLayoutWidget = QWidget(input_climb_data)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(-1, 9, 371, 91))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.Name = QLabel(self.formLayoutWidget)
        self.Name.setObjectName(u"Name")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.Name)

        self.climb_name = QLineEdit(self.formLayoutWidget)
        self.climb_name.setObjectName(u"climb_name")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.climb_name)

        self.Grade = QLabel(self.formLayoutWidget)
        self.Grade.setObjectName(u"Grade")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.Grade)

        self.grade = QSpinBox(self.formLayoutWidget)
        self.grade.setObjectName(u"grade")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.grade)

        self.ratingLabel_2 = QLabel(self.formLayoutWidget)
        self.ratingLabel_2.setObjectName(u"ratingLabel_2")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.ratingLabel_2)

        self.ratingSpinBox = QSpinBox(self.formLayoutWidget)
        self.ratingSpinBox.setObjectName(u"ratingSpinBox")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.ratingSpinBox)


        self.retranslateUi(input_climb_data)
        self.buttonBox.accepted.connect(input_climb_data.accept)
        self.buttonBox.rejected.connect(input_climb_data.reject)

        QMetaObject.connectSlotsByName(input_climb_data)
    # setupUi

    def retranslateUi(self, input_climb_data):
        input_climb_data.setWindowTitle(QCoreApplication.translate("input_climb_data", u"Dialog", None))
        self.Name.setText(QCoreApplication.translate("input_climb_data", u"Name", None))
        self.Grade.setText(QCoreApplication.translate("input_climb_data", u"Grade", None))
        self.ratingLabel_2.setText(QCoreApplication.translate("input_climb_data", u"Rating", None))
    # retranslateUi

