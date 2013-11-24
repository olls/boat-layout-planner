import sys
from PyQt4 import QtGui, QtCore

import items.item
from items.templates import TEMPLATES


class Boat(items.item.Item):
    
    def __init__(self, canvas, length=20, width=2, height=3, bow=3, stern=4, 
                 wallWidth=0.1, color='#000000', description='', 
                 author='Unknown'):
        super(Boat, self).__init__()

        self.items = []

        self.canvas = canvas

        self.attrs = {}
        self._setName('boat')
        self._setLength(length)
        self._setWidth(width)
        self._setHeight(height)
        self._setBow(bow)
        self._setStern(stern)
        self._setWallWidth(wallWidth)
        self._setX(0)
        self._setY(0)
        self._setColor(color)
        self._setDescription(description)
        self._setAuthor(author)

        self.canvas.scene.addItem(self)

        self.setToolTip(str(self.attrs['description']))

        # Create QItems
        self.redraw()
        # self.canvas.fitInView(self)


    def addFurniture(self, name):
        self.items.append(items.furniture.Furniture(self.canvas, name))

    def addWall(self):
        self.items.append(items.furniture.Wall(self.canvas))

    @property
    def furniture(self):
        return TEMPLATES['furniture']

    def redrawAll(self):
        self.redraw()
        for item in self.items:
            item.redraw()


    def _setLength(self, length):
        try:
            self.attrs['length'] = float(length)
        except ValueError:
            sys.exit('Fatal error: Invalid length attribute for Boat item')
    def setLength(self, length):
        self._setWidth(length)
        self.redraw()

    def _setWidth(self, width):
        try:
            self.attrs['width'] = float(width)
        except ValueError:
            sys.exit('Fatal error: Invalid width attribute for Boat item')
        if self.attrs['width'] < 0:
            sys.exit('Fatal error: Invalid width attribute for Boat item')
    def setWidth(self, width):
        self._setWidth(width)
        self.redraw()
        self.redraw()

    def _setHeight(self, height):
        try:
            self.attrs['height'] = float(height)
        except ValueError:
            sys.exit('Fatal error: Invalid height attribute for Boat item')
        if self.attrs['height'] < 0:
            sys.exit('Fatal error: Invalid height attribute for Boat item')
    def setWallWidth(self, height):
        self._setHeight(height)
        self.redraw()

    def _setBow(self, bow):
        try:
            self.attrs['bow'] = float(bow)
        except ValueError:
            sys.exit('Fatal error: Invalid bow attribute for Boat item')
        if self.attrs['bow'] > self.attrs['length']:
            sys.exit('Fatal error: Invalid bow attribute for Boat item')
    def setBow(self, bow):
        self._setBow(bow)
        self.redraw()

    def _setStern(self, stern):
        try:
            self.attrs['stern'] = float(stern)
        except ValueError:
            sys.exit('Fatal error: Invalid stern attribute for Boat item')
        if self.attrs['stern'] > (self.attrs['length'] - self.attrs['bow']):
            sys.exit('Fatal error: Invalid stern attribute for Boat item')
    def setStern(self, stern):
        self._setStern(stern)
        self.redraw()

    def _setWallWidth(self, wallWidth):
        try:
            self.attrs['wallWidth'] = float(wallWidth)
        except ValueError:
            sys.exit('Fatal error: Invalid wallWidth attribute for Boat item')
        if self.attrs['wallWidth'] > (self.attrs['length'] / 2):
            sys.exit('Fatal error: Invalid wallWidth attribute for Boat item')
    def setWallWidth(self, stern):
        self._setStern(stern)

    def _setAuthor(self, author):
        self.attrs['author'] = author
    def setAuthor(self, author):
        self._setAuthor(author)
        self.redraw()