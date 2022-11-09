from PyQt5 import QtWidgets
from PyQt5.QtWidgets import  QApplication, QMainWindow

import sys

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle('Easy programm')
        self.setGeometry(300, 250, 350, 200)

        self.new_t = QtWidgets.QLabel(self)

        self.main_text = QtWidgets.QLabel(self)
        self.main_text.setText('It is a base text')
        self.main_text.move(100, 100)
        self.main_text.adjustSize()

        self.btn = QtWidgets.QPushButton(self)
        self.btn.move(70, 150)
        self.btn.clicked.connect(self.click_add_lab)
        self.btn.setText('Click me')
        self.btn.adjustSize()


    def click_add_lab(self):
        self.new_t.setText('Second text')
        self.new_t.move(100, 50)
        self.new_t.adjustSize()

def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    application()