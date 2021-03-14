from PySide2 import sys
from PySide2 import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PySide demo')
        self.resize(200, 100)
        self.widget()
        
    def widget(self):
        title = QLabel('▼表示テキストの入力▼', self)
        # title.move(0,0)
        self.titleEdit = QLineEdit()

        self.btn = QPushButton("実行", self)
        # ボタンがclickされたときの処理
        self.btn.clicked.connect(self.button_click)
        self.change_text = QLabel('ここの文字が変わります', self)

        self.grid = QGridLayout()
        self.grid.addWidget(title, 0,0)
        self.grid.addWidget(self.titleEdit, 1,0)
        self.grid.addWidget(self.btn, 1,1)
        self.grid.addWidget(self.change_text, 2,0)
        self.setLayout(self.grid)
        
    def button_click(self):
        self.change_text.setText(self.titleEdit.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    windows = Demo()
    windows.show()
    sys.exit(app.exec_())