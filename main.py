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

    def __init__(self):
        super(BoatPlanner, self).__init__()

        self.canvas = layout.Canvas()
        self.boat = items.boat.Boat(self.canvas, length=random.randint(200, 1000),
                               description='My long Boat.')

        self.initUI()

        # Temp test of adding items.
        chair = items.furniture.Furniture(self.canvas, 'chair', x=100, y=100, 
                                    scale=1.5, description='My Seat')

        chair1 = items.furniture.Furniture(self.canvas, 'chair', x=100, y=100, 
                                     scale=1.5, description='My Seat')
        chair1.setX(300)
        chair1.setY(300)
        chair1.setScale(8)

    def initUI(self):
        self.setCentralWidget(self.canvas)

        self.statusBar()
        menubar = self.menuBar()

        exitAction = QtGui.QAction('&Exit', self)
        exitAction.setShortcut('Ctrl+D')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        isoAction = QtGui.QAction('&3D View', self)
        isoAction.setStatusTip('View an isometric image of the boat.')
        isoAction.triggered.connect(self.isoView)

        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(isoAction)
        fileMenu.addAction(exitAction)

        toolbar = self.addToolBar('menu')
        toolbar.addAction(exitAction)
        toolbar.addAction(isoAction)

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
        self.win = isometric.Boat3D(self.boat.attrs['length'], 
                                    self.frameGeometry().center())
        self.win.show()

def main():
    app = QtGui.QApplication(sys.argv)
    win = BoatPlanner()
    win.showMaximized()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()