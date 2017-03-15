# !/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'LH LIU'
import sys
from PyQt5 import Qt, QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMenuBar, QStatusBar, QWidget, QGraphicsView, QSlider
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsItem
from PyQt5.QtGui import QPixmap


class Painter(QGraphicsItem):
    def __init__(self):
        super(Painter, self).__init__()

        self.dots = []
        self.moving_dot = None

    def set_dot(self, x, y):
        self.dots.append([x, y])

    def set_moving_dot(self, x, y):
        self.moving_dot = (x, y)

    def paint(self, painter, option, widget):
        # painter.setPen(Qt.black)
        for dot in self.dots:
            x, y = dot[0], dot[1]
            painter.drawLine(x, y, 2 + x, 2 + y)
            painter.drawLine(x, 2 + y, 2 + y, y)

        for i in range(1, len(self.dots)-1):
            x1, y1 = self.dots[i-1]
            x2, y2 = self.dots[i]
            painter.drawLine(x1 + 1, y + 1, x2 + 1, y2 + 1)

    def reset(self):
        self.dots = []
        self.moving_dot = None

        self.update()

    # defs from super class
    def boundingRect(self):
        return QtCore.QRectF(0, 0, 512, 512)

    def mousePressEvent(self, event):
        pos = event.pos()
        self.set_dot(pos.x(), pos.y())
        self.moving_dot = None
        self.update()

        super(Painter, self).mousePressEvent(event)


class Image_View(QGraphicsView):
    def __init__(self, centralwidget):
        super(Image_View, self).__init__(centralwidget)

        self.scene = QGraphicsScene()
        self.pixmap = QPixmap()
        self.painter = Painter()

        self.setup_ui()

    def setup_ui(self):
        # GraphicsItem
        self.scene.addPixmap(self.pixmap)
        self.scene.addItem(self.painter)

        self.setScene(self.scene)
        self.setCacheMode(QGraphicsView.CacheBackground)

    # defs from super class
    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_R:
            self.painter.reset()


class Main_Window(QMainWindow):
    def __init__(self):
        super(Main_Window, self).__init__()

        self.menubar = QMenuBar(self)
        self.statusbar = QStatusBar(self)
        self.centralwidget = QWidget(self)
        self.image_view = Image_View(self.centralwidget)
        self.horizontal_slider = QSlider(self.centralwidget)

        self.setup_ui()

    def setup_ui(self):
        # 1. self info
        self.setObjectName("Demo_1")
        self.resize(800, 600)

        # 2.1 sub widgets
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)

        # 2.2
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        # 2.3
        self.centralwidget.setObjectName("centralwidget")
        self.setCentralWidget(self.centralwidget)

        self.image_view.setGeometry(QtCore.QRect(144, 10, 512, 512))
        self.image_view.setObjectName("image_view")

        self.horizontal_slider.setGeometry(QtCore.QRect(144, 530, 512, 22))
        self.horizontal_slider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontal_slider.setObjectName("horizontal_slider")

        # 3 signals and slots
        self.horizontal_slider.valueChanged['int'].connect(self.image_view.repaint)


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)

    main_window = Main_Window()
    main_window.show()

    sys.exit(app.exec_())


