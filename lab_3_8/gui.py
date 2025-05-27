import sys
from PySide6 import QtCore, QtWidgets, QtGui
from read_log import read_log_from_file


class LogApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.button = QtWidgets.QPushButton("Read logs!")
        self.text = QtWidgets.QLabel("Hello World",
                                     alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        self.log_list = QtWidgets.QListWidget()

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.log_list)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):

        logs = read_log_from_file("http_first_100k.log")
        for log in logs:
            QtWidgets.QListWidgetItem(" ".join(str(log)), self.log_list)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = LogApp()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
