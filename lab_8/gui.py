# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_layout_based.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QHBoxLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTextBrowser, QToolButton, QVBoxLayout,
    QWidget)
from PySide6 import QtWidgets
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1165, 725)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 18, 20, 20)
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.horizontal_top_bar = QHBoxLayout()
        self.horizontal_top_bar.setObjectName(u"horizontal_top_bar")
        self.horizontal_path_bar = QHBoxLayout()
        self.horizontal_path_bar.setObjectName(u"horizontal_path_bar")
        self.path_edit = QLineEdit(self.centralwidget)
        self.path_edit.setObjectName(u"path_edit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.path_edit.sizePolicy().hasHeightForWidth())
        self.path_edit.setSizePolicy(sizePolicy2)
        self.path_edit.setMinimumSize(QSize(450, 30))
        self.path_edit.setMaximumSize(QSize(600, 40))

        self.horizontal_path_bar.addWidget(self.path_edit)

        self.browse_button = QToolButton(self.centralwidget)
        self.browse_button.setObjectName(u"browse_button")
        self.browse_button.setMinimumSize(QSize(0, 30))

        self.horizontal_path_bar.addWidget(self.browse_button)


        self.horizontal_top_bar.addLayout(self.horizontal_path_bar)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontal_top_bar.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontal_top_bar)

        self.verticalSpacer = QSpacerItem(10, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontal_date_bar = QHBoxLayout()
        self.horizontal_date_bar.setObjectName(u"horizontal_date_bar")
        self.from_label = QLabel(self.centralwidget)
        self.from_label.setObjectName(u"from_label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.from_label.sizePolicy().hasHeightForWidth())
        self.from_label.setSizePolicy(sizePolicy3)
        self.from_label.setMaximumSize(QSize(50, 16777215))
        font = QFont()
        font.setPointSize(10)
        self.from_label.setFont(font)

        self.horizontal_date_bar.addWidget(self.from_label)

        self.lower_date_edit = QDateEdit(self.centralwidget)
        self.lower_date_edit.setObjectName(u"lower_date_edit")
        self.lower_date_edit.setMinimumSize(QSize(130, 30))
        self.lower_date_edit.setMaximumSize(QSize(130, 50))
        self.lower_date_edit.setCalendarPopup(True)

        self.horizontal_date_bar.addWidget(self.lower_date_edit)

        self.horizontalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontal_date_bar.addItem(self.horizontalSpacer_3)

        self.to_label = QLabel(self.centralwidget)
        self.to_label.setObjectName(u"to_label")
        self.to_label.setMaximumSize(QSize(30, 16777215))
        self.to_label.setFont(font)

        self.horizontal_date_bar.addWidget(self.to_label)

        self.upper_date_edit = QDateEdit(self.centralwidget)
        self.upper_date_edit.setObjectName(u"upper_date_edit")
        self.upper_date_edit.setMinimumSize(QSize(130, 30))
        self.upper_date_edit.setMaximumSize(QSize(130, 50))
        self.upper_date_edit.setCalendarPopup(True)

        self.horizontal_date_bar.addWidget(self.upper_date_edit)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontal_date_bar.addItem(self.horizontalSpacer_2)

        self.horizontal_date_bar.setStretch(0, 1)
        self.horizontal_date_bar.setStretch(1, 1)
        self.horizontal_date_bar.setStretch(3, 1)
        self.horizontal_date_bar.setStretch(4, 1)
        self.horizontal_date_bar.setStretch(5, 5)

        self.verticalLayout.addLayout(self.horizontal_date_bar)

        self.verticalSpacer_2 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontal_main_bar = QHBoxLayout()
        self.horizontal_main_bar.setObjectName(u"horizontal_main_bar")
        self.log_list_widget = QListWidget(self.centralwidget)
        self.log_list_widget.setObjectName(u"log_list_widget")
        self.log_list_widget.setMinimumSize(QSize(550, 400))
        self.log_list_widget.setMaximumSize(QSize(750, 600))

        self.horizontal_main_bar.addWidget(self.log_list_widget)

        self.horizontalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontal_main_bar.addItem(self.horizontalSpacer_4)

        self.vertical_details = QVBoxLayout()
        self.vertical_details.setObjectName(u"vertical_details")
        self.horizontal_host = QHBoxLayout()
        self.horizontal_host.setObjectName(u"horizontal_host")
        self.host_label = QLabel(self.centralwidget)
        self.host_label.setObjectName(u"host_label")
        self.host_label.setMinimumSize(QSize(90, 0))

        self.horizontal_host.addWidget(self.host_label)

        self.host_browser = QTextBrowser(self.centralwidget)
        self.host_browser.setObjectName(u"host_browser")
        self.host_browser.setMinimumSize(QSize(0, 20))

        self.horizontal_host.addWidget(self.host_browser)


        self.vertical_details.addLayout(self.horizontal_host)

        self.verticalSpacer_8 = QSpacerItem(20, 150, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vertical_details.addItem(self.verticalSpacer_8)

        self.horizontal_target = QHBoxLayout()
        self.horizontal_target.setObjectName(u"horizontal_target")
        self.target_label = QLabel(self.centralwidget)
        self.target_label.setObjectName(u"target_label")
        self.target_label.setMinimumSize(QSize(90, 0))

        self.horizontal_target.addWidget(self.target_label)

        self.target_browser = QTextBrowser(self.centralwidget)
        self.target_browser.setObjectName(u"target_browser")
        self.target_browser.setMinimumSize(QSize(0, 20))

        self.horizontal_target.addWidget(self.target_browser)


        self.vertical_details.addLayout(self.horizontal_target)

        self.verticalSpacer_7 = QSpacerItem(20, 150, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vertical_details.addItem(self.verticalSpacer_7)

        self.horizontal_datetime = QHBoxLayout()
        self.horizontal_datetime.setObjectName(u"horizontal_datetime")
        self.horizontal_date = QVBoxLayout()
        self.horizontal_date.setObjectName(u"horizontal_date")
        self.date_label = QLabel(self.centralwidget)
        self.date_label.setObjectName(u"date_label")

        self.horizontal_date.addWidget(self.date_label)

        self.date_browser = QTextBrowser(self.centralwidget)
        self.date_browser.setObjectName(u"date_browser")
        sizePolicy2.setHeightForWidth(self.date_browser.sizePolicy().hasHeightForWidth())
        self.date_browser.setSizePolicy(sizePolicy2)
        self.date_browser.setMinimumSize(QSize(0, 5))

        self.horizontal_date.addWidget(self.date_browser)


        self.horizontal_datetime.addLayout(self.horizontal_date)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontal_datetime.addItem(self.horizontalSpacer_6)

        self.vertical_time = QVBoxLayout()
        self.vertical_time.setObjectName(u"vertical_time")
        self.time_label = QLabel(self.centralwidget)
        self.time_label.setObjectName(u"time_label")

        self.vertical_time.addWidget(self.time_label)

        self.time_browser = QTextBrowser(self.centralwidget)
        self.time_browser.setObjectName(u"time_browser")
        sizePolicy2.setHeightForWidth(self.time_browser.sizePolicy().hasHeightForWidth())
        self.time_browser.setSizePolicy(sizePolicy2)
        self.time_browser.setMinimumSize(QSize(0, 5))

        self.vertical_time.addWidget(self.time_browser)


        self.horizontal_datetime.addLayout(self.vertical_time)


        self.vertical_details.addLayout(self.horizontal_datetime)

        self.verticalSpacer_5 = QSpacerItem(20, 150, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vertical_details.addItem(self.verticalSpacer_5)

        self.horizontal_status = QHBoxLayout()
        self.horizontal_status.setObjectName(u"horizontal_status")
        self.status_label = QLabel(self.centralwidget)
        self.status_label.setObjectName(u"status_label")
        self.status_label.setMinimumSize(QSize(90, 0))

        self.horizontal_status.addWidget(self.status_label)

        self.status_browser = QTextBrowser(self.centralwidget)
        self.status_browser.setObjectName(u"status_browser")
        self.status_browser.setMinimumSize(QSize(0, 20))

        self.horizontal_status.addWidget(self.status_browser)

        self.horizontalSpacer_9 = QSpacerItem(400, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontal_status.addItem(self.horizontalSpacer_9)


        self.vertical_details.addLayout(self.horizontal_status)

        self.verticalSpacer_6 = QSpacerItem(20, 150, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vertical_details.addItem(self.verticalSpacer_6)

        self.horizontal_method = QHBoxLayout()
        self.horizontal_method.setObjectName(u"horizontal_method")
        self.method_label = QLabel(self.centralwidget)
        self.method_label.setObjectName(u"method_label")
        self.method_label.setMinimumSize(QSize(90, 0))

        self.horizontal_method.addWidget(self.method_label)

        self.method_browser = QTextBrowser(self.centralwidget)
        self.method_browser.setObjectName(u"method_browser")
        self.method_browser.setMinimumSize(QSize(0, 20))

        self.horizontal_method.addWidget(self.method_browser)

        self.horizontalSpacer_8 = QSpacerItem(400, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontal_method.addItem(self.horizontalSpacer_8)


        self.vertical_details.addLayout(self.horizontal_method)


        self.horizontal_main_bar.addLayout(self.vertical_details)


        self.verticalLayout.addLayout(self.horizontal_main_bar)

        self.horizontal_buttons = QHBoxLayout()
        self.horizontal_buttons.setObjectName(u"horizontal_buttons")
        self.previous_button = QPushButton(self.centralwidget)
        self.previous_button.setObjectName(u"previous_button")
        self.previous_button.setMinimumSize(QSize(100, 30))
        self.previous_button.setMaximumSize(QSize(100, 40))

        self.horizontal_buttons.addWidget(self.previous_button)

        self.horizontalSpacer_7 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontal_buttons.addItem(self.horizontalSpacer_7)

        self.next_button = QPushButton(self.centralwidget)
        self.next_button.setObjectName(u"next_button")
        self.next_button.setMinimumSize(QSize(100, 30))
        self.next_button.setMaximumSize(QSize(100, 40))

        self.horizontal_buttons.addWidget(self.next_button)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontal_buttons.addItem(self.horizontalSpacer_5)

        self.horizontal_buttons.setStretch(3, 10)

        self.verticalLayout.addLayout(self.horizontal_buttons)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 1)
        self.verticalLayout.setStretch(5, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1165, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.path_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter a path to the log file", None))
        self.browse_button.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.from_label.setText(QCoreApplication.translate("MainWindow", u"From", None))
        self.to_label.setText(QCoreApplication.translate("MainWindow", u"To", None))
        self.host_label.setText(QCoreApplication.translate("MainWindow", u"Host Address", None))
        self.target_label.setText(QCoreApplication.translate("MainWindow", u"Target Address", None))
        self.date_label.setText(QCoreApplication.translate("MainWindow", u"Date", None))
        self.time_label.setText(QCoreApplication.translate("MainWindow", u"Time", None))
        self.status_label.setText(QCoreApplication.translate("MainWindow", u"Status Code", None))
        self.method_label.setText(QCoreApplication.translate("MainWindow", u"Method", None))
        self.previous_button.setText(QCoreApplication.translate("MainWindow", u"Previous", None))
        self.next_button.setText(QCoreApplication.translate("MainWindow", u"Next", None))
    # retranslateUi



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)  # <-- pass the QMainWindow instance here
    MainWindow.show()

    sys.exit(app.exec())