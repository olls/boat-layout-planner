import sys
import random
import time
from xml.dom.minidom import parse
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

        newAction = QtGui.QAction('New', self)
        newAction.setShortcut('Ctrl+N')
        newAction.setStatusTip('Create a new blank boat.')
        newAction.triggered.connect(self.new)

        openAction = QtGui.QAction('Open', self)
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('Open a saved boat layout file.')
        openAction.triggered.connect(self.open)

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

        def callbackFactory(n):
            return lambda: self.boat.addFurniture(n)

        for name in self.boat.furniture.keys():
            action = QtGui.QAction(name, self)
            action.setStatusTip('Add a '+str(name))
            if name is not 'wall':
                action.triggered.connect(callbackFactory(name))
            else:
                action.triggered.connect(self.boat.addWall)
            addItems.addAction(action)

    def new(self):
        if QtGui.QMessageBox.question(self, 'Save Changes?',
           "<center>Do you want to save your changes to the boat?</center>",
           QtGui.QMessageBox.Yes | QtGui.QMessageBox.No,
           QtGui.QMessageBox.Yes) == QtGui.QMessageBox.Yes:
            if not self.save(type_='XML'):
                return False

        self.newBoat()

    def newBoat(self, length=20, width=2, height=3, stern=2.5, bow=2,
                wallWidth=0.1, description='Dvbris', author='Unknown',
                color='#000000'):
        try:
            self.boat.removeAll()
        except AttributeError:
            pass # self.boat must not exist yet.

        self.boat = items.boat.Boat(self.canvas, length=length, width=width,
            height=height, stern=stern, bow=bow, wallWidth=wallWidth,
            description=description, author=author, color=color)

        self.canvas.setBoat(self.boat)
        self.boat.redrawAll()

    def open(self):
        xml = self.openFile()
        if not xml:
            return False
        else:
            try:
                boat = xml.getElementsByTagName('boat')[0]
            except IndexError:
                QtGui.QMessageBox.question(self, 'Error',
                    '<center>Error while opening.<br>The file you tried to open is not a vaild BTL file.</center>',
                    QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
                return False

            bAt = boat.attributes
            self.newBoat(length=bAt['length'].value, width=bAt['width'].value,
                height=bAt['height'].value, stern=bAt['stern'].value,
                bow=bAt['bow'].value, wallWidth=bAt['wallWidth'].value,
                description=bAt['description'].value,
                author=bAt['author'].value, color=bAt['color'].value)

            for child in boat.childNodes:
                name = child.tagName
                self.boat.addFurniture(name, attrs = {'x': child.attributes['x'].value,
                                                      'y': child.attributes['y'].value,
                                                      'scale': child.attributes['scale'].value,
                                                      'angle': child.attributes['angle'].value,
                                                      'description': child.attributes['description'].value,
                                                      'color': child.attributes['color'].value})

    def openFile(self):
        type_ = 'BTL'.lower()
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Open file', expanduser('~'), '*.{}'.format(type_))

        if filename:
            if not str(filename)[-4:].lower() == '.'+type_:
                QtGui.QMessageBox.question(self, 'Error',
                    '<center>File not a {} file.</center>'.format(type_),
                    QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
                return False
            else:
                try:
                    data = parse(filename)
                except:
                    QtGui.QMessageBox.question(self, 'Error',
                        '<center>Error while opening.<br>This could be due to not having permission<br>or using an invalid filename.</center>',
                        QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
                    return False
                print(data.toprettyxml())
                self.statusBar().showMessage('Opened successfully.')
                return data
        else:
            self.statusBar().showMessage('Opening Canceled')
            return False

    def save(self, type_='XML'):
        if type_ == 'XML':
            data = self.boat.generateAllXML()
            type_ = 'BTL'
        elif type_ == 'SVG':
            data = self.boat.generateAllSVG()
        else:
            return False

        type_ = type_.lower()
        filename = QtGui.QFileDialog.getSaveFileName(self, 'Save {} File'.format(type_),
                                                     expanduser("~"), '*.{}'.format(type_))
        if filename:
            if not str(filename).endswith(('.'+type_.lower(), '.'+type_.upper())):
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


def main():
    app = QtGui.QApplication(sys.argv)
    win = BoatPlanner()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()