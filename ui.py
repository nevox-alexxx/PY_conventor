import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel, QHBoxLayout
from PyQt5.QtGui import QIcon

from file_converter import convert_file

class FileConverterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()
        self.source_file = ''
        self.destination_file = ''

    def setupUI(self):
        self.setWindowTitle('File Converter Tool')
        self.setWindowIcon(QIcon('convert.png')) 
        
        self.main_layout = QVBoxLayout()
        self.setStyleSheet("background-color: lightblue;")
        
        self.setupLabels()
        self.setupButtons()
        
        self.setLayout(self.main_layout)
        self.show()

    def setupLabels(self):
        self.status_label = QLabel('Select a file to convert')
        self.main_layout.addWidget(self.status_label)

    def setupButtons(self):
        self.button_layout = QHBoxLayout()

        self.select_file_button = QPushButton('Choose File')
        self.select_file_button.setStyleSheet("background-color: white; color: light-grey;")
        self.select_file_button.clicked.connect(self.selectFiles)
        self.button_layout.addWidget(self.select_file_button)

        self.convert_button = QPushButton('Start Conversion')
        self.convert_button.setStyleSheet("background-color: white; color: black;")
        self.convert_button.clicked.connect(self.convertFile)
        self.button_layout.addWidget(self.convert_button)

        self.main_layout.addLayout(self.button_layout)

    def selectFiles(self):
        options = QFileDialog.Options()
        self.source_file, _ = QFileDialog.getOpenFileName(self, 'Open Source File', '', 'All Files (*)', options=options)
        self.destination_file, _ = QFileDialog.getSaveFileName(self, 'Save Converted File As', '', 'All Files (*)', options=options)
        if self.source_file and self.destination_file:
            self.updateStatusLabel(f'Source: {self.source_file}\nDestination: {self.destination_file}')

    def updateStatusLabel(self, text):
        self.status_label.setText(text)

    def convertFile(self):
        if self.source_file and self.destination_file:
            try:
                convert_file(self.source_file, self.destination_file)
                self.updateStatusLabel('Conversion completed successfully!')
            except Exception as error:
                self.updateStatusLabel(f'Error: {str(error)}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    converter_app = FileConverterApp()
    sys.exit(app.exec_())
