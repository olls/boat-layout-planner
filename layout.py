import sys
from PyQt4 import QtGui

class Canvas(QtGui.QGraphicsView):
    """
        This widget the interactive canvas which the layout is created.
    """

    def __init__(self):
        super(Canvas, self).__init__()

        self.scene = QtGui.QGraphicsScene(self)
        self.setScene(self.scene)

def main():
    app = QtGui.QApplication(sys.argv)
    win = Canvas()
    win.showMaximized()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()