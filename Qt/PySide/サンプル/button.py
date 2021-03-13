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
        self.check_text = QLabel('チェックボックス')
        self.check_btn1 = QCheckBox("1")
        self.check_btn2 = QCheckBox("2")
        self.check_btn3 = QCheckBox("3")

        self.radio_text = QLabel('ラジオボタン')
        self.radio_btn1 = QRadioButton("1")
        self.radio_btn2 = QRadioButton("2")
        self.radio_btn3 = QRadioButton("3")

        self.button = QPushButton("ボタン")
        
        self.grid1 = QGridLayout()
        self.grid1.addWidget(self.check_text, 0, 0, 1, 3)
        self.grid1.addWidget(self.check_btn1, 1, 0)
        self.grid1.addWidget(self.check_btn2, 1, 1)
        self.grid1.addWidget(self.check_btn3, 1, 2)
        self.grid1.addWidget(self.radio_text, 2, 0, 2, 3)
        self.grid1.addWidget(self.radio_btn1, 3, 0)
        self.grid1.addWidget(self.radio_btn2, 3, 1)
        self.grid1.addWidget(self.radio_btn3, 3, 2)

        self.grid2 = QGridLayout()
        self.grid2.addWidget(self.button, 4, 1)

        self.grid = QGridLayout()
        self.grid.addLayout(self.grid1, 0, 0)
        self.grid.addLayout(self.grid2, 1, 0)

        self.setLayout(self.grid)
            

if __name__ == '__main__':
    app = QApplication(sys.argv)
    windows = Demo()
    windows.show()
    sys.exit(app.exec_())