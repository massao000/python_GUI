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
        self.layout = QVBoxLayout(self)
        
        self.tab_text1 = QLabel('タブ1')
        self.tab_text2 = QLabel('タブ2')
        
        self.tab = QTabWidget()
        self.tab.addTab(self.tab_text1, 'T2')
        self.tab.addTab(self.tab_text2, 'T1')

        self.layout.addWidget(self.tab)
        self.setLayout(self.layout)
            

if __name__ == '__main__':
    app = QApplication(sys.argv)
    windows = Demo()
    windows.show()
    sys.exit(app.exec_())