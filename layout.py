import sys
from PyQt4 import QtGui

class Canvas(QtGui.QGraphicsView):
    """
        This widget the interactive canvas which the layout is created.
    """

    def __init__(self, scale, ppm):
        super(Canvas, self).__init__()

        self.ppm = ppm
        self.scale(scale*ppm, scale*ppm)

        self.scene = QtGui.QGraphicsScene(self)
        self.setScene(self.scene)

    def zoomIn(self):
        self.scale(1.1, 1.1)

    def zoomOut(self):
        self.scale(.9, .9)

def main():
    app = QtGui.QApplication(sys.argv)
    win = Canvas()
    win.showMaximized()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()