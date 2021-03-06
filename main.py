import sys
import random
import time
from xml.dom.minidom import parse
from os.path import expanduser
from PyQt4 import QtGui, QtCore

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
        """
            Define the layout of the program and all the tool-bar
                buttons.
        """

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

        saveXMLBackupAction = QtGui.QAction('Backup', self)
        saveXMLBackupAction.setStatusTip('Save a backup of the file for editing later.')
        saveXMLBackupAction.triggered.connect(lambda: self.save(type_='XML'))

        saveSVGAction = QtGui.QAction('Export Image', self)
        saveSVGAction.setShortcut('Ctrl+Shift+S')
        saveSVGAction.setStatusTip('Export file for viewing in external programs.')
        saveSVGAction.triggered.connect(lambda: self.save(type_='SVG'))

        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)
        fileMenu.addAction(saveXMLAction)
        fileMenu.addAction(saveXMLBackupAction)
        fileMenu.addAction(openAction)
        fileMenu.addAction(newAction)

        toolbar = self.addToolBar('menu')
        toolbar.addAction(exitAction)
        toolbar.addAction(isoAction)
        toolbar.addAction(saveXMLAction)
        toolbar.addAction(saveXMLBackupAction)
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
        """
            Add all the buttons to the tool-bar for the different
                furniture items.
        """
        addItems = self.addToolBar('items')

        def callbackFactory(n):
            return lambda: self.boat.addFurniture(n)

        for name in self.boat.furniture.keys():
            pretty_name = ' '.join(name.split('-'))
            pretty_name = pretty_name[0].upper() + pretty_name[1:]
            action = QtGui.QAction(pretty_name, self)
            action.setStatusTip('Add a ' + str(pretty_name))
            if not name == 'wall':
                action.triggered.connect(callbackFactory(name))
            else:
                action.triggered.connect(self.boat.addWall)
            addItems.addAction(action)

    def new(self):
        """
            Warn the user then reset the program with a new boat.
        """
        if QtGui.QMessageBox.question(self, 'Save Changes?',
           "<center>Do you want to save your changes to the boat?</center>",
           QtGui.QMessageBox.Yes | QtGui.QMessageBox.No,
           QtGui.QMessageBox.Yes) == QtGui.QMessageBox.Yes:
            if not self.save(type_='XML'):
                return False

        self.newBoat()

    def newBoat(self, length=20, width=2.5, height=3, bow=3, stern=3,
                 wallWidth=0.1, color='#000000', description='',
                 author='Unknown'):
        """
            Create a new boat.
        """

        # Clear the old boat.
        try:
            self.boat.removeAll()
        except AttributeError:
            pass # There must not be an old boat.

        self.boat = items.boat.Boat(self.canvas, length=length, width=width,
            height=height, stern=stern, bow=bow, wallWidth=wallWidth,
            description=description, author=author, color=color)

        self.canvas.setBoat(self.boat)
        self.boat.redrawAll()

    def open(self):
        """
           Load the boat data and use it to create a new boat.
        """
        xml = self.openFile()
        if not xml:
            return False
        else:
            try:
                boat = xml.getElementsByTagName('boat')[0]
            except IndexError:
                QtGui.QMessageBox.question(self, 'Error',
                    '<center>Error while opening.<br>The file you tried to open is not a valid BTL file.</center>',
                    QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
                return False

            bAt = boat.attributes
            self.newBoat(length=bAt['length'].value, width=bAt['width'].value,
                height=bAt['height'].value, stern=bAt['stern'].value,
                bow=bAt['bow'].value, wallWidth=bAt['wallWidth'].value,
                description=bAt['description'].value,
                author=bAt['author'].value, color=bAt['color'].value)

            # For every furniture item.
            for child in boat.childNodes:

                try:
                    name = child.tagName
                except AttributeError:
                    # Not a XML tag, ignore.
                    name = None

                if name == 'wall':
                    self.boat.addWall(
                        attrs = {
                            'x': child.attributes['x'].value,
                            'y': child.attributes['y'].value,
                            'doorY': child.attributes['doorY'].value,
                            'doorWidth': child.attributes['doorWidth'].value,
                            'scale': child.attributes['scale'].value,
                            'description': child.attributes['description'].value,
                            'color': child.attributes['color'].value
                        }
                    )
                elif name is not None:
                    self.boat.addFurniture(
                        name,
                        attrs = {
                            'x': child.attributes['x'].value,
                            'y': child.attributes['y'].value,
                            'scale': child.attributes['scale'].value,
                            'angle': child.attributes['angle'].value,
                            'description': child.attributes['description'].value,
                            'color': child.attributes['color'].value
                        }
                    )

    def openFile(self):
        """
            Display the open file dialog for the user to select a
                *.btl file and return the XML data.
        """
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
                        '<center>Error while opening.<br>This could be due to not having permission<br>or using an invalid file-name.</center>',
                        QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
                    return False
                self.statusBar().showMessage('Opened successfully.')
                return data
        else:
            self.statusBar().showMessage('Opening Cancelled')
            return False

    def save(self, type_='XML'):
        """
            Creates a save file dialogue for the user to select where
                to save the file, then it gets the XML/SVG data
                (type_ parameter), and saves it to the file.
        """
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
                    "<center>Error while saving.<br>This could be due to not having permission<br>or using an invalid file-name.</center>",
                    QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
        else:
            self.statusBar().showMessage('Saving Cancelled')
            return False
        return True

    def closeEvent(self, event):
        """
            Warns the user to save before closing the program.
        """
        reply = QtGui.QMessageBox.question(self, 'Quit?!',
            "<center>Are you sure you want to quit?<br>You will lose your work if you haven't saved it.</center>", QtGui.QMessageBox.Yes |
            QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def isoView(self):
        """
            Opens the isometric 3D view window.
        """

        # Open the 3D view with a temporary random length,
        #   and position it in the centre of this window.
        self.win = isometric.Boat3D(self.boat, self.frameGeometry().center())
        self.win.show()

    def zoom(self, dirc):
        """
            Scales the canvas in dirc.
        """

        if dirc:
            self.canvas.zoomIn()
        else:
            self.canvas.zoomOut()
        self.boat.redrawAll()

    def rotate(self, dirc):
        """
            Rotates the canvas in dirc.
        """

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