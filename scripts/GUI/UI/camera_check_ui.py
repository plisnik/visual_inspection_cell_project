# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'camera_check.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
    QSizePolicy, QWidget)
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from Icons import icons_rc

class Ui_Camera_check(object):
    def setupUi(self, Camera_check):
        if not Camera_check.objectName():
            Camera_check.setObjectName(u"Camera_check")
        Camera_check.resize(649, 556)
        icon = QIcon()
        icon.addFile(u":/Icons/icons8-video-100.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Camera_check.setWindowIcon(icon)
        Camera_check.setStyleSheet(u"QDialog {\n"
"	background-color: #ffffff;\n"
"}\n"
"")
        self.gridLayout = QGridLayout(Camera_check)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_image = QLabel(Camera_check)
        self.label_image.setObjectName(u"label_image")
        font = QFont()
        font.setPointSize(31)
        self.label_image.setFont(font)
        self.label_image.setStyleSheet(u"")
        self.label_image.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_image, 0, 0, 1, 1)


        self.retranslateUi(Camera_check)

        QMetaObject.connectSlotsByName(Camera_check)
    # setupUi

    def retranslateUi(self, Camera_check):
        Camera_check.setWindowTitle(QCoreApplication.translate("Camera_check", u"Display Camera", None))
        self.label_image.setText(QCoreApplication.translate("Camera_check", u"No Image", None))
    # retranslateUi

