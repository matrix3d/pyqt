# https://www.youtube.com/watch?v=OZ3MBmuJ5bg&list=PL0uF99K6uCYPp2hv99pcUPpkUtiDWjGdW&index=9
from PySide2 import QtCore
from PySide2.QtCore import Qt,QUrl
from PySide2.QtWidgets import *


def onclick():
    print("click")


QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
app = QApplication([])
win = QMainWindow()
win.resize(800, 600)

btn = QPushButton("my", win)
btn.setAcceptDrops(True)


def dragEnterEvent(event):
    if event.mimeData().hasUrls:
        event.accept()
    else:
        event.ignore()

def dragMoveEvent(event):
    if event.mimeData().hasUrls:
        event.setDropAction(Qt.CopyAction)
        event.accept()
    else:
        event.ignore()

def dropEvent(event):
    if event.mimeData().hasUrls:
        event.setDropAction(Qt.CopyAction)
        event.accept()
        print(event.mimeData().urls())
    else:
        event.ignore()


btn.dragEnterEvent = dragEnterEvent
btn.dragMoveEvent=dragMoveEvent
btn.dropEvent=dropEvent

btn.clicked.connect(onclick)
btn.clicked.connect(onclick)

win.show()
app.exec_()
