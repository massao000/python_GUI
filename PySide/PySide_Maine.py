import sys
from PySide2.QtWidgets import *
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtUiTools import QUiLoader

# print(dir(QtWidgets))
 
class UISample(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(UISample, self).__init__(parent)
        self.setWindowTitle('PySide')
        self.setGeometry(300, 50, 400, 350)
        self.resize(400, 300)
        self.QAbstractButton('test', self)
 
 
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    a = UISample()
    a.show()
    sys.exit(app.exec_())