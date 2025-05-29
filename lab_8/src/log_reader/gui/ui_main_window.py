from PySide6.QtCore import QSize, QRect, QCoreApplication
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QToolButton,
    QVBoxLayout, QHBoxLayout, QListWidget, QTextBrowser, QDateEdit,
    QPushButton, QSpacerItem, QSizePolicy, QMenuBar, QStatusBar
)
import sys

class Ui_MainWindow:
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1165, 600) 

        central_widget = QWidget(MainWindow)
        central_widget.setObjectName("central_widget")

        sizePolicyFixed = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicyExpanding = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicyPreferred = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)

        vertical_layout = QVBoxLayout(central_widget)
        vertical_layout.setSpacing(5)
        vertical_layout.setContentsMargins(20, 18, 20, 20)

        vertical_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        # Top bar with path text edit and browse button
        horizontal_top_bar = QHBoxLayout()
        horizontal_path_bar = QHBoxLayout()

        self.path_edit = QLineEdit(central_widget)
        self.path_edit.setObjectName("path_edit")
        self.path_edit.setSizePolicy(sizePolicyExpanding)
        self.path_edit.setMinimumSize(QSize(450, 30))
        self.path_edit.setMaximumSize(QSize(600, 40))
        self.path_edit.setPlaceholderText("Enter a path to the log file")
        horizontal_path_bar.addWidget(self.path_edit)

        self.browse_button = QToolButton(central_widget)
        self.browse_button.setObjectName("browse_button")
        self.browse_button.setMinimumSize(QSize(0, 30))
        self.browse_button.setText("...")
        horizontal_path_bar.addWidget(self.browse_button)

        horizontal_top_bar.addLayout(horizontal_path_bar)
        horizontal_top_bar.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))

        vertical_layout.addLayout(horizontal_top_bar)
        vertical_layout.addSpacerItem(QSpacerItem(10, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed))

        # Date bar
        horizontal_date_bar = QHBoxLayout()

        from_label = QLabel("From", central_widget)
        from_label.setObjectName("from_label")
        from_label.setSizePolicy(sizePolicyPreferred)
        from_label.setMaximumSize(QSize(50, 16777215))
        horizontal_date_bar.addWidget(from_label)

        self.lower_date_edit = QDateEdit(central_widget)
        self.lower_date_edit.setObjectName("lower_date_edit")
        self.lower_date_edit.setMinimumSize(QSize(130, 30))
        self.lower_date_edit.setMaximumSize(QSize(130, 50))
        self.lower_date_edit.setCalendarPopup(True)
        horizontal_date_bar.addWidget(self.lower_date_edit)

        horizontal_date_bar.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum))

        to_label = QLabel("To", central_widget)
        to_label.setObjectName("to_label")
        to_label.setMaximumSize(QSize(30, 16777215))
        horizontal_date_bar.addWidget(to_label)

        self.upper_date_edit = QDateEdit(central_widget)
        self.upper_date_edit.setObjectName("upper_date_edit")
        self.upper_date_edit.setMinimumSize(QSize(130, 30))
        self.upper_date_edit.setMaximumSize(QSize(130, 50))
        self.upper_date_edit.setCalendarPopup(True)
        horizontal_date_bar.addWidget(self.upper_date_edit)

        horizontal_date_bar.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))

        horizontal_date_bar.setStretch(0, 1)
        horizontal_date_bar.setStretch(1, 1)
        horizontal_date_bar.setStretch(3, 1)
        horizontal_date_bar.setStretch(4, 1)
        horizontal_date_bar.setStretch(5, 5)

        vertical_layout.addLayout(horizontal_date_bar)
        vertical_layout.addSpacerItem(QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed))

        horizontal_main_bar = QHBoxLayout()

        self.log_list_widget = QListWidget(central_widget)
        self.log_list_widget.setObjectName("log_list_widget")
        self.log_list_widget.setMinimumSize(QSize(550, 400))
        self.log_list_widget.setMaximumSize(QSize(750, 600))
        horizontal_main_bar.addWidget(self.log_list_widget)

        horizontal_main_bar.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))

        vertical_details = QVBoxLayout()

        def make_label_and_browser(label_text):
            h_layout = QHBoxLayout()
            label = QLabel(label_text, central_widget)
            label.setMinimumSize(QSize(90, 0))
            h_layout.addWidget(label)
            browser = QTextBrowser(central_widget)
            browser.setMinimumSize(QSize(0, 15))
            browser.setFixedHeight(50) 
            h_layout.addWidget(browser)
            return h_layout, browser

        # Host Address
        horizontal_host, self.host_browser = make_label_and_browser("Host Address")
        vertical_details.addLayout(horizontal_host)
        vertical_details.addSpacerItem(QSpacerItem(20, 100, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        # Target Address
        horizontal_target, self.target_browser = make_label_and_browser("Target Address")
        vertical_details.addLayout(horizontal_target)
        vertical_details.addSpacerItem(QSpacerItem(20, 100, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        # Date and Time layout
        horizontal_datetime = QHBoxLayout()

        def make_label_and_browser(label_text):
            v_layout = QVBoxLayout()
            label = QLabel(label_text, central_widget)
            v_layout.addWidget(label)
            browser = QTextBrowser(central_widget)
            browser.setMinimumSize(QSize(0, 5))
            browser.setFixedHeight(50)
            v_layout.addWidget(browser)
            return v_layout, browser

        horizontal_date, self.date_browser = make_label_and_browser("Date")
        horizontal_datetime.addLayout(horizontal_date)

        horizontal_datetime.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))

        vertical_time, self.time_browser = make_label_and_browser("Time")
        horizontal_datetime.addLayout(vertical_time)

        vertical_details.addLayout(horizontal_datetime)
        vertical_details.addSpacerItem(QSpacerItem(20, 100, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        # Status Code
        horizontal_status, self.status_browser = make_label_and_browser("Status Code")
        self.status_browser.setMaximumWidth(250)
        vertical_details.addLayout(horizontal_status)
        
        # Method
        horizontal_method, self.method_browser = make_label_and_browser("Method")
        self.method_browser.setMaximumWidth(250)  
        horizontal_method.addSpacerItem(QSpacerItem(400, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        vertical_details.addLayout(horizontal_method)

        
        horizontal_main_bar.addLayout(vertical_details)
        vertical_layout.addLayout(horizontal_main_bar)

        # Buttons bar
        horizontal_buttons = QHBoxLayout()
        self.previous_button = QPushButton("Previous", central_widget)
        self.previous_button.setMinimumSize(QSize(100, 30))
        self.previous_button.setMaximumSize(QSize(100, 40))
        horizontal_buttons.addWidget(self.previous_button)

        horizontal_buttons.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum))

        self.next_button = QPushButton("Next", central_widget)
        self.next_button.setMinimumSize(QSize(100, 30))
        self.next_button.setMaximumSize(QSize(100, 40))
        horizontal_buttons.addWidget(self.next_button)

        horizontal_buttons.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        horizontal_buttons.setStretch(3, 10)

        vertical_layout.addLayout(horizontal_buttons)
        vertical_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        vertical_layout.setStretch(1, 1)
        vertical_layout.setStretch(3, 1)
        vertical_layout.setStretch(4, 1)
        vertical_layout.setStretch(5, 1)

        MainWindow.setCentralWidget(central_widget)

        menubar = QMenuBar(MainWindow)
        menubar.setGeometry(QRect(0, 0, 1165, 26))
        MainWindow.setMenuBar(menubar)

        statusbar = QStatusBar(MainWindow)
        MainWindow.setStatusBar(statusbar)

        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "MainWindow"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
