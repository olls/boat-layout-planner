import sys
from PyQt4 import QtGui, QtCore

class Canvas(QtGui.QGraphicsView):
    """
        This widget is the interactive canvas which the layout is
            created on.
    """

    def __init__(self, scale, ppm):
        super(Canvas, self).__init__()

        # Some scaling values.
        self.ppm = ppm
        self.scale(scale*ppm, scale*ppm)

        # Create the scene.
        self.scene = QtGui.QGraphicsScene(self)
        self.setScene(self.scene)

    def setBoat(self, boat):
        self.boat = boat

    def zoomIn(self):
        self.scale(1.1, 1.1)

    def zoomOut(self):
        self.scale(.9, .9)
