import sys
import random
import time
from os.path import expanduser
from PyQt4 import QtGui

import isometric
import layout
import items.furniture
import items.boat

class BoatPlanner(QtGui.QMainWindow):
    """
        The main window which holds the canvas and tool-bars.
    """

    def __init__(self, ppm=100):
        super(BoatPlanner, self).__init__()

        self.ppm = ppm # Pixels per Meter at Scale = 1
        self.scale = .5

        self.canvas = layout.Canvas(self.scale, self.ppm)

        self.boat = None
        self.newBoat()
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

        newAction = QtGui.QAction('Open', self)
        newAction.setShortcut('Ctrl+O')
        newAction.setStatusTip('Open a saved boat layout file.')
        newAction.triggered.connect(lambda: self.open(self.statusBar))

        openAction = QtGui.QAction('New', self)
        openAction.setShortcut('Ctrl+N')
        openAction.setStatusTip('Create a new blank boat.')
        openAction.triggered.connect(self.new)

        saveXMLAction = QtGui.QAction('Save', self)
        saveXMLAction.setShortcut('Ctrl+S')
        saveXMLAction.setStatusTip('Save file for editing later.')
        saveXMLAction.triggered.connect(lambda: self.save(type_='XML'))

        saveSVGAction = QtGui.QAction('Export Image', self)
        saveSVGAction.setShortcut('Ctrl+Shift+S')
        saveSVGAction.setStatusTip('Export file for viewing in external programs.')
        saveSVGAction.triggered.connect(lambda: self.save(type_='SVG'))

        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)
        fileMenu.addAction(saveXMLAction)
        fileMenu.addAction(openAction)
        fileMenu.addAction(newAction)

        toolbar = self.addToolBar('menu')
        toolbar.addAction(exitAction)
        toolbar.addAction(isoAction)
        toolbar.addAction(saveXMLAction)
        toolbar.addAction(saveSVGAction)


        # Controls
        zoomInAction = QtGui.QAction('Zoom In', self)
        zoomInAction.setShortcut('Up')
        zoomInAction.setStatusTip('Zoom In (Up)')
        zoomInAction.triggered.connect(lambda: self.zoom(True))

        zoomOutAction = QtGui.QAction('Zoom Out', self)
        zoomOutAction.setShortcut('Down')
        zoomOutAction.setStatusTip('Zoom Out (Down)')
        zoomOutAction.triggered.connect(lambda: self.zoom(False))

        turnCWAction = QtGui.QAction('Rotate CW', self)
        turnCWAction.setShortcut('Left')
        turnCWAction.setStatusTip('Zoom In (Left)')
        turnCWAction.triggered.connect(lambda: self.rotate(True))

        turnCCWAction = QtGui.QAction('Rotate CCW', self)
        turnCCWAction.setShortcut('Right')
        turnCCWAction.setStatusTip('Zoom Out (Right)')
        turnCCWAction.triggered.connect(lambda: self.rotate(False))

        toolbar = self.addToolBar('controls')
        toolbar.addAction(zoomInAction)
        toolbar.addAction(zoomOutAction)
        toolbar.addAction(turnCWAction)
        toolbar.addAction(turnCCWAction)


        self.setUpItemsToolbar()

        self.setWindowTitle('Boat Layout Planner')
        self.showMaximized()

    def setUpItemsToolbar(self):
        addItems = self.addToolBar('items')

        for name in self.boat.furniture.keys():
            action = QtGui.QAction(name, self)
            action.setStatusTip('Add a '+str(name))
            action.triggered.connect(lambda: self.boat.addFurniture(name))
            addItems.addAction(action)

    def new(self):
        if QtGui.QMessageBox.question(self, 'Save Changes?',
           "<center>Do you want to save your changes to the boat?</center>",
           QtGui.QMessageBox.Yes | QtGui.QMessageBox.No,
           QtGui.QMessageBox.Yes) == QtGui.QMessageBox.Yes:
            if not self.save(type_='XML'):
                return False

        self.newBoat()

    def newBoat(self, length=20, width=2, stern=2.5, bow=2, description='Dvbris'):
        try:
            self.boat.removeAll()
        except AttributeError:
            pass # self.boat must not exist yet.

        self.boat = items.boat.Boat(self.canvas, length=length, width=width,
                        stern=stern, bow=bow, description=description)

        self.canvas.setBoat(self.boat)
        self.boat.redrawAll()


    def isoView(self):
        """ Opens the isometric 3D view window. """

        # Open the 3D view with a temporary random length,
        #   and position it in the center of this window.
        self.win = isometric.Boat3D(self.boat, self.frameGeometry().center())
        self.win.show()

    def zoom(self, dirc):
        """ Scales the canvas. """

        if dirc:
            self.canvas.zoomIn()
        else:
            self.canvas.zoomOut()
        self.boat.redrawAll()

    def rotate(self, dirc):
        """ Rotates the canvas. """

        if dirc:
            self.canvas.rotate(10)
        else:
            self.canvas.rotate(-10)
        self.boat.redrawAll()

    def save(self, type_='XML'):
        if type_ == 'XML':
            data = self.boat.generateAllXML()
        elif type_ == 'SVG':
            data = self.boat.generateAllSVG()
        else:
            return False

        type_ = type_.lower()
        filename = QtGui.QFileDialog.getSaveFileName(self, 'Save {} File'.format(type_),
                                                     expanduser("~"), '*.{}'.format(type_))
        if filename:
            if not str(filename)[-4:].lower() == '.'+type_:
                filename += '.'+type_
            try:
                with open(filename, 'w') as f:
                    f.write(data)
                self.statusBar().showMessage('Saved \'{}\' successfully.'
                                        .format(filename))
            except IOError:
                QtGui.QMessageBox.question(self, 'Error',
                    "<center>Error while saving.<br>This could be due to not having permission<br>or using an invalid filename.</center>",
                    QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
        else:
            self.statusBar().showMessage('Saving Canceled')
            return False
        return True


def main():
    app = QtGui.QApplication(sys.argv)
    win = BoatPlanner()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()