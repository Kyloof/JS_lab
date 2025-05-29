from log_reader.gui.ui_main_window import Ui_MainWindow  
from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog
from log_reader.utils.read_log import read_log_from_file
from log_reader.utils.get_logs_by_date import get_logs_by_date
import sys


class LogApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.previous_path = ""
        self.log_list = []

        self.ui.browse_button.clicked.connect(self.browse_file)
        self.ui.upper_date_edit.editingFinished.connect(self.get_by_dates)

    def load_logs(self, path):
        if path != self.previous_path:
            self.previous_path = path
            self.ui.log_list_widget.clear()
            self.log_list = read_log_from_file(path)
            for log in self.log_list:
                self.ui.log_list_widget.addItem(str(log))

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
