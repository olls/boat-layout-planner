import sys
import random
from PyQt4 import QtGui

import isometric
import layout
import items.item
import items.furniture
import items.boat

class BoatPlanner(QtGui.QMainWindow):
    """
        The main window which holds the canvas and tool-bars.
    """

    def __init__(self, scale=1, ppm=100):
        super(BoatPlanner, self).__init__()

        self.scale = scale
        self.ppm = ppm # Pixels per Meter at Scale = 1

        self.canvas = layout.Canvas(self.scale, self.ppm)
        self.boat = items.boat.Boat(self.canvas, length=20, stern=2, bow=3,
                               description='My long Boat.')
        self.initUI()

    def initUI(self):
        self.setCentralWidget(self.canvas)

        self.statusBar()
        menubar = self.menuBar()

        exitAction = QtGui.QAction('&Exit', self)
        exitAction.setShortcut('Ctrl+D')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        isoAction = QtGui.QAction('&3D View', self)
        isoAction.setShortcut('Ctrl+V')
        isoAction.setStatusTip('View an isometric image of the boat.')
        isoAction.triggered.connect(self.isoView)

        zoomInAction = QtGui.QAction('Zoom In', self)
        zoomInAction.setShortcut('Ctrl++')
        zoomInAction.setStatusTip('Zoom In (Ctrl++)')
        zoomInAction.triggered.connect(lambda: self.zoom(True))

        zoomOutAction = QtGui.QAction('Zoom Out', self)
        zoomOutAction.setShortcut('Ctrl+-')
        zoomOutAction.setStatusTip('Zoom Out (Ctrl+-)')
        zoomOutAction.triggered.connect(lambda: self.zoom(False))

        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(isoAction)
        fileMenu.addAction(exitAction)

        toolbar = self.addToolBar('menu')
        toolbar.addAction(exitAction)
        toolbar.addAction(isoAction)
        toolbar.addAction(zoomInAction)
        toolbar.addAction(zoomOutAction)

        self.setUpItemsToolbar()

        self.setWindowTitle('Boat Layout Planner')

    def setUpItemsToolbar(self):
        addItems = self.addToolBar('items')

        for name in self.boat.furniture.keys():
            action = QtGui.QAction(name, self)
            action.setStatusTip('Add a '+str(name))
            action.triggered.connect(lambda: self.boat.addFurniture(name))
            addItems.addAction(action)


    def isoView(self):
        """ Opens the isometric 3D view window. """

        # Open the 3D view with a temporary random length, 
        #   and position it in the center of this window.
        self.win = isometric.Boat3D(self.boat, self.frameGeometry().center())
        self.win.show()

    def zoom(self, dir):
        """ Increases the scale in the canvas. """

        if dir:
            self.canvas.zoomIn()
        else:
            self.canvas.zoomOut()
        self.boat.updateAll()

def main():
    app = QtGui.QApplication(sys.argv)
    win = BoatPlanner()
    win.showMaximized()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()