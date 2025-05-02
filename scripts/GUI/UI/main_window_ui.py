# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QGroupBox, QLabel, QLayout, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSlider,
    QSpacerItem, QStackedWidget, QStatusBar, QTabWidget,
    QToolButton, QWidget)
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from Icons import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(929, 730)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(0, 730))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        MainWindow.setPalette(palette)
        MainWindow.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        icon = QIcon()
        icon.addFile(u":/Icons/fast-forward-regular-180_blue000036.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"	background-color: #ffffff;\n"
"}\n"
"")
        MainWindow.setTabShape(QTabWidget.TabShape.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.groupBox.setStyleSheet(u"QGroupBox {\n"
"	border: none;\n"
"	margin: 10px 0px 0px 0px\n"
"}")
        self.groupBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.groupBox.setFlat(False)
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.b_test_menu = QToolButton(self.groupBox)
        self.b_test_menu.setObjectName(u"b_test_menu")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.b_test_menu.sizePolicy().hasHeightForWidth())
        self.b_test_menu.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setPointSize(10)
        self.b_test_menu.setFont(font)
        self.b_test_menu.setStyleSheet(u"QToolButton {\n"
"    background-color: #3e37ff;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    padding: 10px; /* Uprav\u00ed vnit\u0159n\u00ed prostor tla\u010d\u00edtka */\n"
"	color: white;\n"
"}\n"
"\n"
"QToolButton:checked {\n"
"    background-color: #000036;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/Icons/icons8-robotic-arm-100.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.b_test_menu.setIcon(icon1)
        self.b_test_menu.setIconSize(QSize(40, 40))
        self.b_test_menu.setCheckable(True)
        self.b_test_menu.setAutoExclusive(True)
        self.b_test_menu.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.gridLayout_2.addWidget(self.b_test_menu, 3, 0, 1, 1)

        self.b_home_menu = QToolButton(self.groupBox)
        self.b_home_menu.setObjectName(u"b_home_menu")
        sizePolicy.setHeightForWidth(self.b_home_menu.sizePolicy().hasHeightForWidth())
        self.b_home_menu.setSizePolicy(sizePolicy)
        self.b_home_menu.setFont(font)
        self.b_home_menu.setStyleSheet(u"QToolButton {\n"
"    background-color: #3e37ff;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    padding: 10px; /* Uprav\u00ed vnit\u0159n\u00ed prostor tla\u010d\u00edtka */\n"
"	color: white;\n"
"}\n"
"\n"
"QToolButton:checked {\n"
"    background-color: #000036;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/Icons/home-solid-60_white.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.b_home_menu.setIcon(icon2)
        self.b_home_menu.setIconSize(QSize(40, 40))
        self.b_home_menu.setCheckable(True)
        self.b_home_menu.setChecked(True)
        self.b_home_menu.setAutoExclusive(True)
        self.b_home_menu.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.gridLayout_2.addWidget(self.b_home_menu, 0, 0, 1, 1)

        self.b_calib_menu = QToolButton(self.groupBox)
        self.b_calib_menu.setObjectName(u"b_calib_menu")
        sizePolicy2.setHeightForWidth(self.b_calib_menu.sizePolicy().hasHeightForWidth())
        self.b_calib_menu.setSizePolicy(sizePolicy2)
        self.b_calib_menu.setFont(font)
        self.b_calib_menu.setStyleSheet(u"QToolButton {\n"
"    background-color: #3e37ff;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    padding: 10px; /* Uprav\u00ed vnit\u0159n\u00ed prostor tla\u010d\u00edtka */\n"
"	color: white;\n"
"}\n"
"\n"
"QToolButton:checked {\n"
"    background-color: #000036;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/Icons/target-lock-regular-180_white.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.b_calib_menu.setIcon(icon3)
        self.b_calib_menu.setIconSize(QSize(40, 40))
        self.b_calib_menu.setCheckable(True)
        self.b_calib_menu.setAutoExclusive(True)
        self.b_calib_menu.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.gridLayout_2.addWidget(self.b_calib_menu, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 5, 0, 1, 1)

        self.b_settings_menu = QToolButton(self.groupBox)
        self.b_settings_menu.setObjectName(u"b_settings_menu")
        sizePolicy2.setHeightForWidth(self.b_settings_menu.sizePolicy().hasHeightForWidth())
        self.b_settings_menu.setSizePolicy(sizePolicy2)
        self.b_settings_menu.setFont(font)
        self.b_settings_menu.setStyleSheet(u"QToolButton {\n"
"    background-color: #3e37ff;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    padding: 10px; /* Uprav\u00ed vnit\u0159n\u00ed prostor tla\u010d\u00edtka */\n"
"	color: white;\n"
"}\n"
"\n"
"QToolButton:checked {\n"
"    background-color: #000036;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/Icons/icons8-settings-512.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.b_settings_menu.setIcon(icon4)
        self.b_settings_menu.setIconSize(QSize(40, 40))
        self.b_settings_menu.setCheckable(True)
        self.b_settings_menu.setAutoExclusive(True)
        self.b_settings_menu.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.gridLayout_2.addWidget(self.b_settings_menu, 4, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy3)
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        self.stackedWidget.setPalette(palette1)
        self.stackedWidget.setStyleSheet(u"")
        self.stackedWidget.setFrameShape(QFrame.Shape.NoFrame)
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.gridLayout_3 = QGridLayout(self.page_home)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox_2 = QGroupBox(self.page_home)
        self.groupBox_2.setObjectName(u"groupBox_2")
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(True)
        self.groupBox_2.setFont(font1)
        self.groupBox_2.setStyleSheet(u"#groupBox_2 {\n"
"	border: none;\n"
"	padding: 30px 0px 0px 0px;\n"
"	margin: 0px 6px 0px 9px;\n"
"	background-color: #3e37ff;\n"
"	border-radius: 10px;\n"
"}\n"
"#groupBox_2::title {\n"
"	color: white;  /*zkou\u0161ka*/\n"
"}")
        self.groupBox_2.setFlat(False)
        self.gridLayout_9 = QGridLayout(self.groupBox_2)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.groupBox_8 = QGroupBox(self.groupBox_2)
        self.groupBox_8.setObjectName(u"groupBox_8")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.groupBox_8.sizePolicy().hasHeightForWidth())
        self.groupBox_8.setSizePolicy(sizePolicy4)
        self.groupBox_8.setMinimumSize(QSize(0, 0))
        self.groupBox_8.setStyleSheet(u"#groupBox_8 {\n"
"	border: none;\n"
"	padding: 0px 0px 0px 0px;\n"
"	margin: 0px;\n"
"	background-color: #000036;\n"
"	border-radius: 10px;\n"
"}")
        self.gridLayout_11 = QGridLayout(self.groupBox_8)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.groupBox_4 = QGroupBox(self.groupBox_8)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy4.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy4)
        self.groupBox_4.setMinimumSize(QSize(310, 0))
        self.groupBox_4.setMaximumSize(QSize(370, 16777215))
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        self.groupBox_4.setFont(font2)
        self.groupBox_4.setStyleSheet(u"#groupBox_4 {\n"
"	border: none;\n"
"	padding: 0px;\n"
"	margin: 0px;\n"
"}\n"
"#groupBox_4::title {\n"
"	color: white;\n"
"}")
        self.gridLayout_7 = QGridLayout(self.groupBox_4)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_38 = QLabel(self.groupBox_4)
        self.label_38.setObjectName(u"label_38")
        sizePolicy.setHeightForWidth(self.label_38.sizePolicy().hasHeightForWidth())
        self.label_38.setSizePolicy(sizePolicy)

        self.gridLayout_7.addWidget(self.label_38, 0, 1, 1, 4)

        self.tfm_2_3 = QLabel(self.groupBox_4)
        self.tfm_2_3.setObjectName(u"tfm_2_3")
        sizePolicy4.setHeightForWidth(self.tfm_2_3.sizePolicy().hasHeightForWidth())
        self.tfm_2_3.setSizePolicy(sizePolicy4)
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush1 = QBrush(QColor(255, 255, 255, 128))
        brush1.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        self.tfm_2_3.setPalette(palette2)
        self.tfm_2_3.setStyleSheet(u"color: white")
        self.tfm_2_3.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.tfm_2_3.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.gridLayout_7.addWidget(self.tfm_2_3, 3, 4, 1, 1)

        self.tfm_3_0 = QLabel(self.groupBox_4)
        self.tfm_3_0.setObjectName(u"tfm_3_0")
        sizePolicy4.setHeightForWidth(self.tfm_3_0.sizePolicy().hasHeightForWidth())
        self.tfm_3_0.setSizePolicy(sizePolicy4)
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        self.tfm_3_0.setPalette(palette3)
        self.tfm_3_0.setStyleSheet(u"color: white")
        self.tfm_3_0.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.tfm_3_0.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.gridLayout_7.addWidget(self.tfm_3_0, 4, 1, 1, 1)

        self.tfm_0_2 = QLabel(self.groupBox_4)
        self.tfm_0_2.setObjectName(u"tfm_0_2")
        sizePolicy4.setHeightForWidth(self.tfm_0_2.sizePolicy().hasHeightForWidth())
        self.tfm_0_2.setSizePolicy(sizePolicy4)
        self.tfm_0_2.setMinimumSize(QSize(60, 0))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        self.tfm_0_2.setPalette(palette4)
        self.tfm_0_2.setStyleSheet(u"color: white")
        self.tfm_0_2.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.tfm_0_2.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.gridLayout_7.addWidget(self.tfm_0_2, 1, 3, 1, 1)

        self.label_37 = QLabel(self.groupBox_4)
        self.label_37.setObjectName(u"label_37")
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Active, QPalette.Text, brush)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        self.label_37.setPalette(palette5)
        font3 = QFont()
        font3.setPointSize(72)
        font3.setWeight(QFont.Thin)
        self.label_37.setFont(font3)
        self.label_37.setStyleSheet(u"color: white")
        self.label_37.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing)

        self.gridLayout_7.addWidget(self.label_37, 0, 0, 5, 1)

        self.tfm_1_1 = QLabel(self.groupBox_4)
        self.tfm_1_1.setObjectName(u"tfm_1_1")
        sizePolicy4.setHeightForWidth(self.tfm_1_1.sizePolicy().hasHeightForWidth())
        self.tfm_1_1.setSizePolicy(sizePolicy4)
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette6.setBrush(QPalette.Active, QPalette.Text, brush)
        palette6.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette6.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        self.tfm_1_1.setPalette(palette6)
        self.tfm_1_1.setStyleSheet(u"color: white")
        self.tfm_1_1.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.tfm_1_1.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.gridLayout_7.addWidget(self.tfm_1_1, 2, 2, 1, 1)

        self.tfm_0_0 = QLabel(self.groupBox_4)
        self.tfm_0_0.setObjectName(u"tfm_0_0")
        sizePolicy4.setHeightForWidth(self.tfm_0_0.sizePolicy().hasHeightForWidth())
        self.tfm_0_0.setSizePolicy(sizePolicy4)
        self.tfm_0_0.setMinimumSize(QSize(60, 0))
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette7.setBrush(QPalette.Active, QPalette.Text, brush)
        palette7.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette7.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette7.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        self.tfm_0_0.setPalette(palette7)
        self.tfm_0_0.setStyleSheet(u"color: white")
        self.tfm_0_0.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.tfm_0_0.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.gridLayout_7.addWidget(self.tfm_0_0, 1, 1, 1, 1)

        self.tfm_1_2 = QLabel(self.groupBox_4)
        self.tfm_1_2.setObjectName(u"tfm_1_2")
        sizePolicy4.setHeightForWidth(self.tfm_1_2.sizePolicy().hasHeightForWidth())
        self.tfm_1_2.setSizePolicy(sizePolicy4)
        palette8 = QPalette()
        palette8.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette8.setBrush(QPalette.Active, QPalette.Text, brush)
        palette8.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette8.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette8.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        self.tfm_1_2.setPalette(palette8)
        self.tfm_1_2.setStyleSheet(u"color: white")
        self.tfm_1_2.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.tfm_1_2.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.gridLayout_7.addWidget(self.tfm_1_2, 2, 3, 1, 1)

        self.tfm_0_1 = QLabel(self.groupBox_4)
        self.tfm_0_1.setObjectName(u"tfm_0_1")
        sizePolicy4.setHeightForWidth(self.tfm_0_1.sizePolicy().hasHeightForWidth())
        self.tfm_0_1.setSizePolicy(sizePolicy4)
        self.tfm_0_1.setMinimumSize(QSize(60, 0))
        palette9 = QPalette()
        palette9.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette9.setBrush(QPalette.Active, QPalette.Text, brush)
        palette9.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette9.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette9.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        self.tfm_0_1.setPalette(palette9)
        self.tfm_0_1.setStyleSheet(u"color: white")
        self.tfm_0_1.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.tfm_0_1.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.gridLayout_7.addWidget(self.tfm_0_1, 1, 2, 1, 1)

        self.tfm_1_0 = QLabel(self.groupBox_4)
        self.tfm_1_0.setObjectName(u"tfm_1_0")
        sizePolicy4.setHeightForWidth(self.tfm_1_0.sizePolicy().hasHeightForWidth())
        self.tfm_1_0.setSizePolicy(sizePolicy4)
        palette10 = QPalette()
        palette10.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette10.setBrush(QPalette.Active, QPalette.Text, brush)
        palette10.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette10.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette10.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        self.tfm_1_0.setPalette(palette10)
        self.tfm_1_0.setStyleSheet(u"color: white")
        self.tfm_1_0.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.tfm_1_0.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.gridLayout_7.addWidget(self.tfm_1_0, 2, 1, 1, 1)

        self.tfm_3_2 = QLabel(self.groupBox_4)
        self.tfm_3_2.setObjectName(u"tfm_3_2")
        sizePolicy4.setHeightForWidth(self.tfm_3_2.sizePolicy().hasHeightForWidth())
        self.tfm_3_2.setSizePolicy(sizePolicy4)
        palette11 = QPalette()
        palette11.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette11.setBrush(QPalette.Active, QPalette.Text, brush)
        palette11.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette11.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette11.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette11.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette11.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        self.tfm_3_2.setPalette(palette11)
        self.tfm_3_2.setStyleSheet(u"color: white")
        self.tfm_3_2.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.tfm_3_2.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.gridLayout_7.addWidget(self.tfm_3_2, 4, 3, 1, 1)

        self.tfm_2_0 = QLabel(self.groupBox_4)
        self.tfm_2_0.setObjectName(u"tfm_2_0")
        sizePolicy4.setHeightForWidth(self.tfm_2_0.sizePolicy().hasHeightForWidth())
        self.tfm_2_0.setSizePolicy(sizePolicy4)
        palette12 = QPalette()
        palette12.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette12.setBrush(QPalette.Active, QPalette.Text, brush)
        palette12.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette12.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette12.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette12.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette12.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        self.tfm_2_0.setPalette(palette12)
        self.tfm_2_0.setStyleSheet(u"color: white")
        self.tfm_2_0.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.tfm_2_0.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.gridLayout_7.addWidget(self.tfm_2_0, 3, 1, 1, 1)

        self.tfm_3_3 = QLabel(self.groupBox_4)
        self.tfm_3_3.setObjectName(u"tfm_3_3")
        sizePolicy4.setHeightForWidth(self.tfm_3_3.sizePolicy().hasHeightForWidth())
        self.tfm_3_3.setSizePolicy(sizePolicy4)
        palette13 = QPalette()
        palette13.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette13.setBrush(QPalette.Active, QPalette.Text, brush)
        palette13.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette13.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette13.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette13.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette13.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        self.tfm_3_3.setPalette(palette13)
        self.tfm_3_3.setStyleSheet(u"color: white")
        self.tfm_3_3.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.tfm_3_3.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.gridLayout_7.addWidget(self.tfm_3_3, 4, 4, 1, 1)

        self.tfm_2_2 = QLabel(self.groupBox_4)
        self.tfm_2_2.setObjectName(u"tfm_2_2")
        sizePolicy4.setHeightForWidth(self.tfm_2_2.sizePolicy().hasHeightForWidth())
        self.tfm_2_2.setSizePolicy(sizePolicy4)
        palette14 = QPalette()
        palette14.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette14.setBrush(QPalette.Active, QPalette.Text, brush)
        palette14.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette14.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette14.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette14.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette14.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        self.tfm_2_2.setPalette(palette14)
        self.tfm_2_2.setStyleSheet(u"color: white")
        self.tfm_2_2.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.tfm_2_2.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.gridLayout_7.addWidget(self.tfm_2_2, 3, 3, 1, 1)

        self.tfm_2_1 = QLabel(self.groupBox_4)
        self.tfm_2_1.setObjectName(u"tfm_2_1")
        sizePolicy4.setHeightForWidth(self.tfm_2_1.sizePolicy().hasHeightForWidth())
        self.tfm_2_1.setSizePolicy(sizePolicy4)
        palette15 = QPalette()
        palette15.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette15.setBrush(QPalette.Active, QPalette.Text, brush)
        palette15.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette15.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette15.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette15.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette15.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        self.tfm_2_1.setPalette(palette15)
        self.tfm_2_1.setStyleSheet(u"color: white")
        self.tfm_2_1.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.tfm_2_1.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.gridLayout_7.addWidget(self.tfm_2_1, 3, 2, 1, 1)

        self.label_39 = QLabel(self.groupBox_4)
        self.label_39.setObjectName(u"label_39")
        palette16 = QPalette()
        palette16.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette16.setBrush(QPalette.Active, QPalette.Text, brush)
        palette16.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette16.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette16.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette16.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette16.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette16.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette16.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        self.label_39.setPalette(palette16)
        self.label_39.setFont(font3)
        self.label_39.setStyleSheet(u"color: white")
        self.label_39.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.gridLayout_7.addWidget(self.label_39, 0, 5, 5, 1)

        self.tfm_0_3 = QLabel(self.groupBox_4)
        self.tfm_0_3.setObjectName(u"tfm_0_3")
        sizePolicy4.setHeightForWidth(self.tfm_0_3.sizePolicy().hasHeightForWidth())
        self.tfm_0_3.setSizePolicy(sizePolicy4)
        self.tfm_0_3.setMinimumSize(QSize(60, 0))
        palette17 = QPalette()
        palette17.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette17.setBrush(QPalette.Active, QPalette.Text, brush)
        palette17.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette17.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette17.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette17.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette17.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette17.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette17.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        self.tfm_0_3.setPalette(palette17)
        self.tfm_0_3.setStyleSheet(u"color: white")
        self.tfm_0_3.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.tfm_0_3.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.gridLayout_7.addWidget(self.tfm_0_3, 1, 4, 1, 1)

        self.tfm_3_1 = QLabel(self.groupBox_4)
        self.tfm_3_1.setObjectName(u"tfm_3_1")
        sizePolicy4.setHeightForWidth(self.tfm_3_1.sizePolicy().hasHeightForWidth())
        self.tfm_3_1.setSizePolicy(sizePolicy4)
        palette18 = QPalette()
        palette18.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette18.setBrush(QPalette.Active, QPalette.Text, brush)
        palette18.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette18.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette18.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette18.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette18.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette18.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette18.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        self.tfm_3_1.setPalette(palette18)
        self.tfm_3_1.setStyleSheet(u"color: white")
        self.tfm_3_1.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.tfm_3_1.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.gridLayout_7.addWidget(self.tfm_3_1, 4, 2, 1, 1)

        self.tfm_1_3 = QLabel(self.groupBox_4)
        self.tfm_1_3.setObjectName(u"tfm_1_3")
        sizePolicy4.setHeightForWidth(self.tfm_1_3.sizePolicy().hasHeightForWidth())
        self.tfm_1_3.setSizePolicy(sizePolicy4)
        palette19 = QPalette()
        palette19.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette19.setBrush(QPalette.Active, QPalette.Text, brush)
        palette19.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette19.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette19.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette19.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette19.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette19.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette19.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette19.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette19.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette19.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        self.tfm_1_3.setPalette(palette19)
        self.tfm_1_3.setStyleSheet(u"color: white")
        self.tfm_1_3.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.tfm_1_3.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.gridLayout_7.addWidget(self.tfm_1_3, 2, 4, 1, 1)


        self.gridLayout_11.addWidget(self.groupBox_4, 0, 0, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(0, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_6, 0, 1, 2, 1)

        self.groupBox_6 = QGroupBox(self.groupBox_8)
        self.groupBox_6.setObjectName(u"groupBox_6")
        palette20 = QPalette()
        self.groupBox_6.setPalette(palette20)
        self.groupBox_6.setFont(font2)
        self.groupBox_6.setStyleSheet(u"#groupBox_6 {\n"
"	border: none;\n"
"	padding: 15px 0px 0px 0px;\n"
"	margin: 0px;\n"
"}\n"
"#groupBox_6::title {\n"
"	color: white;\n"
"}")
        self.gridLayout_8 = QGridLayout(self.groupBox_6)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.pose_vector = QLabel(self.groupBox_6)
        self.pose_vector.setObjectName(u"pose_vector")
        sizePolicy4.setHeightForWidth(self.pose_vector.sizePolicy().hasHeightForWidth())
        self.pose_vector.setSizePolicy(sizePolicy4)
        self.pose_vector.setMinimumSize(QSize(0, 32))
        palette21 = QPalette()
        palette21.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette21.setBrush(QPalette.Active, QPalette.Text, brush)
        palette21.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette21.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette21.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette21.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette21.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette21.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette21.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette21.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette21.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette21.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        self.pose_vector.setPalette(palette21)
        self.pose_vector.setStyleSheet(u"color: white")
        self.pose_vector.setWordWrap(True)
        self.pose_vector.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.gridLayout_8.addWidget(self.pose_vector, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.groupBox_6, 1, 0, 1, 1)


        self.gridLayout_9.addWidget(self.groupBox_8, 0, 2, 2, 1)

        self.groupBox_7 = QGroupBox(self.groupBox_2)
        self.groupBox_7.setObjectName(u"groupBox_7")
        sizePolicy4.setHeightForWidth(self.groupBox_7.sizePolicy().hasHeightForWidth())
        self.groupBox_7.setSizePolicy(sizePolicy4)
        self.groupBox_7.setMinimumSize(QSize(368, 0))
        self.groupBox_7.setStyleSheet(u"#groupBox_7 {\n"
"	border: none;\n"
"	padding: 0px 0px 0px 0px;\n"
"	margin: 0px;\n"
"	background-color: #000036;\n"
"	border-radius: 10px;\n"
"}\n"
"")
        self.gridLayout_10 = QGridLayout(self.groupBox_7)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_10.addItem(self.verticalSpacer_3, 2, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.groupBox_7)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy4.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy4)
        self.groupBox_3.setMinimumSize(QSize(100, 0))
        self.groupBox_3.setMaximumSize(QSize(300, 16777215))
        palette22 = QPalette()
        self.groupBox_3.setPalette(palette22)
        self.groupBox_3.setFont(font2)
        self.groupBox_3.setStyleSheet(u"#groupBox_3 {\n"
"	border: none;\n"
"	padding: 0px;\n"
"	margin: 0px;\n"
"}\n"
"#groupBox_3::title {\n"
"	color: white;\n"
"}")
        self.gridLayout_5 = QGridLayout(self.groupBox_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.cm_0_2 = QLabel(self.groupBox_3)
        self.cm_0_2.setObjectName(u"cm_0_2")
        sizePolicy4.setHeightForWidth(self.cm_0_2.sizePolicy().hasHeightForWidth())
        self.cm_0_2.setSizePolicy(sizePolicy4)
        self.cm_0_2.setMinimumSize(QSize(60, 0))
        palette23 = QPalette()
        palette23.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette23.setBrush(QPalette.Active, QPalette.Text, brush)
        palette23.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette23.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette23.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette23.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette23.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette23.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette23.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette23.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette23.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette23.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        self.cm_0_2.setPalette(palette23)
        self.cm_0_2.setStyleSheet(u"color: white")
        self.cm_0_2.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.cm_0_2.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.gridLayout_5.addWidget(self.cm_0_2, 1, 3, 1, 1)

        self.cm_0_0 = QLabel(self.groupBox_3)
        self.cm_0_0.setObjectName(u"cm_0_0")
        sizePolicy4.setHeightForWidth(self.cm_0_0.sizePolicy().hasHeightForWidth())
        self.cm_0_0.setSizePolicy(sizePolicy4)
        self.cm_0_0.setMinimumSize(QSize(60, 0))
        palette24 = QPalette()
        palette24.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette24.setBrush(QPalette.Active, QPalette.Text, brush)
        palette24.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette24.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette24.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette24.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette24.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette24.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette24.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette24.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette24.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette24.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        self.cm_0_0.setPalette(palette24)
        self.cm_0_0.setStyleSheet(u"color: white")
        self.cm_0_0.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.cm_0_0.setMargin(0)
        self.cm_0_0.setIndent(-1)
        self.cm_0_0.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.gridLayout_5.addWidget(self.cm_0_0, 1, 1, 1, 1)

        self.cm_1_1 = QLabel(self.groupBox_3)
        self.cm_1_1.setObjectName(u"cm_1_1")
        sizePolicy4.setHeightForWidth(self.cm_1_1.sizePolicy().hasHeightForWidth())
        self.cm_1_1.setSizePolicy(sizePolicy4)
        palette25 = QPalette()
        palette25.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette25.setBrush(QPalette.Active, QPalette.Text, brush)
        palette25.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette25.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette25.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette25.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette25.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette25.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette25.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette25.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette25.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette25.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        self.cm_1_1.setPalette(palette25)
        self.cm_1_1.setStyleSheet(u"color: white")
        self.cm_1_1.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.cm_1_1.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.gridLayout_5.addWidget(self.cm_1_1, 2, 2, 1, 1)

        self.cm_0_1 = QLabel(self.groupBox_3)
        self.cm_0_1.setObjectName(u"cm_0_1")
        sizePolicy4.setHeightForWidth(self.cm_0_1.sizePolicy().hasHeightForWidth())
        self.cm_0_1.setSizePolicy(sizePolicy4)
        self.cm_0_1.setMinimumSize(QSize(60, 0))
        palette26 = QPalette()
        palette26.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette26.setBrush(QPalette.Active, QPalette.Text, brush)
        palette26.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette26.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette26.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette26.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette26.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette26.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette26.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette26.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette26.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette26.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        self.cm_0_1.setPalette(palette26)
        self.cm_0_1.setStyleSheet(u"color: white")
        self.cm_0_1.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.cm_0_1.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.gridLayout_5.addWidget(self.cm_0_1, 1, 2, 1, 1)

        self.cm_2_0 = QLabel(self.groupBox_3)
        self.cm_2_0.setObjectName(u"cm_2_0")
        sizePolicy4.setHeightForWidth(self.cm_2_0.sizePolicy().hasHeightForWidth())
        self.cm_2_0.setSizePolicy(sizePolicy4)
        palette27 = QPalette()
        palette27.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette27.setBrush(QPalette.Active, QPalette.Text, brush)
        palette27.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette27.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette27.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette27.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette27.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette27.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette27.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette27.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette27.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette27.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        self.cm_2_0.setPalette(palette27)
        self.cm_2_0.setStyleSheet(u"color: white")
        self.cm_2_0.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.cm_2_0.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.gridLayout_5.addWidget(self.cm_2_0, 3, 1, 1, 1)

        self.cm_2_1 = QLabel(self.groupBox_3)
        self.cm_2_1.setObjectName(u"cm_2_1")
        sizePolicy4.setHeightForWidth(self.cm_2_1.sizePolicy().hasHeightForWidth())
        self.cm_2_1.setSizePolicy(sizePolicy4)
        palette28 = QPalette()
        palette28.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette28.setBrush(QPalette.Active, QPalette.Text, brush)
        palette28.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette28.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette28.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette28.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette28.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette28.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette28.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette28.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette28.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette28.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        self.cm_2_1.setPalette(palette28)
        self.cm_2_1.setStyleSheet(u"color: white")
        self.cm_2_1.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.cm_2_1.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.gridLayout_5.addWidget(self.cm_2_1, 3, 2, 1, 1)

        self.cm_1_0 = QLabel(self.groupBox_3)
        self.cm_1_0.setObjectName(u"cm_1_0")
        sizePolicy4.setHeightForWidth(self.cm_1_0.sizePolicy().hasHeightForWidth())
        self.cm_1_0.setSizePolicy(sizePolicy4)
        palette29 = QPalette()
        palette29.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette29.setBrush(QPalette.Active, QPalette.Text, brush)
        palette29.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette29.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette29.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette29.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette29.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette29.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette29.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette29.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette29.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette29.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        self.cm_1_0.setPalette(palette29)
        self.cm_1_0.setStyleSheet(u"color: white")
        self.cm_1_0.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.cm_1_0.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.gridLayout_5.addWidget(self.cm_1_0, 2, 1, 1, 1)

        self.cm_1_2 = QLabel(self.groupBox_3)
        self.cm_1_2.setObjectName(u"cm_1_2")
        sizePolicy4.setHeightForWidth(self.cm_1_2.sizePolicy().hasHeightForWidth())
        self.cm_1_2.setSizePolicy(sizePolicy4)
        palette30 = QPalette()
        palette30.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette30.setBrush(QPalette.Active, QPalette.Text, brush)
        palette30.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette30.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette30.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette30.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette30.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette30.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette30.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette30.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette30.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette30.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        self.cm_1_2.setPalette(palette30)
        self.cm_1_2.setStyleSheet(u"color: white")
        self.cm_1_2.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.cm_1_2.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.gridLayout_5.addWidget(self.cm_1_2, 2, 3, 1, 1)

        self.cm_2_2 = QLabel(self.groupBox_3)
        self.cm_2_2.setObjectName(u"cm_2_2")
        sizePolicy4.setHeightForWidth(self.cm_2_2.sizePolicy().hasHeightForWidth())
        self.cm_2_2.setSizePolicy(sizePolicy4)
        palette31 = QPalette()
        palette31.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette31.setBrush(QPalette.Active, QPalette.Text, brush)
        palette31.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette31.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette31.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette31.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette31.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette31.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette31.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette31.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette31.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette31.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        self.cm_2_2.setPalette(palette31)
        self.cm_2_2.setStyleSheet(u"color: white")
        self.cm_2_2.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.cm_2_2.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.gridLayout_5.addWidget(self.cm_2_2, 3, 3, 1, 1)

        self.label_12 = QLabel(self.groupBox_3)
        self.label_12.setObjectName(u"label_12")
        palette32 = QPalette()
        palette32.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette32.setBrush(QPalette.Active, QPalette.Text, brush)
        palette32.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette32.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette32.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette32.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette32.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette32.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette32.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette32.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette32.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette32.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        self.label_12.setPalette(palette32)
        font4 = QFont()
        font4.setPointSize(48)
        self.label_12.setFont(font4)
        self.label_12.setStyleSheet(u"color: white")
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing)

        self.gridLayout_5.addWidget(self.label_12, 0, 0, 4, 1)

        self.label_15 = QLabel(self.groupBox_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.gridLayout_5.addWidget(self.label_15, 0, 1, 1, 3)

        self.label_27 = QLabel(self.groupBox_3)
        self.label_27.setObjectName(u"label_27")
        palette33 = QPalette()
        palette33.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette33.setBrush(QPalette.Active, QPalette.Text, brush)
        palette33.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette33.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette33.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette33.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette33.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette33.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette33.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette33.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette33.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette33.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        self.label_27.setPalette(palette33)
        self.label_27.setFont(font4)
        self.label_27.setStyleSheet(u"color: white")
        self.label_27.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.gridLayout_5.addWidget(self.label_27, 0, 4, 4, 1)


        self.gridLayout_10.addWidget(self.groupBox_3, 0, 0, 1, 1)

        self.groupBox_5 = QGroupBox(self.groupBox_7)
        self.groupBox_5.setObjectName(u"groupBox_5")
        palette34 = QPalette()
        self.groupBox_5.setPalette(palette34)
        self.groupBox_5.setFont(font2)
        self.groupBox_5.setStyleSheet(u"#groupBox_5 {\n"
"	border: none;\n"
"	padding: 15px 0px 0px 0px;\n"
"	margin: 0px;\n"
"}\n"
"#groupBox_5::title {\n"
"	color: white;\n"
"}")
        self.gridLayout_4 = QGridLayout(self.groupBox_5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.dist_coeff = QLabel(self.groupBox_5)
        self.dist_coeff.setObjectName(u"dist_coeff")
        sizePolicy4.setHeightForWidth(self.dist_coeff.sizePolicy().hasHeightForWidth())
        self.dist_coeff.setSizePolicy(sizePolicy4)
        palette35 = QPalette()
        palette35.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette35.setBrush(QPalette.Active, QPalette.Text, brush)
        palette35.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette35.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette35.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette35.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette35.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette35.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette35.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette35.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette35.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette35.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        self.dist_coeff.setPalette(palette35)
        self.dist_coeff.setStyleSheet(u"color: white")
        self.dist_coeff.setWordWrap(True)
        self.dist_coeff.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.gridLayout_4.addWidget(self.dist_coeff, 0, 0, 1, 1)


        self.gridLayout_10.addWidget(self.groupBox_5, 1, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(0, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer, 0, 1, 3, 1)


        self.gridLayout_9.addWidget(self.groupBox_7, 0, 0, 2, 1)


        self.gridLayout_3.addWidget(self.groupBox_2, 4, 0, 1, 2)

        self.groupBox_9 = QGroupBox(self.page_home)
        self.groupBox_9.setObjectName(u"groupBox_9")
        sizePolicy3.setHeightForWidth(self.groupBox_9.sizePolicy().hasHeightForWidth())
        self.groupBox_9.setSizePolicy(sizePolicy3)
        self.groupBox_9.setStyleSheet(u"#groupBox_9 {\n"
"	border: none;\n"
"	padding: 0px 0px 0px 0px;\n"
"	margin: 0px;\n"
"}\n"
"")
        self.gridLayout_39 = QGridLayout(self.groupBox_9)
        self.gridLayout_39.setObjectName(u"gridLayout_39")
        self.gridLayout_39.setContentsMargins(9, -1, 0, -1)
        self.groupBox_32 = QGroupBox(self.groupBox_9)
        self.groupBox_32.setObjectName(u"groupBox_32")
        sizePolicy3.setHeightForWidth(self.groupBox_32.sizePolicy().hasHeightForWidth())
        self.groupBox_32.setSizePolicy(sizePolicy3)
        self.groupBox_32.setMinimumSize(QSize(295, 118))
        self.groupBox_32.setStyleSheet(u"QGroupBox {\n"
"	border: none;\n"
"	margin: 0px 0px 0px 0px;\n"
"	padding: 0px 0px 0px 0px;\n"
"}")
        self.gridLayout_35 = QGridLayout(self.groupBox_32)
        self.gridLayout_35.setObjectName(u"gridLayout_35")
        self.gridLayout_35.setContentsMargins(0, 0, 0, 0)
        self.b_new_calib = QToolButton(self.groupBox_32)
        self.b_new_calib.setObjectName(u"b_new_calib")
        sizePolicy3.setHeightForWidth(self.b_new_calib.sizePolicy().hasHeightForWidth())
        self.b_new_calib.setSizePolicy(sizePolicy3)
        self.b_new_calib.setMinimumSize(QSize(0, 0))
        font5 = QFont()
        font5.setPointSize(11)
        font5.setWeight(QFont.DemiBold)
        self.b_new_calib.setFont(font5)
        self.b_new_calib.setStyleSheet(u"QToolButton {\n"
"	background-color: #3e37ff;\n"
"	border: none;\n"
"    border-radius: 10px;\n"
"    padding: 10px; \n"
"	color: white;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"	background-color: #000036;\n"
"}")
        self.b_new_calib.setIcon(icon3)
        self.b_new_calib.setIconSize(QSize(50, 50))
        self.b_new_calib.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.gridLayout_35.addWidget(self.b_new_calib, 0, 0, 1, 1)


        self.gridLayout_39.addWidget(self.groupBox_32, 0, 0, 1, 1)

        self.groupBox_30 = QGroupBox(self.groupBox_9)
        self.groupBox_30.setObjectName(u"groupBox_30")
        sizePolicy3.setHeightForWidth(self.groupBox_30.sizePolicy().hasHeightForWidth())
        self.groupBox_30.setSizePolicy(sizePolicy3)
        self.groupBox_30.setMinimumSize(QSize(295, 118))
        self.groupBox_30.setStyleSheet(u"QGroupBox {\n"
"	border: none;\n"
"	margin: 0px 0px 0px 0px;\n"
"	padding: 0px 0px 0px 0px;\n"
"}")
        self.gridLayout_40 = QGridLayout(self.groupBox_30)
        self.gridLayout_40.setObjectName(u"gridLayout_40")
        self.gridLayout_40.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.gridLayout_40.setContentsMargins(0, 0, 0, 0)
        self.b_upload_data = QToolButton(self.groupBox_30)
        self.b_upload_data.setObjectName(u"b_upload_data")
        sizePolicy3.setHeightForWidth(self.b_upload_data.sizePolicy().hasHeightForWidth())
        self.b_upload_data.setSizePolicy(sizePolicy3)
        self.b_upload_data.setMinimumSize(QSize(0, 0))
        self.b_upload_data.setFont(font5)
        self.b_upload_data.setStyleSheet(u"QToolButton {\n"
"	background-color: #3e37ff;\n"
"	border: none;\n"
"    border-radius: 10px;\n"
"    padding: 10px; \n"
"	color: white;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"	background-color: #000036;\n"
"}\n"
"\n"
"QToolButton:disabled {\n"
"    background-color: #808080; /* \u0160ed\u00e1 barva pro deaktivovan\u00e9 tla\u010d\u00edtko */\n"
"    color: #c0c0c0; /* Sv\u011btlej\u0161\u00ed \u0161ed\u00e1 barva textu */\n"
"    border: none;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/Icons/icons8-upload-96.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.b_upload_data.setIcon(icon5)
        self.b_upload_data.setIconSize(QSize(50, 50))
        self.b_upload_data.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.gridLayout_40.addWidget(self.b_upload_data, 0, 0, 1, 1)

        self.b_calculate = QToolButton(self.groupBox_30)
        self.b_calculate.setObjectName(u"b_calculate")
        sizePolicy3.setHeightForWidth(self.b_calculate.sizePolicy().hasHeightForWidth())
        self.b_calculate.setSizePolicy(sizePolicy3)
        self.b_calculate.setMinimumSize(QSize(0, 0))
        self.b_calculate.setFont(font5)
        self.b_calculate.setStyleSheet(u"QToolButton {\n"
"	background-color: #3e37ff;\n"
"	border: none;\n"
"    border-radius: 10px;\n"
"    padding: 10px; \n"
"	color: white;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"	background-color: #000036;\n"
"}\n"
"\n"
"QToolButton:disabled {\n"
"    background-color: #808080; /* \u0160ed\u00e1 barva pro deaktivovan\u00e9 tla\u010d\u00edtko */\n"
"    color: #c0c0c0; /* Sv\u011btlej\u0161\u00ed \u0161ed\u00e1 barva textu */\n"
"    border: none;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/Icons/icons8-math-96.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.b_calculate.setIcon(icon6)
        self.b_calculate.setIconSize(QSize(50, 50))
        self.b_calculate.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.gridLayout_40.addWidget(self.b_calculate, 0, 1, 1, 1)


        self.gridLayout_39.addWidget(self.groupBox_30, 3, 0, 1, 1)

        self.groupBox_35 = QGroupBox(self.groupBox_9)
        self.groupBox_35.setObjectName(u"groupBox_35")
        sizePolicy3.setHeightForWidth(self.groupBox_35.sizePolicy().hasHeightForWidth())
        self.groupBox_35.setSizePolicy(sizePolicy3)
        self.groupBox_35.setMinimumSize(QSize(295, 118))
        self.groupBox_35.setStyleSheet(u"QGroupBox {\n"
"	border: none;\n"
"	margin: 0px 0px 0px 0px;\n"
"	padding: 0px 0px 0px 0px;\n"
"}")
        self.gridLayout_38 = QGridLayout(self.groupBox_35)
        self.gridLayout_38.setObjectName(u"gridLayout_38")
        self.gridLayout_38.setContentsMargins(0, 0, 0, 0)
        self.b_test = QToolButton(self.groupBox_35)
        self.b_test.setObjectName(u"b_test")
        sizePolicy3.setHeightForWidth(self.b_test.sizePolicy().hasHeightForWidth())
        self.b_test.setSizePolicy(sizePolicy3)
        self.b_test.setMinimumSize(QSize(0, 0))
        self.b_test.setFont(font5)
        self.b_test.setStyleSheet(u"QToolButton {\n"
"	background-color: #3e37ff;\n"
"	border: none;\n"
"    border-radius: 10px;\n"
"    padding: 10px; \n"
"	color: white;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"	background-color: #000036;\n"
"}")
        self.b_test.setIcon(icon1)
        self.b_test.setIconSize(QSize(50, 50))
        self.b_test.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.gridLayout_38.addWidget(self.b_test, 0, 0, 1, 1)


        self.gridLayout_39.addWidget(self.groupBox_35, 3, 1, 1, 1)

        self.groupBox_33 = QGroupBox(self.groupBox_9)
        self.groupBox_33.setObjectName(u"groupBox_33")
        sizePolicy3.setHeightForWidth(self.groupBox_33.sizePolicy().hasHeightForWidth())
        self.groupBox_33.setSizePolicy(sizePolicy3)
        self.groupBox_33.setMinimumSize(QSize(295, 118))
        self.groupBox_33.setStyleSheet(u"QGroupBox {\n"
"	border: none;\n"
"	margin: 0px 0px 0px 0px;\n"
"	padding: 0px 0px 0px 0px;\n"
"}")
        self.gridLayout_36 = QGridLayout(self.groupBox_33)
        self.gridLayout_36.setObjectName(u"gridLayout_36")
        self.gridLayout_36.setContentsMargins(0, 0, 0, 0)
        self.b_upload_calib = QToolButton(self.groupBox_33)
        self.b_upload_calib.setObjectName(u"b_upload_calib")
        sizePolicy3.setHeightForWidth(self.b_upload_calib.sizePolicy().hasHeightForWidth())
        self.b_upload_calib.setSizePolicy(sizePolicy3)
        self.b_upload_calib.setMinimumSize(QSize(0, 0))
        self.b_upload_calib.setFont(font5)
        self.b_upload_calib.setStyleSheet(u"QToolButton {\n"
"	background-color: #3e37ff;\n"
"	border: none;\n"
"    border-radius: 10px;\n"
"    padding: 10px; \n"
"	color: white;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"	background-color: #000036;\n"
"}")
        self.b_upload_calib.setIcon(icon5)
        self.b_upload_calib.setIconSize(QSize(50, 50))
        self.b_upload_calib.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.gridLayout_36.addWidget(self.b_upload_calib, 0, 0, 1, 1)


        self.gridLayout_39.addWidget(self.groupBox_33, 0, 1, 1, 1)

        self.groupBox_34 = QGroupBox(self.groupBox_9)
        self.groupBox_34.setObjectName(u"groupBox_34")
        sizePolicy3.setHeightForWidth(self.groupBox_34.sizePolicy().hasHeightForWidth())
        self.groupBox_34.setSizePolicy(sizePolicy3)
        self.groupBox_34.setMinimumSize(QSize(295, 118))
        self.groupBox_34.setStyleSheet(u"QGroupBox {\n"
"	border: none;\n"
"	margin: 0px 0px 0px 0px;\n"
"	padding: 0px 0px 0px 0px;\n"
"}")
        self.gridLayout_37 = QGridLayout(self.groupBox_34)
        self.gridLayout_37.setObjectName(u"gridLayout_37")
        self.gridLayout_37.setContentsMargins(0, 0, 0, 0)
        self.b_save_data = QToolButton(self.groupBox_34)
        self.b_save_data.setObjectName(u"b_save_data")
        sizePolicy3.setHeightForWidth(self.b_save_data.sizePolicy().hasHeightForWidth())
        self.b_save_data.setSizePolicy(sizePolicy3)
        self.b_save_data.setMinimumSize(QSize(0, 0))
        self.b_save_data.setFont(font5)
        self.b_save_data.setStyleSheet(u"QToolButton {\n"
"	background-color: #3e37ff;\n"
"	border: none;\n"
"    border-radius: 10px;\n"
"    padding: 10px; \n"
"	color: white;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"	background-color: #000036;\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/Icons/icons8-downloading-updates-96.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.b_save_data.setIcon(icon7)
        self.b_save_data.setIconSize(QSize(50, 50))
        self.b_save_data.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.gridLayout_37.addWidget(self.b_save_data, 0, 0, 1, 1)


        self.gridLayout_39.addWidget(self.groupBox_34, 2, 1, 1, 1)

        self.groupBox_31 = QGroupBox(self.groupBox_9)
        self.groupBox_31.setObjectName(u"groupBox_31")
        sizePolicy3.setHeightForWidth(self.groupBox_31.sizePolicy().hasHeightForWidth())
        self.groupBox_31.setSizePolicy(sizePolicy3)
        self.groupBox_31.setMinimumSize(QSize(295, 118))
        self.groupBox_31.setStyleSheet(u"QGroupBox {\n"
"	border: none;\n"
"	margin: 0px 0px 0px 0px;\n"
"	padding: 0px 0px 0px 0px;\n"
"}")
        self.gridLayout_12 = QGridLayout(self.groupBox_31)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.b_save_results = QToolButton(self.groupBox_31)
        self.b_save_results.setObjectName(u"b_save_results")
        sizePolicy3.setHeightForWidth(self.b_save_results.sizePolicy().hasHeightForWidth())
        self.b_save_results.setSizePolicy(sizePolicy3)
        self.b_save_results.setMinimumSize(QSize(0, 0))
        self.b_save_results.setFont(font5)
        self.b_save_results.setStyleSheet(u"QToolButton {\n"
"	background-color: #3e37ff;\n"
"	border: none;\n"
"    border-radius: 10px;\n"
"    padding: 10px; \n"
"	color: white;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"	background-color: #000036;\n"
"}")
        self.b_save_results.setIcon(icon7)
        self.b_save_results.setIconSize(QSize(50, 50))
        self.b_save_results.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.gridLayout_12.addWidget(self.b_save_results, 0, 0, 1, 1)


        self.gridLayout_39.addWidget(self.groupBox_31, 2, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_9, 3, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_home)
        self.page_calib = QWidget()
        self.page_calib.setObjectName(u"page_calib")
        self.gridLayout_19 = QGridLayout(self.page_calib)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.groupBox_15 = QGroupBox(self.page_calib)
        self.groupBox_15.setObjectName(u"groupBox_15")
        self.groupBox_15.setStyleSheet(u"QGroupBox {\n"
"	border: none;\n"
"	padding: 0px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"	color: #000036;\n"
"}")
        self.gridLayout_18 = QGridLayout(self.groupBox_15)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.label_21 = QLabel(self.groupBox_15)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font2)
        self.label_21.setStyleSheet(u"color: #000036;")

        self.gridLayout_18.addWidget(self.label_21, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_18.addItem(self.horizontalSpacer_2, 0, 3, 1, 1)

        self.comboBox_methods = QComboBox(self.groupBox_15)
        self.comboBox_methods.addItem("")
        self.comboBox_methods.addItem("")
        self.comboBox_methods.addItem("")
        self.comboBox_methods.addItem("")
        self.comboBox_methods.addItem("")
        self.comboBox_methods.addItem("")
        self.comboBox_methods.addItem("")
        self.comboBox_methods.setObjectName(u"comboBox_methods")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.comboBox_methods.sizePolicy().hasHeightForWidth())
        self.comboBox_methods.setSizePolicy(sizePolicy5)
        self.comboBox_methods.setMinimumSize(QSize(200, 0))
        font6 = QFont()
        font6.setPointSize(9)
        self.comboBox_methods.setFont(font6)

        self.gridLayout_18.addWidget(self.comboBox_methods, 0, 2, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_18.addItem(self.horizontalSpacer_4, 0, 1, 1, 1)


        self.gridLayout_19.addWidget(self.groupBox_15, 3, 0, 1, 2)

        self.groupBox_13 = QGroupBox(self.page_calib)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.groupBox_13.setStyleSheet(u"QGroupBox {\n"
"	border: none;\n"
"	padding: 0px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"	color: #000036;\n"
"}")
        self.gridLayout_15 = QGridLayout(self.groupBox_13)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.label_6 = QLabel(self.groupBox_13)
        self.label_6.setObjectName(u"label_6")
        sizePolicy3.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy3)
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"color: #000036;")

        self.gridLayout_15.addWidget(self.label_6, 0, 0, 1, 1)

        self.label_11 = QLabel(self.groupBox_13)
        self.label_11.setObjectName(u"label_11")
        sizePolicy3.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy3)
        self.label_11.setFont(font5)
        self.label_11.setStyleSheet(u"color: #000036;")
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_15.addWidget(self.label_11, 0, 1, 1, 1)

        self.slider_light = QSlider(self.groupBox_13)
        self.slider_light.setObjectName(u"slider_light")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.slider_light.sizePolicy().hasHeightForWidth())
        self.slider_light.setSizePolicy(sizePolicy6)
        self.slider_light.setMinimumSize(QSize(100, 0))
        self.slider_light.setStyleSheet(u"QSlider::groove:horizontal {\n"
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
"}\n"
"/*\n"
"QSlider::sub-page:horizontal {\n"
"    background: #0078D7;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: #bbb;\n"
"    border-radius: 4px;\n"
"}\n"
"*/")
        self.slider_light.setMinimum(0)
        self.slider_light.setMaximum(1)
        self.slider_light.setValue(0)
        self.slider_light.setSliderPosition(0)
        self.slider_light.setOrientation(Qt.Orientation.Horizontal)
        self.slider_light.setInvertedControls(False)

        self.gridLayout_15.addWidget(self.slider_light, 0, 2, 1, 1)

        self.label_14 = QLabel(self.groupBox_13)
        self.label_14.setObjectName(u"label_14")
        sizePolicy3.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy3)
        self.label_14.setFont(font5)
        self.label_14.setStyleSheet(u"color: #000036;")
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_15.addWidget(self.label_14, 0, 3, 1, 1)


        self.gridLayout_19.addWidget(self.groupBox_13, 2, 0, 1, 2)

        self.groupBox_11 = QGroupBox(self.page_calib)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.groupBox_11.setFont(font2)
        self.groupBox_11.setStyleSheet(u"QGroupBox {\n"
"	border: none;\n"
"	padding: 20px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"	color: #000036;\n"
"}")
        self.gridLayout_6 = QGridLayout(self.groupBox_11)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.lineEdit_size_square = QLineEdit(self.groupBox_11)
        self.lineEdit_size_square.setObjectName(u"lineEdit_size_square")

        self.gridLayout_6.addWidget(self.lineEdit_size_square, 2, 1, 1, 1)

        self.label_25 = QLabel(self.groupBox_11)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font5)
        self.label_25.setStyleSheet(u"color: #000036;")

        self.gridLayout_6.addWidget(self.label_25, 2, 0, 1, 1)

        self.lineEdit_columns = QLineEdit(self.groupBox_11)
        self.lineEdit_columns.setObjectName(u"lineEdit_columns")

        self.gridLayout_6.addWidget(self.lineEdit_columns, 1, 1, 1, 1)

        self.label_26 = QLabel(self.groupBox_11)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font5)
        self.label_26.setStyleSheet(u"color: #000036;")

        self.gridLayout_6.addWidget(self.label_26, 3, 0, 1, 1)

        self.label_23 = QLabel(self.groupBox_11)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font5)
        self.label_23.setStyleSheet(u"color: #000036;")

        self.gridLayout_6.addWidget(self.label_23, 0, 0, 1, 1)

        self.lineEdit_size_marker = QLineEdit(self.groupBox_11)
        self.lineEdit_size_marker.setObjectName(u"lineEdit_size_marker")

        self.gridLayout_6.addWidget(self.lineEdit_size_marker, 3, 1, 1, 1)

        self.label_24 = QLabel(self.groupBox_11)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font5)
        self.label_24.setStyleSheet(u"color: #000036;")

        self.gridLayout_6.addWidget(self.label_24, 1, 0, 1, 1)

        self.lineEdit_rows = QLineEdit(self.groupBox_11)
        self.lineEdit_rows.setObjectName(u"lineEdit_rows")
        self.lineEdit_rows.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)
        self.lineEdit_rows.setClearButtonEnabled(False)

        self.gridLayout_6.addWidget(self.lineEdit_rows, 0, 1, 1, 1)

        self.b_set_board_params = QPushButton(self.groupBox_11)
        self.b_set_board_params.setObjectName(u"b_set_board_params")
        font7 = QFont()
        font7.setPointSize(10)
        font7.setWeight(QFont.DemiBold)
        self.b_set_board_params.setFont(font7)
        self.b_set_board_params.setStyleSheet(u"QPushButton {\n"
"    background-color: #3e37ff;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    padding: 5px; /* Uprav\u00ed vnit\u0159n\u00ed prostor tla\u010d\u00edtka */\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #000036;\n"
"}")

        self.gridLayout_6.addWidget(self.b_set_board_params, 4, 1, 1, 1)


        self.gridLayout_19.addWidget(self.groupBox_11, 4, 0, 2, 2)

        self.groupBox_12 = QGroupBox(self.page_calib)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.groupBox_12.setStyleSheet(u"QGroupBox {\n"
"	border: none;\n"
"	padding: 0px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"	color: #000036;\n"
"}")
        self.gridLayout_14 = QGridLayout(self.groupBox_12)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.label_5 = QLabel(self.groupBox_12)
        self.label_5.setObjectName(u"label_5")
        sizePolicy3.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy3)
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"color: #000036;")

        self.gridLayout_14.addWidget(self.label_5, 1, 0, 1, 1)

        self.slider_config = QSlider(self.groupBox_12)
        self.slider_config.setObjectName(u"slider_config")
        sizePolicy6.setHeightForWidth(self.slider_config.sizePolicy().hasHeightForWidth())
        self.slider_config.setSizePolicy(sizePolicy6)
        self.slider_config.setMinimumSize(QSize(100, 0))
        self.slider_config.setStyleSheet(u"QSlider::groove:horizontal {\n"
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
"}\n"
"/*\n"
"QSlider::sub-page:horizontal {\n"
"    background: #0078D7;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: #bbb;\n"
"    border-radius: 4px;\n"
"}\n"
"*/")
        self.slider_config.setMaximum(1)
        self.slider_config.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_14.addWidget(self.slider_config, 1, 2, 1, 1)

        self.label_13 = QLabel(self.groupBox_12)
        self.label_13.setObjectName(u"label_13")
        sizePolicy3.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy3)
        self.label_13.setFont(font5)
        self.label_13.setStyleSheet(u"color: #000036;")
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_14.addWidget(self.label_13, 0, 1, 3, 1)

        self.label_18 = QLabel(self.groupBox_12)
        self.label_18.setObjectName(u"label_18")
        sizePolicy3.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy3)
        self.label_18.setFont(font5)
        self.label_18.setStyleSheet(u"color: #000036;")
        self.label_18.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_14.addWidget(self.label_18, 1, 3, 1, 1)


        self.gridLayout_19.addWidget(self.groupBox_12, 1, 0, 1, 2)

        self.label_17 = QLabel(self.page_calib)
        self.label_17.setObjectName(u"label_17")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy7)
        self.label_17.setMinimumSize(QSize(0, 50))
        font8 = QFont()
        font8.setPointSize(13)
        font8.setWeight(QFont.DemiBold)
        self.label_17.setFont(font8)
        self.label_17.setStyleSheet(u"color: #000036;")
        self.label_17.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_17.setWordWrap(True)

        self.gridLayout_19.addWidget(self.label_17, 0, 0, 1, 2)

        self.groupBox_16 = QGroupBox(self.page_calib)
        self.groupBox_16.setObjectName(u"groupBox_16")
        self.groupBox_16.setStyleSheet(u"QGroupBox {\n"
"	border: none;\n"
"	padding: 0px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"	color: #000036;\n"
"}")
        self.gridLayout_17 = QGridLayout(self.groupBox_16)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.label_22 = QLabel(self.groupBox_16)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font5)
        self.label_22.setStyleSheet(u"color: #000036;")
        self.label_22.setWordWrap(True)

        self.gridLayout_17.addWidget(self.label_22, 0, 0, 1, 1)

        self.b_initial_adjustment = QPushButton(self.groupBox_16)
        self.b_initial_adjustment.setObjectName(u"b_initial_adjustment")
        self.b_initial_adjustment.setFont(font5)
        self.b_initial_adjustment.setStyleSheet(u"QPushButton {\n"
"    background-color: #3e37ff;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    padding: 10px; /* Uprav\u00ed vnit\u0159n\u00ed prostor tla\u010d\u00edtka */\n"
"	margin: 0px 20px 0px 0px;\n"
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

        self.gridLayout_17.addWidget(self.b_initial_adjustment, 0, 1, 1, 1)


        self.gridLayout_19.addWidget(self.groupBox_16, 6, 0, 1, 2)

        self.b_start_calib = QPushButton(self.page_calib)
        self.b_start_calib.setObjectName(u"b_start_calib")
        font9 = QFont()
        font9.setPointSize(14)
        font9.setBold(True)
        self.b_start_calib.setFont(font9)
        self.b_start_calib.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_19.addWidget(self.b_start_calib, 8, 0, 1, 2)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_19.addItem(self.verticalSpacer_4, 7, 0, 1, 2)

        self.stackedWidget.addWidget(self.page_calib)
        self.page_test = QWidget()
        self.page_test.setObjectName(u"page_test")
        self.gridLayout_13 = QGridLayout(self.page_test)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(-1, -1, 6, -1)
        self.groupBox_10 = QGroupBox(self.page_test)
        self.groupBox_10.setObjectName(u"groupBox_10")
        sizePolicy4.setHeightForWidth(self.groupBox_10.sizePolicy().hasHeightForWidth())
        self.groupBox_10.setSizePolicy(sizePolicy4)
        self.groupBox_10.setFont(font1)
        self.groupBox_10.setStyleSheet(u"#groupBox_10 {\n"
"	border: none;\n"
"	padding: 30px 0px 0px 0px;\n"
"	margin: 0px 9px 0px 9px;\n"
"	background-color: #3e37ff;\n"
"	border-radius: 10px;\n"
"}\n"
"#groupBox_10::title {\n"
"	color: white;  /*zkou\u0161ka*/\n"
"}")
        self.groupBox_10.setFlat(False)
        self.gridLayout_20 = QGridLayout(self.groupBox_10)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.groupBox_17 = QGroupBox(self.groupBox_10)
        self.groupBox_17.setObjectName(u"groupBox_17")
        sizePolicy4.setHeightForWidth(self.groupBox_17.sizePolicy().hasHeightForWidth())
        self.groupBox_17.setSizePolicy(sizePolicy4)
        self.groupBox_17.setMinimumSize(QSize(368, 0))
        self.groupBox_17.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox_17.setStyleSheet(u"#groupBox_17 {\n"
"	border: none;\n"
"	padding: 0px 0px 0px 0px;\n"
"	margin: 0px;\n"
"	background-color: #000036;\n"
"	border-radius: 10px;\n"
"}\n"
"")
        self.gridLayout_21 = QGridLayout(self.groupBox_17)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.groupBox_19 = QGroupBox(self.groupBox_17)
        self.groupBox_19.setObjectName(u"groupBox_19")
        sizePolicy4.setHeightForWidth(self.groupBox_19.sizePolicy().hasHeightForWidth())
        self.groupBox_19.setSizePolicy(sizePolicy4)
        self.groupBox_19.setMinimumSize(QSize(100, 0))
        self.groupBox_19.setMaximumSize(QSize(300, 16777215))
        palette36 = QPalette()
        self.groupBox_19.setPalette(palette36)
        self.groupBox_19.setFont(font2)
        self.groupBox_19.setStyleSheet(u"#groupBox_19 {\n"
"	border: none;\n"
"	padding: 0px;\n"
"	margin: 0px;\n"
"}\n"
"#groupBox_19::title {\n"
"	color: white;\n"
"}")
        self.gridLayout_23 = QGridLayout(self.groupBox_19)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.cm_0_2_t = QLabel(self.groupBox_19)
        self.cm_0_2_t.setObjectName(u"cm_0_2_t")
        self.cm_0_2_t.setMinimumSize(QSize(60, 0))
        palette37 = QPalette()
        palette37.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette37.setBrush(QPalette.Active, QPalette.Text, brush)
        palette37.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette37.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette37.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette37.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette37.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette37.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette37.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette37.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette37.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette37.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        self.cm_0_2_t.setPalette(palette37)
        self.cm_0_2_t.setStyleSheet(u"color: white")
        self.cm_0_2_t.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.cm_0_2_t.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.gridLayout_23.addWidget(self.cm_0_2_t, 1, 3, 1, 1)

        self.cm_0_0_t = QLabel(self.groupBox_19)
        self.cm_0_0_t.setObjectName(u"cm_0_0_t")
        self.cm_0_0_t.setMinimumSize(QSize(60, 0))
        palette38 = QPalette()
        palette38.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette38.setBrush(QPalette.Active, QPalette.Text, brush)
        palette38.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette38.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette38.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette38.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette38.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette38.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette38.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette38.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette38.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette38.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        self.cm_0_0_t.setPalette(palette38)
        self.cm_0_0_t.setStyleSheet(u"color: white")
        self.cm_0_0_t.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.cm_0_0_t.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.gridLayout_23.addWidget(self.cm_0_0_t, 1, 1, 1, 1)

        self.cm_1_1_t = QLabel(self.groupBox_19)
        self.cm_1_1_t.setObjectName(u"cm_1_1_t")
        self.cm_1_1_t.setMinimumSize(QSize(60, 0))
        palette39 = QPalette()
        palette39.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette39.setBrush(QPalette.Active, QPalette.Text, brush)
        palette39.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette39.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette39.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette39.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette39.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette39.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette39.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette39.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette39.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette39.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        self.cm_1_1_t.setPalette(palette39)
        self.cm_1_1_t.setStyleSheet(u"color: white")
        self.cm_1_1_t.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.cm_1_1_t.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.gridLayout_23.addWidget(self.cm_1_1_t, 2, 2, 1, 1)

        self.cm_0_1_t = QLabel(self.groupBox_19)
        self.cm_0_1_t.setObjectName(u"cm_0_1_t")
        self.cm_0_1_t.setMinimumSize(QSize(60, 0))
        palette40 = QPalette()
        palette40.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette40.setBrush(QPalette.Active, QPalette.Text, brush)
        palette40.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette40.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette40.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette40.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette40.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette40.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette40.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette40.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette40.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette40.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        self.cm_0_1_t.setPalette(palette40)
        self.cm_0_1_t.setStyleSheet(u"color: white")
        self.cm_0_1_t.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.cm_0_1_t.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.gridLayout_23.addWidget(self.cm_0_1_t, 1, 2, 1, 1)

        self.cm_2_0_t = QLabel(self.groupBox_19)
        self.cm_2_0_t.setObjectName(u"cm_2_0_t")
        self.cm_2_0_t.setMinimumSize(QSize(60, 0))
        palette41 = QPalette()
        palette41.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette41.setBrush(QPalette.Active, QPalette.Text, brush)
        palette41.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette41.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette41.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette41.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette41.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette41.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette41.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette41.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette41.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette41.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        self.cm_2_0_t.setPalette(palette41)
        self.cm_2_0_t.setStyleSheet(u"color: white")
        self.cm_2_0_t.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.cm_2_0_t.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.gridLayout_23.addWidget(self.cm_2_0_t, 3, 1, 1, 1)

        self.cm_2_1_t = QLabel(self.groupBox_19)
        self.cm_2_1_t.setObjectName(u"cm_2_1_t")
        self.cm_2_1_t.setMinimumSize(QSize(60, 0))
        palette42 = QPalette()
        palette42.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette42.setBrush(QPalette.Active, QPalette.Text, brush)
        palette42.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette42.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette42.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette42.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette42.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette42.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette42.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette42.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette42.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette42.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        self.cm_2_1_t.setPalette(palette42)
        self.cm_2_1_t.setStyleSheet(u"color: white")
        self.cm_2_1_t.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.cm_2_1_t.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.gridLayout_23.addWidget(self.cm_2_1_t, 3, 2, 1, 1)

        self.cm_1_0_t = QLabel(self.groupBox_19)
        self.cm_1_0_t.setObjectName(u"cm_1_0_t")
        self.cm_1_0_t.setMinimumSize(QSize(60, 0))
        palette43 = QPalette()
        palette43.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette43.setBrush(QPalette.Active, QPalette.Text, brush)
        palette43.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette43.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette43.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette43.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette43.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette43.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette43.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette43.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette43.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette43.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        self.cm_1_0_t.setPalette(palette43)
        self.cm_1_0_t.setStyleSheet(u"color: white")
        self.cm_1_0_t.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.cm_1_0_t.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.gridLayout_23.addWidget(self.cm_1_0_t, 2, 1, 1, 1)

        self.cm_1_2_t = QLabel(self.groupBox_19)
        self.cm_1_2_t.setObjectName(u"cm_1_2_t")
        self.cm_1_2_t.setMinimumSize(QSize(60, 0))
        palette44 = QPalette()
        palette44.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette44.setBrush(QPalette.Active, QPalette.Text, brush)
        palette44.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette44.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette44.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette44.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette44.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette44.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette44.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette44.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette44.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette44.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        self.cm_1_2_t.setPalette(palette44)
        self.cm_1_2_t.setStyleSheet(u"color: white")
        self.cm_1_2_t.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.cm_1_2_t.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.gridLayout_23.addWidget(self.cm_1_2_t, 2, 3, 1, 1)

        self.cm_2_2_t = QLabel(self.groupBox_19)
        self.cm_2_2_t.setObjectName(u"cm_2_2_t")
        self.cm_2_2_t.setMinimumSize(QSize(60, 0))
        palette45 = QPalette()
        palette45.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette45.setBrush(QPalette.Active, QPalette.Text, brush)
        palette45.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette45.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette45.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette45.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette45.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette45.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette45.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette45.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette45.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette45.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        self.cm_2_2_t.setPalette(palette45)
        self.cm_2_2_t.setStyleSheet(u"color: white")
        self.cm_2_2_t.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.cm_2_2_t.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.gridLayout_23.addWidget(self.cm_2_2_t, 3, 3, 1, 1)

        self.label_81 = QLabel(self.groupBox_19)
        self.label_81.setObjectName(u"label_81")
        palette46 = QPalette()
        palette46.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette46.setBrush(QPalette.Active, QPalette.Text, brush)
        palette46.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette46.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette46.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette46.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette46.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette46.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette46.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette46.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette46.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette46.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        self.label_81.setPalette(palette46)
        self.label_81.setFont(font4)
        self.label_81.setStyleSheet(u"color: white")
        self.label_81.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing)

        self.gridLayout_23.addWidget(self.label_81, 0, 0, 4, 1)

        self.label_82 = QLabel(self.groupBox_19)
        self.label_82.setObjectName(u"label_82")
        self.label_82.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.gridLayout_23.addWidget(self.label_82, 0, 1, 1, 3)

        self.label_83 = QLabel(self.groupBox_19)
        self.label_83.setObjectName(u"label_83")
        palette47 = QPalette()
        palette47.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette47.setBrush(QPalette.Active, QPalette.Text, brush)
        palette47.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette47.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette47.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette47.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette47.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette47.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette47.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette47.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette47.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette47.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        self.label_83.setPalette(palette47)
        self.label_83.setFont(font4)
        self.label_83.setStyleSheet(u"color: white")
        self.label_83.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.gridLayout_23.addWidget(self.label_83, 0, 4, 4, 1)


        self.gridLayout_21.addWidget(self.groupBox_19, 0, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_21.addItem(self.verticalSpacer_5, 2, 0, 1, 1)

        self.groupBox_18 = QGroupBox(self.groupBox_17)
        self.groupBox_18.setObjectName(u"groupBox_18")
        palette48 = QPalette()
        self.groupBox_18.setPalette(palette48)
        self.groupBox_18.setFont(font2)
        self.groupBox_18.setStyleSheet(u"#groupBox_18 {\n"
"	border: none;\n"
"	padding: 15px 0px 0px 0px;\n"
"	margin: 0px;\n"
"}\n"
"#groupBox_18::title {\n"
"	color: white;\n"
"}")
        self.gridLayout_22 = QGridLayout(self.groupBox_18)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.dist_coeff_t = QLabel(self.groupBox_18)
        self.dist_coeff_t.setObjectName(u"dist_coeff_t")
        sizePolicy4.setHeightForWidth(self.dist_coeff_t.sizePolicy().hasHeightForWidth())
        self.dist_coeff_t.setSizePolicy(sizePolicy4)
        palette49 = QPalette()
        palette49.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette49.setBrush(QPalette.Active, QPalette.Text, brush)
        palette49.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette49.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette49.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette49.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette49.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette49.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette49.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette49.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette49.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette49.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        self.dist_coeff_t.setPalette(palette49)
        self.dist_coeff_t.setStyleSheet(u"color: white")
        self.dist_coeff_t.setWordWrap(True)

        self.gridLayout_22.addWidget(self.dist_coeff_t, 0, 0, 1, 1)


        self.gridLayout_21.addWidget(self.groupBox_18, 1, 0, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(0, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_21.addItem(self.horizontalSpacer_7, 0, 1, 3, 1)


        self.gridLayout_20.addWidget(self.groupBox_17, 0, 0, 1, 1)

        self.groupBox_20 = QGroupBox(self.groupBox_10)
        self.groupBox_20.setObjectName(u"groupBox_20")
        sizePolicy4.setHeightForWidth(self.groupBox_20.sizePolicy().hasHeightForWidth())
        self.groupBox_20.setSizePolicy(sizePolicy4)
        self.groupBox_20.setStyleSheet(u"#groupBox_20 {\n"
"	border: none;\n"
"	padding: 0px 0px 0px 0px;\n"
"	margin: 0px;\n"
"	background-color: #000036;\n"
"	border-radius: 10px;\n"
"}")
        self.gridLayout_24 = QGridLayout(self.groupBox_20)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.groupBox_22 = QGroupBox(self.groupBox_20)
        self.groupBox_22.setObjectName(u"groupBox_22")
        palette50 = QPalette()
        self.groupBox_22.setPalette(palette50)
        self.groupBox_22.setFont(font2)
        self.groupBox_22.setStyleSheet(u"#groupBox_22 {\n"
"	border: none;\n"
"	padding: 15px 0px 0px 0px;\n"
"	margin: 0px;\n"
"}\n"
"#groupBox_22::title {\n"
"	color: white;\n"
"}")
        self.gridLayout_26 = QGridLayout(self.groupBox_22)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.pose_vector_t = QLabel(self.groupBox_22)
        self.pose_vector_t.setObjectName(u"pose_vector_t")
        sizePolicy4.setHeightForWidth(self.pose_vector_t.sizePolicy().hasHeightForWidth())
        self.pose_vector_t.setSizePolicy(sizePolicy4)
        self.pose_vector_t.setMinimumSize(QSize(0, 32))
        palette51 = QPalette()
        palette51.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette51.setBrush(QPalette.Active, QPalette.Text, brush)
        palette51.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette51.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette51.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette51.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette51.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette51.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette51.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette51.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette51.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette51.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        self.pose_vector_t.setPalette(palette51)
        self.pose_vector_t.setStyleSheet(u"color: white")
        self.pose_vector_t.setWordWrap(True)

        self.gridLayout_26.addWidget(self.pose_vector_t, 0, 0, 1, 1)


        self.gridLayout_24.addWidget(self.groupBox_22, 1, 0, 1, 1)

        self.groupBox_21 = QGroupBox(self.groupBox_20)
        self.groupBox_21.setObjectName(u"groupBox_21")
        sizePolicy4.setHeightForWidth(self.groupBox_21.sizePolicy().hasHeightForWidth())
        self.groupBox_21.setSizePolicy(sizePolicy4)
        self.groupBox_21.setMinimumSize(QSize(310, 0))
        self.groupBox_21.setMaximumSize(QSize(370, 16777215))
        self.groupBox_21.setFont(font2)
        self.groupBox_21.setStyleSheet(u"#groupBox_21 {\n"
"	border: none;\n"
"	padding: 0px;\n"
"	margin: 0px;\n"
"}\n"
"#groupBox_21::title {\n"
"	color: white;\n"
"}")
        self.gridLayout_25 = QGridLayout(self.groupBox_21)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.label_84 = QLabel(self.groupBox_21)
        self.label_84.setObjectName(u"label_84")
        palette52 = QPalette()
        palette52.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette52.setBrush(QPalette.Active, QPalette.Text, brush)
        palette52.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette52.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette52.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette52.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette52.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette52.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette52.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette52.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette52.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette52.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        self.label_84.setPalette(palette52)
        self.label_84.setFont(font3)
        self.label_84.setStyleSheet(u"color: white")
        self.label_84.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing)

        self.gridLayout_25.addWidget(self.label_84, 0, 0, 5, 1)

        self.tfm_0_3_t = QLabel(self.groupBox_21)
        self.tfm_0_3_t.setObjectName(u"tfm_0_3_t")
        self.tfm_0_3_t.setMinimumSize(QSize(60, 0))
        palette53 = QPalette()
        palette53.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette53.setBrush(QPalette.Active, QPalette.Text, brush)
        palette53.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette53.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette53.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette53.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette53.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette53.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette53.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette53.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette53.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette53.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        self.tfm_0_3_t.setPalette(palette53)
        self.tfm_0_3_t.setStyleSheet(u"color: white")
        self.tfm_0_3_t.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.tfm_0_3_t.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.gridLayout_25.addWidget(self.tfm_0_3_t, 1, 4, 1, 1)

        self.tfm_0_1_t = QLabel(self.groupBox_21)
        self.tfm_0_1_t.setObjectName(u"tfm_0_1_t")
        self.tfm_0_1_t.setMinimumSize(QSize(60, 0))
        palette54 = QPalette()
        palette54.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette54.setBrush(QPalette.Active, QPalette.Text, brush)
        palette54.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette54.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette54.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette54.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette54.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette54.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette54.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette54.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette54.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette54.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        self.tfm_0_1_t.setPalette(palette54)
        self.tfm_0_1_t.setStyleSheet(u"color: white")
        self.tfm_0_1_t.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.tfm_0_1_t.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.gridLayout_25.addWidget(self.tfm_0_1_t, 1, 2, 1, 1)

        self.tfm_2_3_t = QLabel(self.groupBox_21)
        self.tfm_2_3_t.setObjectName(u"tfm_2_3_t")
        self.tfm_2_3_t.setMinimumSize(QSize(60, 0))
        palette55 = QPalette()
        palette55.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette55.setBrush(QPalette.Active, QPalette.Text, brush)
        palette55.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette55.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette55.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette55.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette55.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette55.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette55.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette55.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette55.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette55.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        self.tfm_2_3_t.setPalette(palette55)
        self.tfm_2_3_t.setStyleSheet(u"color: white")
        self.tfm_2_3_t.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.tfm_2_3_t.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.gridLayout_25.addWidget(self.tfm_2_3_t, 3, 4, 1, 1)

        self.tfm_1_1_t = QLabel(self.groupBox_21)
        self.tfm_1_1_t.setObjectName(u"tfm_1_1_t")
        self.tfm_1_1_t.setMinimumSize(QSize(60, 0))
        palette56 = QPalette()
        palette56.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette56.setBrush(QPalette.Active, QPalette.Text, brush)
        palette56.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette56.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette56.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette56.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette56.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette56.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette56.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette56.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette56.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette56.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        self.tfm_1_1_t.setPalette(palette56)
        self.tfm_1_1_t.setStyleSheet(u"color: white")
        self.tfm_1_1_t.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.tfm_1_1_t.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.gridLayout_25.addWidget(self.tfm_1_1_t, 2, 2, 1, 1)

        self.tfm_3_3_t = QLabel(self.groupBox_21)
        self.tfm_3_3_t.setObjectName(u"tfm_3_3_t")
        self.tfm_3_3_t.setMinimumSize(QSize(60, 0))
        palette57 = QPalette()
        palette57.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette57.setBrush(QPalette.Active, QPalette.Text, brush)
        palette57.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette57.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette57.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette57.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette57.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette57.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette57.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette57.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette57.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette57.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        self.tfm_3_3_t.setPalette(palette57)
        self.tfm_3_3_t.setStyleSheet(u"color: white")
        self.tfm_3_3_t.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.tfm_3_3_t.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.gridLayout_25.addWidget(self.tfm_3_3_t, 4, 4, 1, 1)

        self.label_87 = QLabel(self.groupBox_21)
        self.label_87.setObjectName(u"label_87")
        palette58 = QPalette()
        palette58.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette58.setBrush(QPalette.Active, QPalette.Text, brush)
        palette58.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette58.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette58.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette58.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette58.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette58.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette58.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette58.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette58.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette58.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        self.label_87.setPalette(palette58)
        self.label_87.setFont(font3)
        self.label_87.setStyleSheet(u"color: white")
        self.label_87.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.gridLayout_25.addWidget(self.label_87, 0, 5, 5, 1)

        self.tfm_2_2_t = QLabel(self.groupBox_21)
        self.tfm_2_2_t.setObjectName(u"tfm_2_2_t")
        self.tfm_2_2_t.setMinimumSize(QSize(60, 0))
        palette59 = QPalette()
        palette59.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette59.setBrush(QPalette.Active, QPalette.Text, brush)
        palette59.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette59.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette59.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette59.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette59.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette59.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette59.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette59.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette59.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette59.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        self.tfm_2_2_t.setPalette(palette59)
        self.tfm_2_2_t.setStyleSheet(u"color: white")
        self.tfm_2_2_t.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.tfm_2_2_t.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.gridLayout_25.addWidget(self.tfm_2_2_t, 3, 3, 1, 1)

        self.label_93 = QLabel(self.groupBox_21)
        self.label_93.setObjectName(u"label_93")

        self.gridLayout_25.addWidget(self.label_93, 0, 1, 1, 4)

        self.tfm_1_3_t = QLabel(self.groupBox_21)
        self.tfm_1_3_t.setObjectName(u"tfm_1_3_t")
        self.tfm_1_3_t.setMinimumSize(QSize(60, 0))
        palette60 = QPalette()
        palette60.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette60.setBrush(QPalette.Active, QPalette.Text, brush)
        palette60.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette60.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette60.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette60.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette60.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette60.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette60.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette60.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette60.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette60.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        self.tfm_1_3_t.setPalette(palette60)
        self.tfm_1_3_t.setStyleSheet(u"color: white")
        self.tfm_1_3_t.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.tfm_1_3_t.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.gridLayout_25.addWidget(self.tfm_1_3_t, 2, 4, 1, 1)

        self.tfm_2_0_t = QLabel(self.groupBox_21)
        self.tfm_2_0_t.setObjectName(u"tfm_2_0_t")
        self.tfm_2_0_t.setMinimumSize(QSize(60, 0))
        palette61 = QPalette()
        palette61.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette61.setBrush(QPalette.Active, QPalette.Text, brush)
        palette61.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette61.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette61.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette61.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette61.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette61.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette61.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette61.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette61.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette61.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        self.tfm_2_0_t.setPalette(palette61)
        self.tfm_2_0_t.setStyleSheet(u"color: white")
        self.tfm_2_0_t.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.tfm_2_0_t.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.gridLayout_25.addWidget(self.tfm_2_0_t, 3, 1, 1, 1)

        self.tfm_0_2_t = QLabel(self.groupBox_21)
        self.tfm_0_2_t.setObjectName(u"tfm_0_2_t")
        self.tfm_0_2_t.setMinimumSize(QSize(60, 0))
        palette62 = QPalette()
        palette62.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette62.setBrush(QPalette.Active, QPalette.Text, brush)
        palette62.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette62.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette62.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette62.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette62.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette62.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette62.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette62.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette62.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette62.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        self.tfm_0_2_t.setPalette(palette62)
        self.tfm_0_2_t.setStyleSheet(u"color: white")
        self.tfm_0_2_t.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.tfm_0_2_t.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.gridLayout_25.addWidget(self.tfm_0_2_t, 1, 3, 1, 1)

        self.tfm_0_0_t = QLabel(self.groupBox_21)
        self.tfm_0_0_t.setObjectName(u"tfm_0_0_t")
        self.tfm_0_0_t.setMinimumSize(QSize(60, 0))
        palette63 = QPalette()
        palette63.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette63.setBrush(QPalette.Active, QPalette.Text, brush)
        palette63.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette63.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette63.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette63.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette63.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette63.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette63.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette63.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette63.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette63.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        self.tfm_0_0_t.setPalette(palette63)
        self.tfm_0_0_t.setStyleSheet(u"color: white")
        self.tfm_0_0_t.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.tfm_0_0_t.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.gridLayout_25.addWidget(self.tfm_0_0_t, 1, 1, 1, 1)

        self.tfm_2_1_t = QLabel(self.groupBox_21)
        self.tfm_2_1_t.setObjectName(u"tfm_2_1_t")
        self.tfm_2_1_t.setMinimumSize(QSize(60, 0))
        palette64 = QPalette()
        palette64.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette64.setBrush(QPalette.Active, QPalette.Text, brush)
        palette64.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette64.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette64.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette64.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette64.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette64.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette64.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette64.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette64.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette64.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        self.tfm_2_1_t.setPalette(palette64)
        self.tfm_2_1_t.setStyleSheet(u"color: white")
        self.tfm_2_1_t.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.tfm_2_1_t.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.gridLayout_25.addWidget(self.tfm_2_1_t, 3, 2, 1, 1)

        self.tfm_1_2_t = QLabel(self.groupBox_21)
        self.tfm_1_2_t.setObjectName(u"tfm_1_2_t")
        self.tfm_1_2_t.setMinimumSize(QSize(60, 0))
        palette65 = QPalette()
        palette65.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette65.setBrush(QPalette.Active, QPalette.Text, brush)
        palette65.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette65.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette65.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette65.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette65.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette65.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette65.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette65.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette65.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette65.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        self.tfm_1_2_t.setPalette(palette65)
        self.tfm_1_2_t.setStyleSheet(u"color: white")
        self.tfm_1_2_t.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.tfm_1_2_t.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.gridLayout_25.addWidget(self.tfm_1_2_t, 2, 3, 1, 1)

        self.tfm_3_0_t = QLabel(self.groupBox_21)
        self.tfm_3_0_t.setObjectName(u"tfm_3_0_t")
        self.tfm_3_0_t.setMinimumSize(QSize(60, 0))
        palette66 = QPalette()
        palette66.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette66.setBrush(QPalette.Active, QPalette.Text, brush)
        palette66.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette66.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette66.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette66.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette66.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette66.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette66.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette66.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette66.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette66.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        self.tfm_3_0_t.setPalette(palette66)
        self.tfm_3_0_t.setStyleSheet(u"color: white")
        self.tfm_3_0_t.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.tfm_3_0_t.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.gridLayout_25.addWidget(self.tfm_3_0_t, 4, 1, 1, 1)

        self.tfm_3_2_t = QLabel(self.groupBox_21)
        self.tfm_3_2_t.setObjectName(u"tfm_3_2_t")
        self.tfm_3_2_t.setMinimumSize(QSize(60, 0))
        palette67 = QPalette()
        palette67.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette67.setBrush(QPalette.Active, QPalette.Text, brush)
        palette67.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette67.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette67.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette67.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette67.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette67.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette67.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette67.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette67.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette67.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        self.tfm_3_2_t.setPalette(palette67)
        self.tfm_3_2_t.setStyleSheet(u"color: white")
        self.tfm_3_2_t.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.tfm_3_2_t.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.gridLayout_25.addWidget(self.tfm_3_2_t, 4, 3, 1, 1)

        self.tfm_3_1_t = QLabel(self.groupBox_21)
        self.tfm_3_1_t.setObjectName(u"tfm_3_1_t")
        self.tfm_3_1_t.setMinimumSize(QSize(60, 0))
        palette68 = QPalette()
        palette68.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette68.setBrush(QPalette.Active, QPalette.Text, brush)
        palette68.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette68.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette68.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette68.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette68.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette68.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette68.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette68.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette68.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette68.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        self.tfm_3_1_t.setPalette(palette68)
        self.tfm_3_1_t.setStyleSheet(u"color: white")
        self.tfm_3_1_t.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.tfm_3_1_t.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.gridLayout_25.addWidget(self.tfm_3_1_t, 4, 2, 1, 1)

        self.tfm_1_0_t = QLabel(self.groupBox_21)
        self.tfm_1_0_t.setObjectName(u"tfm_1_0_t")
        self.tfm_1_0_t.setMinimumSize(QSize(60, 0))
        palette69 = QPalette()
        palette69.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette69.setBrush(QPalette.Active, QPalette.Text, brush)
        palette69.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette69.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette69.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette69.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette69.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette69.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette69.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette69.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette69.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette69.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        self.tfm_1_0_t.setPalette(palette69)
        self.tfm_1_0_t.setStyleSheet(u"color: white")
        self.tfm_1_0_t.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.tfm_1_0_t.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.gridLayout_25.addWidget(self.tfm_1_0_t, 2, 1, 1, 1)


        self.gridLayout_24.addWidget(self.groupBox_21, 0, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(0, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_24.addItem(self.horizontalSpacer_3, 0, 1, 2, 1)


        self.gridLayout_20.addWidget(self.groupBox_20, 0, 1, 1, 1)


        self.gridLayout_13.addWidget(self.groupBox_10, 5, 0, 1, 5)

        self.b_test_1 = QToolButton(self.page_test)
        self.b_test_1.setObjectName(u"b_test_1")
        sizePolicy4.setHeightForWidth(self.b_test_1.sizePolicy().hasHeightForWidth())
        self.b_test_1.setSizePolicy(sizePolicy4)
        self.b_test_1.setMaximumSize(QSize(300, 16777215))
        self.b_test_1.setFont(font5)
        self.b_test_1.setToolTipDuration(-1)
        self.b_test_1.setStyleSheet(u"QToolButton {\n"
"	background-color: #3e37ff;\n"
"	border: none;\n"
"    border-radius: 10px;\n"
"    padding: 10px; \n"
"	margin: 0px 9px 0px 9px;\n"
"	color: white;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"	background-color: #000036;\n"
"}\n"
"\n"
"QToolButton:disabled {\n"
"    background-color: #808080; /* \u0160ed\u00e1 barva pro deaktivovan\u00e9 tla\u010d\u00edtko */\n"
"    color: #c0c0c0; /* Sv\u011btlej\u0161\u00ed \u0161ed\u00e1 barva textu */\n"
"    border: none;\n"
"}")
        self.b_test_1.setText(u"Test 1\n"
"Pick and place")
        self.b_test_1.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)

        self.gridLayout_13.addWidget(self.b_test_1, 4, 0, 1, 1)

        self.b_test_2 = QToolButton(self.page_test)
        self.b_test_2.setObjectName(u"b_test_2")
        sizePolicy4.setHeightForWidth(self.b_test_2.sizePolicy().hasHeightForWidth())
        self.b_test_2.setSizePolicy(sizePolicy4)
        self.b_test_2.setFont(font5)
        self.b_test_2.setStyleSheet(u"QToolButton {\n"
"	background-color: #3e37ff;\n"
"	border: none;\n"
"    border-radius: 10px;\n"
"    padding: 10px; \n"
"	margin: 0px 9px 0px 9px;\n"
"	color: white;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"	background-color: #000036;\n"
"}\n"
"\n"
"QToolButton:disabled {\n"
"    background-color: #808080; /* \u0160ed\u00e1 barva pro deaktivovan\u00e9 tla\u010d\u00edtko */\n"
"    color: #c0c0c0; /* Sv\u011btlej\u0161\u00ed \u0161ed\u00e1 barva textu */\n"
"    border: none;\n"
"}")

        self.gridLayout_13.addWidget(self.b_test_2, 4, 2, 1, 1)

        self.label_3 = QLabel(self.page_test)
        self.label_3.setObjectName(u"label_3")
        sizePolicy3.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy3)
        font10 = QFont()
        font10.setFamilies([u"Segoe UI"])
        font10.setPointSize(11)
        font10.setBold(True)
        self.label_3.setFont(font10)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_13.addWidget(self.label_3, 0, 0, 1, 5)

        self.groupBox_29 = QGroupBox(self.page_test)
        self.groupBox_29.setObjectName(u"groupBox_29")
        self.groupBox_29.setStyleSheet(u"QGroupBox {\n"
"	border: none;\n"
"	padding: 0px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"	color: #000036;\n"
"}")
        self.gridLayout_34 = QGridLayout(self.groupBox_29)
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.label_4 = QLabel(self.groupBox_29)
        self.label_4.setObjectName(u"label_4")
        sizePolicy4.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy4)
        self.label_4.setFont(font2)
        self.label_4.setStyleSheet(u"color: #000036;")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_34.addWidget(self.label_4, 0, 0, 1, 1)

        self.slider_config_test = QSlider(self.groupBox_29)
        self.slider_config_test.setObjectName(u"slider_config_test")
        sizePolicy4.setHeightForWidth(self.slider_config_test.sizePolicy().hasHeightForWidth())
        self.slider_config_test.setSizePolicy(sizePolicy4)
        self.slider_config_test.setStyleSheet(u"QSlider::groove:horizontal {\n"
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
"}\n"
"/*\n"
"QSlider::sub-page:horizontal {\n"
"    background: #0078D7;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: #bbb;\n"
"    border-radius: 4px;\n"
"}\n"
"*/")
        self.slider_config_test.setMaximum(1)
        self.slider_config_test.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_34.addWidget(self.slider_config_test, 0, 1, 1, 1)

        self.label_16 = QLabel(self.groupBox_29)
        self.label_16.setObjectName(u"label_16")
        sizePolicy4.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy4)
        self.label_16.setFont(font2)
        self.label_16.setStyleSheet(u"color: #000036;")
        self.label_16.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_34.addWidget(self.label_16, 0, 2, 1, 1)


        self.gridLayout_13.addWidget(self.groupBox_29, 1, 0, 1, 5)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_13.addItem(self.verticalSpacer_2, 3, 0, 1, 5)

        self.groupBox_28 = QGroupBox(self.page_test)
        self.groupBox_28.setObjectName(u"groupBox_28")
        self.groupBox_28.setStyleSheet(u"QGroupBox {\n"
"	border: none;\n"
"	padding: 0px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"	color: #000036;\n"
"}")
        self.gridLayout_33 = QGridLayout(self.groupBox_28)
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.label_31 = QLabel(self.groupBox_28)
        self.label_31.setObjectName(u"label_31")
        sizePolicy3.setHeightForWidth(self.label_31.sizePolicy().hasHeightForWidth())
        self.label_31.setSizePolicy(sizePolicy3)
        self.label_31.setFont(font2)
        self.label_31.setStyleSheet(u"color: #000036;")
        self.label_31.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_33.addWidget(self.label_31, 0, 0, 1, 1)

        self.label_32 = QLabel(self.groupBox_28)
        self.label_32.setObjectName(u"label_32")
        sizePolicy3.setHeightForWidth(self.label_32.sizePolicy().hasHeightForWidth())
        self.label_32.setSizePolicy(sizePolicy3)
        self.label_32.setFont(font5)
        self.label_32.setStyleSheet(u"color: #000036;")
        self.label_32.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_33.addWidget(self.label_32, 0, 1, 1, 1)

        self.slider_light_test = QSlider(self.groupBox_28)
        self.slider_light_test.setObjectName(u"slider_light_test")
        sizePolicy3.setHeightForWidth(self.slider_light_test.sizePolicy().hasHeightForWidth())
        self.slider_light_test.setSizePolicy(sizePolicy3)
        self.slider_light_test.setMinimumSize(QSize(100, 0))
        self.slider_light_test.setStyleSheet(u"QSlider::groove:horizontal {\n"
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
"}\n"
"/*\n"
"QSlider::sub-page:horizontal {\n"
"    background: #0078D7;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: #bbb;\n"
"    border-radius: 4px;\n"
"}\n"
"*/")
        self.slider_light_test.setMaximum(1)
        self.slider_light_test.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_33.addWidget(self.slider_light_test, 0, 2, 1, 1)

        self.label_33 = QLabel(self.groupBox_28)
        self.label_33.setObjectName(u"label_33")
        sizePolicy3.setHeightForWidth(self.label_33.sizePolicy().hasHeightForWidth())
        self.label_33.setSizePolicy(sizePolicy3)
        self.label_33.setFont(font5)
        self.label_33.setStyleSheet(u"color: #000036;")
        self.label_33.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_33.addWidget(self.label_33, 0, 3, 1, 1)


        self.gridLayout_13.addWidget(self.groupBox_28, 2, 0, 1, 5)

        self.b_test_3 = QToolButton(self.page_test)
        self.b_test_3.setObjectName(u"b_test_3")
        sizePolicy4.setHeightForWidth(self.b_test_3.sizePolicy().hasHeightForWidth())
        self.b_test_3.setSizePolicy(sizePolicy4)
        self.b_test_3.setMaximumSize(QSize(300, 16777215))
        self.b_test_3.setFont(font5)
        self.b_test_3.setStyleSheet(u"QToolButton {\n"
"	background-color: #3e37ff;\n"
"	border: none;\n"
"    border-radius: 10px;\n"
"    padding: 10px; \n"
"	margin: 0px 9px 0px 9px;\n"
"	color: white;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"	background-color: #000036;\n"
"}\n"
"\n"
"QToolButton:disabled {\n"
"    background-color: #808080; /* \u0160ed\u00e1 barva pro deaktivovan\u00e9 tla\u010d\u00edtko */\n"
"    color: #c0c0c0; /* Sv\u011btlej\u0161\u00ed \u0161ed\u00e1 barva textu */\n"
"    border: none;\n"
"}")

        self.gridLayout_13.addWidget(self.b_test_3, 4, 4, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_5, 4, 3, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_8, 4, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_test)
        self.page_settings = QWidget()
        self.page_settings.setObjectName(u"page_settings")
        self.gridLayout_32 = QGridLayout(self.page_settings)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.groupBox_24 = QGroupBox(self.page_settings)
        self.groupBox_24.setObjectName(u"groupBox_24")
        self.groupBox_24.setStyleSheet(u"QGroupBox {\n"
"	border: none;\n"
"}")
        self.gridLayout_27 = QGridLayout(self.groupBox_24)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.label_30 = QLabel(self.groupBox_24)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font5)
        self.label_30.setStyleSheet(u"color: #000036;")

        self.gridLayout_27.addWidget(self.label_30, 0, 0, 1, 1)

        self.b_light_on = QPushButton(self.groupBox_24)
        self.b_light_on.setObjectName(u"b_light_on")
        font11 = QFont()
        font11.setWeight(QFont.DemiBold)
        self.b_light_on.setFont(font11)
        self.b_light_on.setStyleSheet(u"QPushButton {\n"
"    background-color: #3e37ff;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #000036;\n"
"}")

        self.gridLayout_27.addWidget(self.b_light_on, 0, 1, 1, 1)

        self.b_light_off = QPushButton(self.groupBox_24)
        self.b_light_off.setObjectName(u"b_light_off")
        self.b_light_off.setFont(font11)
        self.b_light_off.setStyleSheet(u"QPushButton {\n"
"    background-color: #3e37ff;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #000036;\n"
"}")

        self.gridLayout_27.addWidget(self.b_light_off, 0, 2, 1, 1)


        self.gridLayout_32.addWidget(self.groupBox_24, 8, 0, 1, 2)

        self.groupBox_25 = QGroupBox(self.page_settings)
        self.groupBox_25.setObjectName(u"groupBox_25")
        self.groupBox_25.setStyleSheet(u"QGroupBox {\n"
"	border: none;\n"
"}")
        self.gridLayout_31 = QGridLayout(self.groupBox_25)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.label_10 = QLabel(self.groupBox_25)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font5)
        self.label_10.setStyleSheet(u"color: #000036;")

        self.gridLayout_31.addWidget(self.label_10, 0, 0, 1, 1)

        self.b_check_robot = QPushButton(self.groupBox_25)
        self.b_check_robot.setObjectName(u"b_check_robot")
        self.b_check_robot.setFont(font11)
        self.b_check_robot.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_31.addWidget(self.b_check_robot, 0, 1, 1, 1)


        self.gridLayout_32.addWidget(self.groupBox_25, 2, 0, 1, 2)

        self.groupBox_27 = QGroupBox(self.page_settings)
        self.groupBox_27.setObjectName(u"groupBox_27")
        self.groupBox_27.setStyleSheet(u"QGroupBox {\n"
"	border: none;\n"
"}")
        self.gridLayout_28 = QGridLayout(self.groupBox_27)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.label_7 = QLabel(self.groupBox_27)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font5)
        self.label_7.setStyleSheet(u"color: #000036;")

        self.gridLayout_28.addWidget(self.label_7, 0, 0, 1, 1)

        self.b_camera_check = QPushButton(self.groupBox_27)
        self.b_camera_check.setObjectName(u"b_camera_check")
        self.b_camera_check.setFont(font11)
        self.b_camera_check.setStyleSheet(u"QPushButton {\n"
"    background-color: #3e37ff;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #000036;\n"
"}")

        self.gridLayout_28.addWidget(self.b_camera_check, 0, 1, 1, 1)


        self.gridLayout_32.addWidget(self.groupBox_27, 7, 0, 1, 2)

        self.label_8 = QLabel(self.page_settings)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font5)
        self.label_8.setStyleSheet(u"color: #000036;\n"
"margin: 0px 0px 10px 5px;")
        self.label_8.setWordWrap(True)

        self.gridLayout_32.addWidget(self.label_8, 5, 0, 1, 2)

        self.label_2 = QLabel(self.page_settings)
        self.label_2.setObjectName(u"label_2")
        font12 = QFont()
        font12.setPointSize(13)
        font12.setBold(True)
        self.label_2.setFont(font12)
        self.label_2.setStyleSheet(u"color: #000036;\n"
"margin: 10px 0px 10px 0px;")

        self.gridLayout_32.addWidget(self.label_2, 0, 0, 1, 2)

        self.groupBox_23 = QGroupBox(self.page_settings)
        self.groupBox_23.setObjectName(u"groupBox_23")
        self.groupBox_23.setStyleSheet(u"QGroupBox {\n"
"	border: none;\n"
"}")
        self.gridLayout_30 = QGridLayout(self.groupBox_23)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.label_29 = QLabel(self.groupBox_23)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font5)
        self.label_29.setStyleSheet(u"color: #000036;")

        self.gridLayout_30.addWidget(self.label_29, 0, 0, 1, 1)

        self.b_camera_on = QPushButton(self.groupBox_23)
        self.b_camera_on.setObjectName(u"b_camera_on")
        self.b_camera_on.setFont(font11)
        self.b_camera_on.setStyleSheet(u"QPushButton {\n"
"    background-color: #3e37ff;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #000036;\n"
"}")

        self.gridLayout_30.addWidget(self.b_camera_on, 0, 1, 1, 1)

        self.b_camera_off = QPushButton(self.groupBox_23)
        self.b_camera_off.setObjectName(u"b_camera_off")
        self.b_camera_off.setFont(font11)
        self.b_camera_off.setStyleSheet(u"QPushButton {\n"
"    background-color: #3e37ff;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #000036;\n"
"}")

        self.gridLayout_30.addWidget(self.b_camera_off, 0, 2, 1, 1)


        self.gridLayout_32.addWidget(self.groupBox_23, 6, 0, 1, 2)

        self.label_28 = QLabel(self.page_settings)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font12)
        self.label_28.setStyleSheet(u"color: #000036;\n"
"margin: 10px 0px 10px 0px;")

        self.gridLayout_32.addWidget(self.label_28, 4, 0, 1, 2)

        self.line = QFrame(self.page_settings)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"color: #000036;")
        self.line.setFrameShadow(QFrame.Shadow.Plain)
        self.line.setLineWidth(11)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QFrame.Shape.HLine)

        self.gridLayout_32.addWidget(self.line, 3, 0, 1, 2)

        self.groupBox_14 = QGroupBox(self.page_settings)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.groupBox_14.setStyleSheet(u"QGroupBox {\n"
"	border: none;\n"
"}")
        self.gridLayout_16 = QGridLayout(self.groupBox_14)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.label_19 = QLabel(self.groupBox_14)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font5)
        self.label_19.setStyleSheet(u"color: #000036;\n"
"margin: 0px 20px 0px 0px;")

        self.gridLayout_16.addWidget(self.label_19, 0, 0, 1, 1)

        self.lineEdit_IP = QLineEdit(self.groupBox_14)
        self.lineEdit_IP.setObjectName(u"lineEdit_IP")
        self.lineEdit_IP.setFrame(True)

        self.gridLayout_16.addWidget(self.lineEdit_IP, 0, 1, 1, 1)

        self.label_20 = QLabel(self.groupBox_14)
        self.label_20.setObjectName(u"label_20")
        font13 = QFont()
        font13.setWeight(QFont.Thin)
        font13.setItalic(True)
        self.label_20.setFont(font13)
        self.label_20.setStyleSheet(u"color: #000036;\n"
"margin: 0px 20px 0px 20px;")

        self.gridLayout_16.addWidget(self.label_20, 0, 2, 1, 1)

        self.b_set_IP = QPushButton(self.groupBox_14)
        self.b_set_IP.setObjectName(u"b_set_IP")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.b_set_IP.sizePolicy().hasHeightForWidth())
        self.b_set_IP.setSizePolicy(sizePolicy8)
        self.b_set_IP.setMinimumSize(QSize(100, 0))
        font14 = QFont()
        font14.setPointSize(9)
        font14.setWeight(QFont.DemiBold)
        self.b_set_IP.setFont(font14)
        self.b_set_IP.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_16.addWidget(self.b_set_IP, 0, 3, 1, 1)


        self.gridLayout_32.addWidget(self.groupBox_14, 1, 0, 1, 2)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_32.addItem(self.verticalSpacer_6, 9, 0, 1, 2)

        self.stackedWidget.addWidget(self.page_settings)

        self.gridLayout.addWidget(self.stackedWidget, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.b_home_menu, self.b_calib_menu)
        QWidget.setTabOrder(self.b_calib_menu, self.b_test_menu)
        QWidget.setTabOrder(self.b_test_menu, self.b_settings_menu)
        QWidget.setTabOrder(self.b_settings_menu, self.b_new_calib)
        QWidget.setTabOrder(self.b_new_calib, self.b_upload_calib)
        QWidget.setTabOrder(self.b_upload_calib, self.b_save_results)
        QWidget.setTabOrder(self.b_save_results, self.b_save_data)
        QWidget.setTabOrder(self.b_save_data, self.b_upload_data)
        QWidget.setTabOrder(self.b_upload_data, self.b_calculate)
        QWidget.setTabOrder(self.b_calculate, self.b_test)
        QWidget.setTabOrder(self.b_test, self.slider_config)
        QWidget.setTabOrder(self.slider_config, self.slider_light)
        QWidget.setTabOrder(self.slider_light, self.comboBox_methods)
        QWidget.setTabOrder(self.comboBox_methods, self.lineEdit_rows)
        QWidget.setTabOrder(self.lineEdit_rows, self.lineEdit_columns)
        QWidget.setTabOrder(self.lineEdit_columns, self.lineEdit_size_square)
        QWidget.setTabOrder(self.lineEdit_size_square, self.lineEdit_size_marker)
        QWidget.setTabOrder(self.lineEdit_size_marker, self.b_set_board_params)
        QWidget.setTabOrder(self.b_set_board_params, self.b_initial_adjustment)
        QWidget.setTabOrder(self.b_initial_adjustment, self.b_start_calib)
        QWidget.setTabOrder(self.b_start_calib, self.slider_config_test)
        QWidget.setTabOrder(self.slider_config_test, self.slider_light_test)
        QWidget.setTabOrder(self.slider_light_test, self.b_test_1)
        QWidget.setTabOrder(self.b_test_1, self.b_test_3)
        QWidget.setTabOrder(self.b_test_3, self.lineEdit_IP)
        QWidget.setTabOrder(self.lineEdit_IP, self.b_set_IP)
        QWidget.setTabOrder(self.b_set_IP, self.b_check_robot)
        QWidget.setTabOrder(self.b_check_robot, self.b_camera_on)
        QWidget.setTabOrder(self.b_camera_on, self.b_camera_off)
        QWidget.setTabOrder(self.b_camera_off, self.b_camera_check)
        QWidget.setTabOrder(self.b_camera_check, self.b_light_on)
        QWidget.setTabOrder(self.b_light_on, self.b_light_off)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle("")
        self.b_test_menu.setText(QCoreApplication.translate("MainWindow", u"Test", None))
        self.b_home_menu.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.b_calib_menu.setText(QCoreApplication.translate("MainWindow", u"Calibration", None))
        self.b_settings_menu.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Calibration results", None))
        self.groupBox_8.setTitle("")
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Transformation: Camera -> Gripper (Base)", None))
        self.label_38.setText("")
        self.tfm_2_3.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.tfm_3_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.tfm_0_2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"[", None))
        self.tfm_1_1.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.tfm_0_0.setText(QCoreApplication.translate("MainWindow", u"0.0000000", None))
        self.tfm_1_2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.tfm_0_1.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.tfm_1_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.tfm_3_2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.tfm_2_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.tfm_3_3.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.tfm_2_2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.tfm_2_1.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"]", None))
        self.tfm_0_3.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.tfm_3_1.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.tfm_1_3.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Position vector [tx,ty,tz,rx,ry,rz]", None))
        self.pose_vector.setText(QCoreApplication.translate("MainWindow", u"[ 0, 0, 0, 0, 0, 0 ]", None))
        self.groupBox_7.setTitle("")
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Camera matrix", None))
        self.cm_0_2.setText(QCoreApplication.translate("MainWindow", u"0.0000000", None))
        self.cm_0_0.setText(QCoreApplication.translate("MainWindow", u"0.0000000", None))
        self.cm_1_1.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cm_0_1.setText(QCoreApplication.translate("MainWindow", u"0.0000000", None))
        self.cm_2_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cm_2_1.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cm_1_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cm_1_2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cm_2_2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"[", None))
        self.label_15.setText("")
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"]", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Distortion coefficients", None))
        self.dist_coeff.setText(QCoreApplication.translate("MainWindow", u"[ 0, 0, 0, 0, 0 ]", None))
        self.groupBox_9.setTitle("")
        self.groupBox_32.setTitle("")
        self.b_new_calib.setText(QCoreApplication.translate("MainWindow", u"New calibration", None))
        self.groupBox_30.setTitle("")
        self.b_upload_data.setText(QCoreApplication.translate("MainWindow", u"Upload data", None))
        self.b_calculate.setText(QCoreApplication.translate("MainWindow", u"Calculate calibration", None))
        self.groupBox_35.setTitle("")
        self.b_test.setText(QCoreApplication.translate("MainWindow", u"Test", None))
        self.groupBox_33.setTitle("")
        self.b_upload_calib.setText(QCoreApplication.translate("MainWindow", u"Upload calibration", None))
        self.groupBox_34.setTitle("")
        self.b_save_data.setText(QCoreApplication.translate("MainWindow", u"Save caliration data\n"
"(pictures, robot position...)", None))
        self.groupBox_31.setTitle("")
        self.b_save_results.setText(QCoreApplication.translate("MainWindow", u"Save calibration results\n"
"(below)", None))
        self.groupBox_15.setTitle("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Hand-exe calibration method:", None))
        self.comboBox_methods.setItemText(0, QCoreApplication.translate("MainWindow", u"ANDREFF", None))
        self.comboBox_methods.setItemText(1, QCoreApplication.translate("MainWindow", u"DANIILIDIS", None))
        self.comboBox_methods.setItemText(2, QCoreApplication.translate("MainWindow", u"HORAUD", None))
        self.comboBox_methods.setItemText(3, QCoreApplication.translate("MainWindow", u"PARK", None))
        self.comboBox_methods.setItemText(4, QCoreApplication.translate("MainWindow", u"TSAI", None))
        self.comboBox_methods.setItemText(5, QCoreApplication.translate("MainWindow", u"SHAH (world)", None))
        self.comboBox_methods.setItemText(6, QCoreApplication.translate("MainWindow", u"LI (world)", None))

        self.groupBox_13.setTitle("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Use lighting:", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"No", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Yes", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"Calibration Charuco board parameters", None))
        self.lineEdit_size_square.setText("")
        self.lineEdit_size_square.setPlaceholderText(QCoreApplication.translate("MainWindow", u"E.g. 30", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Size of squares (mm)", None))
        self.lineEdit_columns.setText("")
        self.lineEdit_columns.setPlaceholderText(QCoreApplication.translate("MainWindow", u"E.g. 8", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Size of markers (mm)", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Number of rows", None))
        self.lineEdit_size_marker.setText("")
        self.lineEdit_size_marker.setPlaceholderText(QCoreApplication.translate("MainWindow", u"E.g. 22", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Number of columns", None))
        self.lineEdit_rows.setInputMask("")
        self.lineEdit_rows.setText("")
        self.lineEdit_rows.setPlaceholderText(QCoreApplication.translate("MainWindow", u"E.g. 6", None))
        self.b_set_board_params.setText(QCoreApplication.translate("MainWindow", u"Set parameters", None))
        self.groupBox_12.setTitle("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Choose configuration:", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Camera on robot\n"
"Eye-in-Hand", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Camera fixed\n"
"Eye-to-hand", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Check in the settings if the robot and the camera are turned on\n"
" and connected !!!", None))
        self.groupBox_16.setTitle("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Initial adjustment of the robot against the calibration board is required before calibration", None))
        self.b_initial_adjustment.setText(QCoreApplication.translate("MainWindow", u"Initial adjustment", None))
        self.b_start_calib.setText(QCoreApplication.translate("MainWindow", u"Start automatic calibration", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"Calibration values", None))
        self.groupBox_17.setTitle("")
        self.groupBox_19.setTitle(QCoreApplication.translate("MainWindow", u"Camera matrix", None))
        self.cm_0_2_t.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cm_0_0_t.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cm_1_1_t.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cm_0_1_t.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cm_2_0_t.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cm_2_1_t.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cm_1_0_t.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cm_1_2_t.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cm_2_2_t.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"[", None))
        self.label_82.setText("")
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"]", None))
        self.groupBox_18.setTitle(QCoreApplication.translate("MainWindow", u"Distortion coefficients", None))
        self.dist_coeff_t.setText(QCoreApplication.translate("MainWindow", u"[ 0, 0, 0, 0, 0 ]", None))
        self.groupBox_20.setTitle("")
        self.groupBox_22.setTitle(QCoreApplication.translate("MainWindow", u"Position vector [tx,ty,tz,rx,ry,rz]", None))
        self.pose_vector_t.setText(QCoreApplication.translate("MainWindow", u"[ 0, 0, 0, 0, 0, 0 ]", None))
        self.groupBox_21.setTitle(QCoreApplication.translate("MainWindow", u"Transformation: Camera -> Gripper (Base)", None))
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"[", None))
        self.tfm_0_3_t.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.tfm_0_1_t.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.tfm_2_3_t.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.tfm_1_1_t.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.tfm_3_3_t.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"]", None))
        self.tfm_2_2_t.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_93.setText("")
        self.tfm_1_3_t.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.tfm_2_0_t.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.tfm_0_2_t.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.tfm_0_0_t.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.tfm_2_1_t.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.tfm_1_2_t.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.tfm_3_0_t.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.tfm_3_2_t.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.tfm_3_1_t.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.tfm_1_0_t.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(tooltip)
        self.b_test_1.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.b_test_1.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.b_test_1.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.b_test_2.setText(QCoreApplication.translate("MainWindow", u"Test 2\n"
"Pick and place 2", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Choose your configuration", None))
        self.groupBox_29.setTitle("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Camera on robot\n"
"Eye-in-Hand", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Camera fixed\n"
"Eye-to-hand", None))
        self.groupBox_28.setTitle("")
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Use lighting:", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"No", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Yes", None))
        self.b_test_3.setText(QCoreApplication.translate("MainWindow", u"Test 3\n"
"Board and tip", None))
        self.groupBox_24.setTitle("")
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Lighting", None))
        self.b_light_on.setText(QCoreApplication.translate("MainWindow", u"Turn ON", None))
        self.b_light_off.setText(QCoreApplication.translate("MainWindow", u"Turn OFF", None))
        self.groupBox_25.setTitle("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Check the connection to the robot", None))
        self.b_check_robot.setText(QCoreApplication.translate("MainWindow", u"Check connection", None))
        self.groupBox_27.setTitle("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Check camera connection", None))
        self.b_camera_check.setText(QCoreApplication.translate("MainWindow", u"Image display", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"First, configure the camera parameters in pylon Viewer. After completing the setup, disconnect the camera in pylon Viewer before using it in this application.", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"UR robot", None))
        self.groupBox_23.setTitle("")
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Camera power supply", None))
        self.b_camera_on.setText(QCoreApplication.translate("MainWindow", u"Power ON", None))
        self.b_camera_off.setText(QCoreApplication.translate("MainWindow", u"Power OFF", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Camera Basler", None))
        self.groupBox_14.setTitle("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Robot IP address:", None))
        self.lineEdit_IP.setInputMask(QCoreApplication.translate("MainWindow", u"000.000.000.000", None))
        self.lineEdit_IP.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.lineEdit_IP.setPlaceholderText(QCoreApplication.translate("MainWindow", u"192.168.209.124", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"(E.g. 192.168.209.124)", None))
        self.b_set_IP.setText(QCoreApplication.translate("MainWindow", u"Set IP address", None))
    # retranslateUi

