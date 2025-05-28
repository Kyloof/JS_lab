# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui_project.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import sys
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLayout,
    QListWidget, QListWidgetItem, QMainWindow, QMenuBar,
    QPushButton, QScrollBar, QSizePolicy, QSpacerItem,
    QStatusBar, QTextBrowser, QTextEdit, QVBoxLayout,
    QWidget)
from PySide6 import QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1089, 626)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.open_button = QPushButton(self.centralwidget)
        self.open_button.setObjectName(u"open_button")
        self.open_button.setGeometry(QRect(830, 30, 141, 41))
        self.log_path_edit = QTextEdit(self.centralwidget)
        self.log_path_edit.setObjectName(u"log_path_edit")
        self.log_path_edit.setGeometry(QRect(0, 30, 781, 41))
        self.horizontalLayoutWidget_6 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(10, 110, 1041, 371))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.log_list = QListWidget(self.horizontalLayoutWidget_6)
        self.log_list.setObjectName(u"log_list")
        self.log_list.setMinimumSize(QSize(550, 100))
        self.log_list.setMaximumSize(QSize(365, 16777215))

        self.horizontalLayout_6.addWidget(self.log_list)

        self.list_scroll_bar = QScrollBar(self.horizontalLayoutWidget_6)
        self.list_scroll_bar.setObjectName(u"list_scroll_bar")
        self.list_scroll_bar.setOrientation(Qt.Vertical)

        self.horizontalLayout_6.addWidget(self.list_scroll_bar)

        self.list_spacer = QSpacerItem(200, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.list_spacer)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.remote_host_label = QLabel(self.horizontalLayoutWidget_6)
        self.remote_host_label.setObjectName(u"remote_host_label")
        self.remote_host_label.setMinimumSize(QSize(75, 0))

        self.horizontalLayout.addWidget(self.remote_host_label)

        self.remote_host_text = QTextBrowser(self.horizontalLayoutWidget_6)
        self.remote_host_text.setObjectName(u"remote_host_text")
        self.remote_host_text.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.remote_host_text.sizePolicy().hasHeightForWidth())
        self.remote_host_text.setSizePolicy(sizePolicy)
        self.remote_host_text.setMinimumSize(QSize(0, 1))

        self.horizontalLayout.addWidget(self.remote_host_text)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.date_label = QLabel(self.horizontalLayoutWidget_6)
        self.date_label.setObjectName(u"date_label")
        self.date_label.setMinimumSize(QSize(75, 0))

        self.horizontalLayout_2.addWidget(self.date_label)

        self.date_text = QTextBrowser(self.horizontalLayoutWidget_6)
        self.date_text.setObjectName(u"date_text")
        self.date_text.setMinimumSize(QSize(0, 1))

        self.horizontalLayout_2.addWidget(self.date_text)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.time_label = QLabel(self.horizontalLayoutWidget_6)
        self.time_label.setObjectName(u"time_label")
        self.time_label.setMinimumSize(QSize(75, 0))

        self.horizontalLayout_3.addWidget(self.time_label)

        self.time_text = QTextBrowser(self.horizontalLayoutWidget_6)
        self.time_text.setObjectName(u"time_text")
        self.time_text.setMinimumSize(QSize(0, 1))

        self.horizontalLayout_3.addWidget(self.time_text)

        self.timezone_label = QLabel(self.horizontalLayoutWidget_6)
        self.timezone_label.setObjectName(u"timezone_label")
        self.timezone_label.setMinimumSize(QSize(75, 0))

        self.horizontalLayout_3.addWidget(self.timezone_label)

        self.timezone_text = QTextBrowser(self.horizontalLayoutWidget_6)
        self.timezone_text.setObjectName(u"timezone_text")
        self.timezone_text.setMinimumSize(QSize(0, 1))

        self.horizontalLayout_3.addWidget(self.timezone_text)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.status_label = QLabel(self.horizontalLayoutWidget_6)
        self.status_label.setObjectName(u"status_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(75)
        sizePolicy1.setHeightForWidth(self.status_label.sizePolicy().hasHeightForWidth())
        self.status_label.setSizePolicy(sizePolicy1)
        self.status_label.setMinimumSize(QSize(75, 0))

        self.horizontalLayout_4.addWidget(self.status_label)

        self.status_text = QTextBrowser(self.horizontalLayoutWidget_6)
        self.status_text.setObjectName(u"status_text")
        self.status_text.setMinimumSize(QSize(0, 1))

        self.horizontalLayout_4.addWidget(self.status_text)

        self.metkod_label = QLabel(self.horizontalLayoutWidget_6)
        self.metkod_label.setObjectName(u"metkod_label")
        self.metkod_label.setMinimumSize(QSize(75, 0))

        self.horizontalLayout_4.addWidget(self.metkod_label)

        self.metkod_text = QTextBrowser(self.horizontalLayoutWidget_6)
        self.metkod_text.setObjectName(u"metkod_text")
        self.metkod_text.setMinimumSize(QSize(0, 1))

        self.horizontalLayout_4.addWidget(self.metkod_text)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.resource_label = QLabel(self.horizontalLayoutWidget_6)
        self.resource_label.setObjectName(u"resource_label")
        self.resource_label.setMinimumSize(QSize(75, 0))

        self.horizontalLayout_5.addWidget(self.resource_label)

        self.resource_text = QTextBrowser(self.horizontalLayoutWidget_6)
        self.resource_text.setObjectName(u"resource_text")
        self.resource_text.setMinimumSize(QSize(0, 1))

        self.horizontalLayout_5.addWidget(self.resource_text)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.size_label = QLabel(self.horizontalLayoutWidget_6)
        self.size_label.setObjectName(u"size_label")
        self.size_label.setMinimumSize(QSize(75, 0))

        self.horizontalLayout_7.addWidget(self.size_label)

        self.size_text = QTextBrowser(self.horizontalLayoutWidget_6)
        self.size_text.setObjectName(u"size_text")
        self.size_text.setMinimumSize(QSize(0, 1))

        self.horizontalLayout_7.addWidget(self.size_text)


        self.verticalLayout.addLayout(self.horizontalLayout_7)


        self.horizontalLayout_6.addLayout(self.verticalLayout)

        self.horizontalLayoutWidget_8 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_8.setObjectName(u"horizontalLayoutWidget_8")
        self.horizontalLayoutWidget_8.setGeometry(QRect(10, 500, 1041, 61))
        self.horizontalLayout_8 = QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.previous_button = QPushButton(self.horizontalLayoutWidget_8)
        self.previous_button.setObjectName(u"previous_button")

        self.horizontalLayout_8.addWidget(self.previous_button)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_2)

        self.next_button = QPushButton(self.horizontalLayoutWidget_8)
        self.next_button.setObjectName(u"next_button")

        self.horizontalLayout_8.addWidget(self.next_button)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1089, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.open_button.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.remote_host_label.setText(QCoreApplication.translate("MainWindow", u"Remote host", None))
        self.date_label.setText(QCoreApplication.translate("MainWindow", u"Date", None))
        self.time_label.setText(QCoreApplication.translate("MainWindow", u"Time", None))
        self.timezone_label.setText(QCoreApplication.translate("MainWindow", u"Timezone", None))
        self.status_label.setText(QCoreApplication.translate("MainWindow", u"Status Code", None))
        self.metkod_label.setText(QCoreApplication.translate("MainWindow", u"Metkod", None))
        self.resource_label.setText(QCoreApplication.translate("MainWindow", u"Resource", None))
        self.size_label.setText(QCoreApplication.translate("MainWindow", u"Size", None))
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
