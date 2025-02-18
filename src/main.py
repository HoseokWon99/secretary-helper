import sys
from PyQt6.QtWidgets import *
from src.view import Form

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Form()
    win.show()
    app.exec()
