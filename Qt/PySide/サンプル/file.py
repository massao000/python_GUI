from PySide2 import sys
from PySide2 import *
from PySide2.QtWidgets import *
# from PySide2.QtCore import *

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PySide demo')
        self.resize(200, 150)
        self.widget()
        
    def widget(self):
        self.open_file = QPushButton("ファイル選択", self)
        self.open_file.clicked.connect(self.open_file_menu)
        self.open_file.setGeometry(50, 55, 100, 30)
        # self.grid = QGridLayout()
        # self.grid.addWidget(self.open_file, 0,0)
        # self.setLayout(self.grid)
        # self.show()

    def open_file_menu(self):
        directory = QFileDialog.getOpenFileName()
        self.file.setText(f'{directory[0]}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    windows = Demo()
    windows.show()
    sys.exit(app.exec_())