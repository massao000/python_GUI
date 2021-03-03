# import sys
# import 
from PySide2 import sys
from PySide2 import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
# from PySide2.QtGui import *
# from PySide2 import QtCore, QtGui, QtWidgets, QtQuickWidgets
# from PySide2.QtUiTools import QUiLoader

# print(dir(PySide2.QtWidgets))
# class UISample(QtWidgets.QMainWindow):
#     def __init__(self, parent=None):
#         super(UISample, self).__init__(parent)

# 今回はQGridLayoutでグリッド分けをしているほかには{move}で細かくできる
class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PySide')
        # self.setGeometry(0, 300, 300, 0)
        self.resize(400, 300)
        self.widget()
        # self.text()
        
    def widget(self):
        title = QLabel('▼表示テキストの入力▼', self)
        # title.move(0,0)
        self.titleEdit = QLineEdit()

        self.btn = QPushButton("実行", self)
        # ボタンがclickされたときの処理
        self.btn.clicked.connect(self.button_click)
        self.change_text = QLabel('ここの文字が変わります', self)

        self.check_btn = QCheckBox("チェックボックス->")
        # ボタンがclickされたときの処理
        self.check_btn.stateChanged.connect(self.change_on)
        self.change_text_box = QLabel('OFF')

        self.btn_pop = QPushButton("pop", self)
        # ボタンがclickされたときの処理
        self.btn_pop.clicked.connect(self.pop)


        self.file_selection = QLabel('ファイル選択')
        self.open_file = QPushButton("ファイル選択", self)
        self.open_file.clicked.connect(self.open_file_menu)
        self.file = QLineEdit()
        # self.file.setEnabled(False) # 書き込みを禁止できる

        self.file_pop = QPushButton("ファイルパス表示", self)
        self.file_pop.clicked.connect(self.file_check_pop)

        li = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        self.combo = QComboBox(self)
        self.combo.setEditable(True)
        self.combo.addItems(li)
        self.combo.currentIndex()
        # self.combo.setCurrentIndex(self.combo.currentIndex())
        # self.combo.setCurrentText('コンボックス')
        # self.combo.setItemText(self.combo, 'コンボックス')
        # self.combo.writeText('コンボックス')

        self.listbox = QListWidget()
        self.listbox.addItems(li)
        # self.listbox.insertItem(0, 'aa')

        self.tab_text1 = QLabel('タブ1')
        self.tab_text2 = QLabel('タブ2')
        self.tab = QTabWidget()
        self.tab.addTab(self.tab_text1, 'T2')
        self.tab.addTab(self.tab_text2, 'T1')
        
        self.grid = QGridLayout()
        self.grid.addWidget(title, 0,0)
        self.grid.addWidget(self.titleEdit, 1,0)
        self.grid.addWidget(self.btn, 1,1)
        self.grid.addWidget(self.change_text, 2,0)
        self.grid.addWidget(self.check_btn, 3,0)
        self.grid.addWidget(self.change_text_box, 3,1)
        self.grid.addWidget(self.btn_pop, 4,0)
        self.grid.addWidget(self.file_selection, 5,0)
        self.grid.addWidget(self.file, 5,1)
        self.grid.addWidget(self.open_file, 5,3)
        self.grid.addWidget(self.file_pop, 6,0)
        self.grid.addWidget(self.combo, 7,0)
        self.grid.addWidget(self.listbox, 7,1)
        self.grid.addWidget(self.tab, 7,3)
        self.setLayout(self.grid)

    def button_click(self):
        self.change_text.setText(self.titleEdit.text())

    def pop(self):
        reply = QMessageBox.information(self, "popup表示", 'ポップアップの表示', QMessageBox.Ok)

    def change_on(self, state):
        if Qt.Checked == state:
            self.change_text_box.setText('ON')
        else:
            self.change_text_box.setText('OFF')

    def open_file_menu(self):
        directory = QFileDialog.getOpenFileName()
        self.file.setText(f'{directory[0]}')
        # print(directory[0])
    
    def file_check_pop(self):
        # print(self.file.text())
        if  self.file.text() != '':
            reply = QMessageBox.information(self, "popup表示", self.file.text(), QMessageBox.Ok)
        else:
            reply = QMessageBox.information(self, "popup表示", "何も選択されていない", QMessageBox.Ok)
            

if __name__ == '__main__':
    app = QApplication(sys.argv)
    windows = Demo()
    windows.show()
    sys.exit(app.exec_())

    # 978179889