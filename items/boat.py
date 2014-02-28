import sys
from PyQt4 import QtGui, QtCore

import items.item
from items.templates import TEMPLATES
from func import *


class Boat(items.item.Item):

    def __init__(self, canvas, length=20, width=2, height=3, bow=3, stern=4,
                 wallWidth=0.1, color='#000000', description='',
                 author='Unknown'):
        super(Boat, self).__init__()

        self.items = []

        self.canvas = canvas

        self.editable = {
            'length':   'lineEdit',
            'width':    'lineEdit',
            'height':   'lineEdit',
            'bow':      'lineEdit',
            'stern':    'lineEdit',
            'wallWidth':'lineEdit',
            'author':   'lineEdit',
            'color':    'color'
        }

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

        # Create QItems
        self.redraw()
        # self.canvas.fitInView(self)


    def addFurniture(self, name, attrs=None):
        if attrs == None:
            self.items.append(items.furniture.Furniture(self.canvas, name,
                self.attrs['bow'] + self.attrs['wallWidth'], # X
                self.attrs['wallWidth'], # Y
                self.attrs['length'] - self.attrs['wallWidth'] - self.attrs['stern'], # X Limit
                self.attrs['width'] - self.attrs['wallWidth'] # Y Limit
            ))
        else:
            self.items.append(items.furniture.Furniture(self.canvas, name,
                float(attrs['x']), # X
                float(attrs['y']), # Y
                self.attrs['length'] - self.attrs['wallWidth'] - self.attrs['stern'], # X Limit
                self.attrs['width'] - self.attrs['wallWidth'], # Y Limit
                scale = float(attrs['scale']),
                angle = float(attrs['angle']),
                description = attrs['description'],
                color = attrs['color']
            ))

    def addWall(self, attrs=None):
        if not attrs:
            self.items.append(items.furniture.Wall(self.canvas,
                self.attrs['bow'] + self.attrs['wallWidth'], # X
                self.attrs['wallWidth'], # Y
                self.attrs['length'] - self.attrs['wallWidth'] - self.attrs['stern'], # X Limit
                self.attrs['width'] - self.attrs['wallWidth'] # Y Limit
            ))
        else:
            self.items.append(items.furniture.Wall(self.canvas,
                float(attrs['x']), # X
                float(attrs['y']), # Y
                self.attrs['length'] - self.attrs['wallWidth'] - self.attrs['stern'], # X Limit
                self.attrs['width'] - self.attrs['wallWidth'], # Y Limit
                doorY = float(attrs['doorY']),
                doorWidth = float(attrs['doorWidth']),
                scale = float(attrs['scale']),
                description = attrs['description'],
                color = attrs['color']
            ))

    @property
    def furniture(self):
        return TEMPLATES['furniture']

    def redrawAll(self):
        self.redraw()
        [item.redraw() for item in self.items]
    def updateAllPos(self):
        [item.updatePos() for item in self.items]

    def removeAll(self):
        self.canvas.scene.removeItem(self)
        [self.canvas.scene.removeItem(item) for item in self.items]

    def generateAllSVG(self):
        svg = (('<?xml version="1.0"?>\n'
                '<svg width="{length}" height="{width}" version="1.1" xmlns="http://www.w3.org/2000/svg">\n'
                '<text x="0" y="{width}" font-family="sans-serif" font-size="20px">{description}</text>\n')
                .format(length=(self.attrs['length']*100)+1, width=(self.attrs['width']*100)+1, description=self.attrs['description']) +
                '\n'.join([item.generateSVG(scale=100, noScale='stroke-width') for item in self.items] +
                          [self.generateSVG(scale=100, noScale='stroke-width')]) +
                '</svg>')
        svg = svg.replace('  ', ' ')
        return svg

    def generateAllXML(self):
        xml = ('<?xml version="1.0"?>\n' +
               self.generateXML()+'\n'+'\n\t'.join([item.generateXML() for item in self.items]) +'\n</boat>')
        xml = xml.replace('  ', ' ')
        return xml

    def updateAttr(self, attr, value):
        if attr == 'length': self.setLength(value)
        elif attr == 'width': self.setWidth(value)
        elif attr == 'height': self.setHeight(value)
        elif attr == 'bow': self.setBow(value)
        elif attr == 'stern': self.setStern(value)
        elif attr == 'wallWidth': self.setWallWidth(value)
        elif attr == 'x': self.setX(value)
        elif attr == 'y': self.setY(value)
        elif attr == 'color': self.setColor(value)
        elif attr == 'description': self.setDescription(value)
        elif attr == 'author': self.setAuthor(value)

    def _setLength(self, length):
        try:
            self.attrs['length'] = float(length)
        except ValueError:
            error(self.canvas, 'Value Error', 'Invalid length attribute for Boat item')
    def setLength(self, length):
        self._setLength(length)
        self.redraw()

    def _setWidth(self, width):
        try:
            self.attrs['width'] = float(width)
        except ValueError:
            error(self.canvas, 'Value Error', 'Invalid width attribute for Boat item')
        if self.attrs['width'] < 0:
            error(self.canvas, 'Value Error', 'Invalid width attribute for Boat item')
    def setWidth(self, width):
        self._setWidth(width)
        self.redraw()

    def _setHeight(self, height):
        try:
            self.attrs['height'] = float(height)
        except ValueError:
            error(self.canvas, 'Value Error', 'Invalid height attribute for Boat item')
        if self.attrs['height'] < 0:
            error(self.canvas, 'Value Error', 'Invalid height attribute for Boat item')
    def setHeight(self, height):
        self._setHeight(height)
        self.redraw()

    def _setBow(self, bow):
        try:
            self.attrs['bow'] = float(bow)
        except ValueError:
            error(self.canvas, 'Value Error', 'Invalid bow attribute for Boat item')
        if self.attrs['bow'] > self.attrs['length']:
            error(self.canvas, 'Value Error', 'Invalid bow attribute for Boat item')
    def setBow(self, bow):
        self._setBow(bow)
        self.redraw()

    def _setStern(self, stern):
        try:
            self.attrs['stern'] = float(stern)
        except ValueError:
            error(self.canvas, 'Value Error', 'Invalid stern attribute for Boat item')
        if self.attrs['stern'] > (self.attrs['length'] - self.attrs['bow']):
            error(self.canvas, 'Value Error', 'Invalid stern attribute for Boat item')
    def setStern(self, stern):
        self._setStern(stern)
        self.redraw()

    def _setWallWidth(self, wallWidth):
        try:
            self.attrs['wallWidth'] = float(wallWidth)
        except ValueError:
            error(self.canvas, 'Value Error', 'Invalid wallWidth attribute for Boat item')
        if self.attrs['wallWidth'] > (self.attrs['length'] / 2):
            error(self.canvas, 'Value Error', 'Invalid wallWidth attribute for Boat item')
    def setWallWidth(self, wallWidth):
        self._setWallWidth(wallWidth)

    def _setAuthor(self, author):
        self.attrs['author'] = author
    def setAuthor(self, author):
        self._setAuthor(author)
        self.redraw()
