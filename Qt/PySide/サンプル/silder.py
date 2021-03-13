from PySide2 import sys
from PySide2 import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PySide demo')
        # self.resize(220, 220)
        self.widget()
        
    def widget(self):
        self.slider = QSlider(Qt.Vertical, self)
        self.slider.setGeometry(10, 30, 30, 200)

        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setGeometry(10, 250, 200, 30)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    windows = Demo()
    windows.show()
    sys.exit(app.exec_())