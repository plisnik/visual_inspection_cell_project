# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'initial_adjustment.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QGroupBox,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSlider, QSpacerItem, QWidget)

class Ui_Initial_adjustment(object):
    def setupUi(self, Initial_adjustment):
        if not Initial_adjustment.objectName():
            Initial_adjustment.setObjectName(u"Initial_adjustment")
        Initial_adjustment.resize(896, 550)
        Initial_adjustment.setStyleSheet(u"QDialog {\n"
"	background-color: #ffffff;\n"
"}")
        self.gridLayout = QGridLayout(Initial_adjustment)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_image = QLabel(Initial_adjustment)
        self.label_image.setObjectName(u"label_image")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_image.sizePolicy().hasHeightForWidth())
        self.label_image.setSizePolicy(sizePolicy)
        self.label_image.setMinimumSize(QSize(500, 0))
        font = QFont()
        font.setPointSize(17)
        self.label_image.setFont(font)
        self.label_image.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_image, 0, 2, 9, 1)

        self.groupBox_2 = QGroupBox(Initial_adjustment)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(350, 0))
        self.groupBox_2.setMaximumSize(QSize(368, 16777215))
        self.groupBox_2.setStyleSheet(u"QGroupBox {\n"
"	border: none;\n"
"	padding: 0px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"	color: #000036;\n"
"}")
        self.gridLayout_3 = QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.b_close = QPushButton(self.groupBox_2)
        self.b_close.setObjectName(u"b_close")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.b_close.sizePolicy().hasHeightForWidth())
        self.b_close.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(11)
        font1.setWeight(QFont.DemiBold)
        self.b_close.setFont(font1)
        self.b_close.setStyleSheet(u"QPushButton {\n"
"    background-color: #3e37ff;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    padding: 10px; /* Uprav\u00ed vnit\u0159n\u00ed prostor tla\u010d\u00edtka */\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #000036;\n"
"}")

        self.gridLayout_3.addWidget(self.b_close, 0, 1, 1, 1)

        self.b_setup = QPushButton(self.groupBox_2)
        self.b_setup.setObjectName(u"b_setup")
        sizePolicy1.setHeightForWidth(self.b_setup.sizePolicy().hasHeightForWidth())
        self.b_setup.setSizePolicy(sizePolicy1)
        self.b_setup.setMinimumSize(QSize(0, 0))
        self.b_setup.setMaximumSize(QSize(5000, 16777215))
        self.b_setup.setFont(font1)
        self.b_setup.setStyleSheet(u"QPushButton {\n"
"    background-color: #3e37ff;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    padding: 10px; /* Uprav\u00ed vnit\u0159n\u00ed prostor tla\u010d\u00edtka */\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #000036;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #808080; /* \u0160ed\u00e1 barva pro deaktivovan\u00e9 tla\u010d\u00edtko */\n"
"    color: #c0c0c0; /* Sv\u011btlej\u0161\u00ed \u0161ed\u00e1 barva textu */\n"
"    border: none;\n"
"}")

        self.gridLayout_3.addWidget(self.b_setup, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_2, 6, 0, 1, 1)

        self.groupBox_4 = QGroupBox(Initial_adjustment)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy2)
        self.groupBox_4.setMinimumSize(QSize(0, 0))
        self.groupBox_4.setMaximumSize(QSize(368, 16777215))
        self.groupBox_4.setStyleSheet(u"QGroupBox {\n"
"	border: none;\n"
"	padding: 0px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"	color: #000036;\n"
"}")
        self.gridLayout_6 = QGridLayout(self.groupBox_4)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.groupBox_3 = QGroupBox(self.groupBox_4)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_4 = QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.b_freedrive_on = QPushButton(self.groupBox_3)
        self.b_freedrive_on.setObjectName(u"b_freedrive_on")
        self.b_freedrive_on.setStyleSheet(u"QPushButton {\n"
"    background-color: #3e37ff;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    padding: 10px; /* Uprav\u00ed vnit\u0159n\u00ed prostor tla\u010d\u00edtka */\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #000036;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #808080; /* \u0160ed\u00e1 barva pro deaktivovan\u00e9 tla\u010d\u00edtko */\n"
"    color: #c0c0c0; /* Sv\u011btlej\u0161\u00ed \u0161ed\u00e1 barva textu */\n"
"    border: none;\n"
"}")

        self.gridLayout_4.addWidget(self.b_freedrive_on, 0, 0, 1, 1)

        self.b_freedrive_off = QPushButton(self.groupBox_3)
        self.b_freedrive_off.setObjectName(u"b_freedrive_off")
        self.b_freedrive_off.setStyleSheet(u"QPushButton {\n"
"    background-color: #3e37ff;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    padding: 10px; /* Uprav\u00ed vnit\u0159n\u00ed prostor tla\u010d\u00edtka */\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #000036;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #808080; /* \u0160ed\u00e1 barva pro deaktivovan\u00e9 tla\u010d\u00edtko */\n"
"    color: #c0c0c0; /* Sv\u011btlej\u0161\u00ed \u0161ed\u00e1 barva textu */\n"
"    border: none;\n"
"}")

        self.gridLayout_4.addWidget(self.b_freedrive_off, 0, 1, 1, 1)


        self.gridLayout_6.addWidget(self.groupBox_3, 3, 0, 1, 2)

        self.groupBox_5 = QGroupBox(self.groupBox_4)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_5 = QGridLayout(self.groupBox_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.b_light_on_init = QPushButton(self.groupBox_5)
        self.b_light_on_init.setObjectName(u"b_light_on_init")
        self.b_light_on_init.setStyleSheet(u"QPushButton {\n"
"    background-color: #3e37ff;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    padding: 10px; /* Uprav\u00ed vnit\u0159n\u00ed prostor tla\u010d\u00edtka */\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #000036;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #808080; /* \u0160ed\u00e1 barva pro deaktivovan\u00e9 tla\u010d\u00edtko */\n"
"    color: #c0c0c0; /* Sv\u011btlej\u0161\u00ed \u0161ed\u00e1 barva textu */\n"
"    border: none;\n"
"}")

        self.gridLayout_5.addWidget(self.b_light_on_init, 0, 0, 1, 1)

        self.b_light_off_init = QPushButton(self.groupBox_5)
        self.b_light_off_init.setObjectName(u"b_light_off_init")
        self.b_light_off_init.setStyleSheet(u"QPushButton {\n"
"    background-color: #3e37ff;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    padding: 10px; /* Uprav\u00ed vnit\u0159n\u00ed prostor tla\u010d\u00edtka */\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #000036;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #808080; /* \u0160ed\u00e1 barva pro deaktivovan\u00e9 tla\u010d\u00edtko */\n"
"    color: #c0c0c0; /* Sv\u011btlej\u0161\u00ed \u0161ed\u00e1 barva textu */\n"
"    border: none;\n"
"}")

        self.gridLayout_5.addWidget(self.b_light_off_init, 0, 1, 1, 1)


        self.gridLayout_6.addWidget(self.groupBox_5, 4, 0, 1, 2)

        self.label_2 = QLabel(self.groupBox_4)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setMinimumSize(QSize(350, 120))
        self.label_2.setMaximumSize(QSize(350, 120))
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color:#000036;")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_2.setWordWrap(True)
        self.label_2.setMargin(0)

        self.gridLayout_6.addWidget(self.label_2, 0, 0, 1, 2)

        self.groupBox = QGroupBox(self.groupBox_4)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy2.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy2)
        self.groupBox.setMinimumSize(QSize(350, 100))
        self.groupBox.setMaximumSize(QSize(350, 100))
        self.groupBox.setStyleSheet(u"QGroupBox {\n"
"	border: none;\n"
"	padding: 0px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"	color: #000036;\n"
"}")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lineEdit_distance = QLineEdit(self.groupBox)
        self.lineEdit_distance.setObjectName(u"lineEdit_distance")
        self.lineEdit_distance.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_distance.setStyleSheet(u"margin: 20px;")

        self.gridLayout_2.addWidget(self.lineEdit_distance, 0, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy3)
        self.label_3.setMinimumSize(QSize(200, 0))
        self.label_3.setMaximumSize(QSize(16777215, 16777215))
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color:#000036;")
        self.label_3.setWordWrap(True)
        self.label_3.setMargin(0)

        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.groupBox, 2, 0, 1, 2)

        self.Slider_rectangle = QSlider(self.groupBox_4)
        self.Slider_rectangle.setObjectName(u"Slider_rectangle")
        sizePolicy2.setHeightForWidth(self.Slider_rectangle.sizePolicy().hasHeightForWidth())
        self.Slider_rectangle.setSizePolicy(sizePolicy2)
        self.Slider_rectangle.setMinimumSize(QSize(350, 50))
        self.Slider_rectangle.setMaximumSize(QSize(350, 60))
        self.Slider_rectangle.setStyleSheet(u"QSlider  {\n"
"    margin: 20px 50px 20px 50px;\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    border: 1px solid #999;\n"
"    height: 20px;\n"
"    background: #ccc;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: #0078D7;\n"
"    border: 1px solid #005A9E;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"    border-radius: 9px;\n"
"}")
        self.Slider_rectangle.setMinimum(30)
        self.Slider_rectangle.setMaximum(70)
        self.Slider_rectangle.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_6.addWidget(self.Slider_rectangle, 1, 0, 1, 2)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_2, 5, 0, 1, 2)


        self.gridLayout.addWidget(self.groupBox_4, 0, 0, 1, 1)

        QWidget.setTabOrder(self.Slider_rectangle, self.lineEdit_distance)
        QWidget.setTabOrder(self.lineEdit_distance, self.b_freedrive_on)
        QWidget.setTabOrder(self.b_freedrive_on, self.b_freedrive_off)
        QWidget.setTabOrder(self.b_freedrive_off, self.b_light_on_init)
        QWidget.setTabOrder(self.b_light_on_init, self.b_light_off_init)
        QWidget.setTabOrder(self.b_light_off_init, self.b_setup)
        QWidget.setTabOrder(self.b_setup, self.b_close)

        self.retranslateUi(Initial_adjustment)

        QMetaObject.connectSlotsByName(Initial_adjustment)
    # setupUi

    def retranslateUi(self, Initial_adjustment):
        Initial_adjustment.setWindowTitle(QCoreApplication.translate("Initial_adjustment", u"Initial Adjustment", None))
        self.label_image.setText(QCoreApplication.translate("Initial_adjustment", u"No Image", None))
        self.groupBox_2.setTitle("")
        self.b_close.setText(QCoreApplication.translate("Initial_adjustment", u"Close", None))
        self.b_setup.setText(QCoreApplication.translate("Initial_adjustment", u"Set up", None))
        self.groupBox_4.setTitle("")
        self.groupBox_3.setTitle("")
        self.b_freedrive_on.setText(QCoreApplication.translate("Initial_adjustment", u"Freedrive ON", None))
        self.b_freedrive_off.setText(QCoreApplication.translate("Initial_adjustment", u"Freedrive OFF", None))
        self.groupBox_5.setTitle("")
        self.b_light_on_init.setText(QCoreApplication.translate("Initial_adjustment", u"Light ON", None))
        self.b_light_off_init.setText(QCoreApplication.translate("Initial_adjustment", u"Light OFF", None))
        self.label_2.setText(QCoreApplication.translate("Initial_adjustment", u"Position the robot and camera so that the camera is perpendicular to the calibration pad. The calibration pad must be in focus and aligned in a rectangle. The size of the rectangle can be partially changed using the slider below.", None))
        self.groupBox.setTitle("")
        self.label_3.setText(QCoreApplication.translate("Initial_adjustment", u"Enter the approximate distance from the calibration pad (mm):", None))
    # retranslateUi

