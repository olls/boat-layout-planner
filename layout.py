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

    def update(self, vectorItems):
        """ This method allows you to add a Item 
            (From the items module.) to the canvas. 
            It returns the group of Qitems 
            that make up the item. """

        # Then for each vector, find the type and create the Qitems for it.
        Qitems = []
        for item in vectorItems:
            if item[0] == 'line':
                Qitems.append(
                    self.scene.addLine(
                        QtCore.QLineF(float(item[1]['x1']),
                                      float(item[1]['y1']),
                                      float(item[1]['x2']),
                                      float(item[1]['y2']))
                    )
                )
        # Store all the Qitems in a group so they behave as one item.
        group = self.scene.createItemGroup(Qitems)
        group.setFlag(QtGui.QGraphicsItem.ItemIsMovable)

        self.centerOn(group)

        return group

    def delete(self, group):
        """ Remove the group from the canvas """
        self.scene.removeItem(group)

def main():
    app = QtGui.QApplication(sys.argv)
    win = Canvas()
    win.showMaximized()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()