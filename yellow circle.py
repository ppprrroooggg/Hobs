from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication
from PyQt5 import uic
import sys
from random import randint
from PyQt5.QtGui import QPainter, QColor
from random import randint
from UI import Ui_MainWindow


class YellowCircles(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.update)
        self.drawing = True

    def paintEvent(self, event):
        if self.drawing:
            qp = QPainter()
            qp.begin(self)
            qp.setPen(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            self.draw(qp)
            qp.end()

    def draw(self, qp):
        s = randint(30, 300)
        f = randint(30, 300)
        qp.drawEllipse(s, s, s + f, s + f)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = YellowCircles()
    ex.show()
    sys.exit(app.exec_())
