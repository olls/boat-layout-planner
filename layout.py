import sys
from PyQt4 import QtGui, QtCore

class Canvas(QtGui.QGraphicsView):
    """
        This widget the interactive canvas which the layout is created.
    """
    def __init__(self):
        super(Canvas, self).__init__()

        self.scene = QtGui.QGraphicsScene(self)
        self.setScene(self.scene)

    def update(self, item):
        """ This method allows you to add a Item 
            (From the items module.) to the canvas. """
        # First generate the vector information for that item.
        vectorItems = item.generateVectors()
        # Then for each vector, find the type and create the Qitems for it.
        for item in vectorItems:
            if item[0] == 'line':
                Qitem = QtCore.QLineF(float(item[1]['x1']),
                                      float(item[1]['y1']),
                                      float(item[1]['x2']),
                                      float(item[1]['y2']))
            self.scene.addLine(Qitem)

def main():
    app = QtGui.QApplication(sys.argv)
    win = Canvas()
    win.showMaximized()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()