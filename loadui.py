#打包 pyinstaller loadui.py --noconsole --hidden-import PySide2.QtXml
from PySide2 import QtCore
from PySide2.QtCore import QFile
from PySide2.QtUiTools import *
from PySide2.QtWidgets import *


def onclick():
    print("click")

QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
app = QApplication([])

win=QUiLoader().load(QFile("untitled.ui"))

win.show()
app.exec_()