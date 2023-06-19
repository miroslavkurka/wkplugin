from PyQt5 import QtWidgets
from pymol import cmd


class LoadFileDialog(QtWidgets.QWidget):
    """
    This class implements very simple dialog to "load" a file.
    It's based on ui of getSaveFileNameWithExt() from pymol.Qt.utils

    """
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Load File')
        self.setGeometry(200, 200, 400, 100)

        self.layout = QtWidgets.QVBoxLayout()

        self.file_path_label = QtWidgets.QLabel('File Path:')
        self.layout.addWidget(self.file_path_label)

        self.file_path_line_edit = QtWidgets.QLineEdit()
        self.layout.addWidget(self.file_path_line_edit)

        self.load_button = QtWidgets.QPushButton('Load')
        self.load_button.clicked.connect(self.load_file)
        self.layout.addWidget(self.load_button)

        self.setLayout(self.layout)

    def load_file(self):
        file_path = self.file_path_line_edit.text()

        if file_path:
            return file_path
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setText('File path is empty!')
        msg.setWindowTitle('Warning')
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()
        return None


