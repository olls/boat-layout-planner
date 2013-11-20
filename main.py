import sys
import random
from PyQt4 import QtGui, QtCore

import isometric
import layout
import items

class BoatPlanner(QtGui.QMainWindow):
    """
        The main window which holds the canvas and tool-bars.
    """

    def __init__(self):
        super(BoatPlanner, self).__init__()

        self.canvas = layout.Canvas()

        self.initUI()

        # Temp test of adding items.
        chair1 = items.Furniture('chair', 100, 100, 1.5, 0, 
                                 'My Seat', '#000000')
        self.canvas.update(chair1)
        chair1.setX(300)
        chair1.setY(300)
        chair1.setScale(8)
        self.canvas.update(chair1)

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

        toolbar = self.addToolBar('File')
        toolbar.addAction(exitAction)
        toolbar.addAction(isoAction)

        self.setWindowTitle('Boat Layout Planner')

    def isoView(self):
        """ Opens the isometric 3D view window. """

        # Open the 3D view with a temporary random length, 
        #   and position it in the center of this window.
        self.win = isometric.Boat3D(random.randint(0, 300), 
                                    self.frameGeometry().center())
        self.win.show()

def main():
    app = QtGui.QApplication(sys.argv)
    win = BoatPlanner()
    win.showMaximized()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()