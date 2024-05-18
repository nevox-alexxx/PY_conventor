import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel

from converter import convert_file

class ConverterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.label = QLabel('Select files to convert')
        layout.addWidget(self.label)

        self.btn_open = QPushButton('Open File')
        self.btn_open.clicked.connect(self.showDialog)
        layout.addWidget(self.btn_open)

        self.btn_convert = QPushButton('Convert File')
        self.btn_convert.clicked.connect(self.convert_file)
        layout.addWidget(self.btn_convert)

        self.setLayout(layout)
        self.setWindowTitle('File Converter')
        self.show()

    def showDialog(self):
        options = QFileDialog.Options()
        self.input_file, _ = QFileDialog.getOpenFileName(self, 'Open File', '', 'All Files (*)', options=options)
        self.output_file, _ = QFileDialog.getSaveFileName(self, 'Save File', '', 'All Files (*)', options=options)
        if self.input_file and self.output_file:
            self.label.setText(f'Input: {self.input_file}\nOutput: {self.output_file}')

    def convert_file(self):
        if self.input_file and self.output_file:
            try:
                convert_file(self.input_file, self.output_file)
                self.label.setText('Conversion successful!')
            except Exception as e:
                self.label.setText(f'Error: {str(e)}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ConverterApp()
    sys.exit(app.exec_())