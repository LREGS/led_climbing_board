# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'signupwindow.ui'
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
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 196)
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(50, 120, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.formLayoutWidget = QWidget(Dialog)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(0, 0, 401, 80))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.username_label = QLabel(self.formLayoutWidget)
        self.username_label.setObjectName(u"username_label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.username_label)

        self.password_label = QLabel(self.formLayoutWidget)
        self.password_label.setObjectName(u"password_label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.password_label)

        self.username_input = QLineEdit(self.formLayoutWidget)
        self.username_input.setObjectName(u"username_input")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.username_input)

        self.password_input = QLineEdit(self.formLayoutWidget)
        self.password_input.setObjectName(u"password_input")
        self.password_input.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.password_input)

        self.retyped_password_2 = QLabel(self.formLayoutWidget)
        self.retyped_password_2.setObjectName(u"retyped_password_2")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.retyped_password_2)

        self.retyped_password_input = QLineEdit(self.formLayoutWidget)
        self.retyped_password_input.setObjectName(u"retyped_password_input")
        self.retyped_password_input.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.retyped_password_input)

        self.communication_box = QLabel(Dialog)
        self.communication_box.setObjectName(u"communication_box")
        self.communication_box.setGeometry(QRect(6, 90, 391, 20))

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.username_label.setText(QCoreApplication.translate("Dialog", u"Username", None))
        self.password_label.setText(QCoreApplication.translate("Dialog", u"Password", None))
        self.retyped_password_2.setText(QCoreApplication.translate("Dialog", u"Retype Passowrd ", None))
        self.communication_box.setText("")
    # retranslateUi

