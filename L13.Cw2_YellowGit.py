import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from random import randint
from PIL import Image, ImageDraw
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtGui import QPixmap



class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.flag = False
        self.cir = []
        self.pushButton.clicked.connect(self.run)
    
    def run(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            qp.setPen(QColor(255, 255, 0))
            #qp.setBrush(QColor(255, 255, 0))
            h = randint(10, 100)
            self.cir.append([randint(0, 800), randint(0, 800), h, h])
            for i in self.cir:
                qp.drawEllipse(i[0], i[1], i[2], i[2]) 



if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())