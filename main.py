import sys
import random
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor


class MyWidget(QMainWindow):
    def __init__(self):
        self.do_paint = False
        self.w = 1
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.qw.clicked.connect(self.run)

    def run(self):
        self.w = random.randint(5, 100)
        self.do_paint = True
        self.update()

    def paintEvent(self, event):
        if self.do_paint:
            # print(1)
            # return 0
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp, self.w)
            qp.end()
        self.do_paint = False

    def draw_flag(self, qp, w):
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(0, 0, w, w)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())