from log_reader.gui.ui_main_window import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog
from log_reader.utils.read_log import read_log_from_file
from log_reader.utils.get_logs_by_date import get_logs_by_date
from PySide6.QtCore import Qt
import sys


class LogApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.previous_path = ""
        self.log_list = []

        self.current_log = None

        self.ui.browse_button.clicked.connect(self.browse_file)
        self.ui.upper_date_edit.editingFinished.connect(self.get_by_dates)

        self.ui.log_list_widget.currentItemChanged.connect(self.extract_log_info)
        self.ui.next_button.clicked.connect(self.next_log)
        self.ui.previous_button.clicked.connect(self.prev_log)


    def extract_log_info(self, item):
        self.current_log = self.ui.log_list_widget.row(item)

        self.change_labels(self.log_list[self.current_log])
        self.update_navigation_buttons()

    def change_labels(self, log):
        self.ui.host_browser.setText(log.host_address)
        self.ui.target_browser.setText(log.target_address)
        self.ui.status_browser.setText(log.status_code)
        self.ui.method_browser.setText(log.method)
        self.ui.time_browser.setText(str(log.time))
        self.ui.date_browser.setText(str(log.date))

    def reset_labels(self):
        self.ui.host_browser.setText('')
        self.ui.target_browser.setText('')
        self.ui.status_browser.setText('')
        self.ui.method_browser.setText('')
        self.ui.time_browser.setText('')
        self.ui.date_browser.setText('')

    def next_log(self):
        if self.current_log is None:
            return

        if self.current_log < len(self.log_list) - 1:
            self.current_log += 1
            self.ui.log_list_widget.setCurrentRow(self.current_log)

        self.update_navigation_buttons()

    def prev_log(self):
        if self.current_log is None:
            return

        if self.current_log > 0:
            self.current_log -= 1
            self.ui.log_list_widget.setCurrentRow(self.current_log)

        self.update_navigation_buttons()

    def update_navigation_buttons(self):
        if not self.log_list or self.current_log is None:
            self.ui.previous_button.setEnabled(False)
            self.ui.next_button.setEnabled(False)
            return

        self.ui.previous_button.setEnabled(self.current_log > 0)
        self.ui.next_button.setEnabled(self.current_log < len(self.log_list) - 1)

    def load_logs(self, path):
        if path != self.previous_path:
            self.previous_path = path
            self.ui.log_list_widget.clear()
            self.log_list = read_log_from_file(path)
            for log in self.log_list:
                self.ui.log_list_widget.addItem(str(log))

            self.current_log = None
            self.reset_labels()

            self.update_navigation_buttons()

    def browse_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Log File", "", "Log Files (*.log *.txt);;All Files (*)")
        if file_path:
            self.ui.path_edit.setText(file_path)
            self.load_logs(file_path)

    def get_by_dates(self):
        self.ui.log_list_widget.clear()
        for log in self.log_list:
            if log.is_withing_bounds(self.ui.lower_date_edit.date(), self.ui.upper_date_edit.date()):
                self.ui.log_list_widget.addItem(str(log))

    



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LogApp()
    window.show()
    sys.exit(app.exec())
