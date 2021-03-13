from PySide2 import sys
from PySide2 import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PySide demo')
        self.resize(200, 150)
        self.widget()
        
    def widget(self):

        self.btn_pop = QPushButton("pop", self)
        # ボタンがclickされたときの処理
        self.btn_pop.clicked.connect(self.pop)
        self.btn_pop.setGeometry(50, 50, 100, 30)
        # self.grid = QGridLayout()
        # self.grid.addWidget(self.btn_pop, 0,0)
        # self.setLayout(self.grid)
    
    def pop(self):
        reply = QMessageBox.information(self, "popup表示", 'ポップアップの表示', QMessageBox.Ok)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    windows = Demo()
    windows.show()
    sys.exit(app.exec_())