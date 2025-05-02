# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test_init.ui'
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
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)

class Ui_test_1(object):
    def setupUi(self, test_1):
        if not test_1.objectName():
            test_1.setObjectName(u"test_1")
        test_1.resize(774, 418)
        test_1.setStyleSheet(u"QDialog {\n"
"	background-color: #ffffff;\n"
"}")
        self.gridLayout = QGridLayout(test_1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.image_label = QLabel(test_1)
        self.image_label.setObjectName(u"image_label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image_label.sizePolicy().hasHeightForWidth())
        self.image_label.setSizePolicy(sizePolicy)
        self.image_label.setMinimumSize(QSize(400, 400))
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.image_label, 0, 3, 8, 1)

        self.groupBox = QGroupBox(test_1)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(350, 0))
        self.groupBox.setMaximumSize(QSize(350, 16777215))
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
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 2, 1, 1, 3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 8, 1, 1, 3)

        self.b_close = QPushButton(self.groupBox)
        self.b_close.setObjectName(u"b_close")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.b_close.sizePolicy().hasHeightForWidth())
        self.b_close.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(11)
        font.setWeight(QFont.DemiBold)
        self.b_close.setFont(font)
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
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #808080; /* \u0160ed\u00e1 barva pro deaktivovan\u00e9 tla\u010d\u00edtko */\n"
"    color: #c0c0c0; /* Sv\u011btlej\u0161\u00ed \u0161ed\u00e1 barva textu */\n"
"    border: none;\n"
"}")

        self.gridLayout_2.addWidget(self.b_close, 10, 1, 1, 1)

        self.b_freedrive_on = QPushButton(self.groupBox)
        self.b_freedrive_on.setObjectName(u"b_freedrive_on")
        sizePolicy1.setHeightForWidth(self.b_freedrive_on.sizePolicy().hasHeightForWidth())
        self.b_freedrive_on.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(9)
        font1.setBold(False)
        self.b_freedrive_on.setFont(font1)
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

        self.gridLayout_2.addWidget(self.b_freedrive_on, 3, 1, 1, 1)

        self.b_start_test = QPushButton(self.groupBox)
        self.b_start_test.setObjectName(u"b_start_test")
        sizePolicy1.setHeightForWidth(self.b_start_test.sizePolicy().hasHeightForWidth())
        self.b_start_test.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setPointSize(11)
        font2.setWeight(QFont.DemiBold)
        font2.setKerning(False)
        self.b_start_test.setFont(font2)
        self.b_start_test.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_2.addWidget(self.b_start_test, 10, 2, 1, 1)

        self.b_freedrive_off = QPushButton(self.groupBox)
        self.b_freedrive_off.setObjectName(u"b_freedrive_off")
        sizePolicy1.setHeightForWidth(self.b_freedrive_off.sizePolicy().hasHeightForWidth())
        self.b_freedrive_off.setSizePolicy(sizePolicy1)
        self.b_freedrive_off.setFont(font1)
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

        self.gridLayout_2.addWidget(self.b_freedrive_off, 3, 2, 1, 2)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setMinimumSize(QSize(300, 0))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color:#000036;")
        self.label_2.setWordWrap(True)

        self.gridLayout_2.addWidget(self.label_2, 1, 1, 1, 2)

        self.b_light_off_init = QPushButton(self.groupBox)
        self.b_light_off_init.setObjectName(u"b_light_off_init")
        sizePolicy1.setHeightForWidth(self.b_light_off_init.sizePolicy().hasHeightForWidth())
        self.b_light_off_init.setSizePolicy(sizePolicy1)
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

        self.gridLayout_2.addWidget(self.b_light_off_init, 4, 2, 1, 1)

        self.b_light_on_init = QPushButton(self.groupBox)
        self.b_light_on_init.setObjectName(u"b_light_on_init")
        sizePolicy1.setHeightForWidth(self.b_light_on_init.sizePolicy().hasHeightForWidth())
        self.b_light_on_init.setSizePolicy(sizePolicy1)
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

        self.gridLayout_2.addWidget(self.b_light_on_init, 4, 1, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 3, 0, 1, 1)


        self.retranslateUi(test_1)

        QMetaObject.connectSlotsByName(test_1)
    # setupUi

    def retranslateUi(self, test_1):
        test_1.setWindowTitle(QCoreApplication.translate("test_1", u"Test 1", None))
        self.image_label.setText(QCoreApplication.translate("test_1", u"No Image", None))
        self.groupBox.setTitle("")
        self.b_close.setText(QCoreApplication.translate("test_1", u"Close", None))
        self.b_freedrive_on.setText(QCoreApplication.translate("test_1", u"Freedrive ON", None))
        self.b_start_test.setText(QCoreApplication.translate("test_1", u"Start test", None))
        self.b_freedrive_off.setText(QCoreApplication.translate("test_1", u"Freedrive OFF", None))
        self.label_2.setText(QCoreApplication.translate("test_1", u"Set the robot according to the configuration:\n"
"Eye-in-hand: Move the robot so that the camera can detect the test objects and their storage places. \n"
"Eye-to-hand: Move the robot to the starting position to begin the test.\n"
"The image must always be in focus.", None))
        self.b_light_off_init.setText(QCoreApplication.translate("test_1", u"Light OFF", None))
        self.b_light_on_init.setText(QCoreApplication.translate("test_1", u"Light ON", None))
    # retranslateUi

