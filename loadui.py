#打包 pyinstaller loadui.py --noconsole --hidden-import PySide2.QtXml
#https://zhuanlan.zhihu.com/p/390192953
from PySide2 import QtCore
from PySide2.QtCore import QFile
from PySide2.QtUiTools import *
from PySide2.QtWidgets import *


def read_qss_file(qss_file_name):
    with open(qss_file_name, 'r', encoding='UTF-8') as file:
        return file.read()
def onclick():
    print("click")

QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
app = QApplication([])

win=QUiLoader().load(QFile("untitled.ui"))
#app.setStyleSheet(read_qss_file("qdarkstyle/light/style.qss"))

win.show()
app.exec_()