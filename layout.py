import sys
from PyQt4 import QtGui, QtCore

class Canvas(QtGui.QGraphicsView):
    def __init__(self):
        super(Canvas, self).__init__()

        self.scene = QtGui.QGraphicsScene(self)
        self.setScene(self.scene)

        self.item = QtGui.QGraphicsEllipseItem(0, 0, 50, 50)
        self.scene.addItem(self.item)

def main():
    app = QtGui.QApplication(sys.argv)
    win = Canvas()
    win.showMaximized()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()