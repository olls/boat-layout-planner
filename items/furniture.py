from PyQt4 import QtGui, QtCore

import items.item

class Furniture(items.item.Item):
    """
        An QGraphicsItemGroup which holds all the QItems
            and can return its XML or SVG.
    """

    def __init__(self, canvas, name, x, y, xL, yL, scale=1, angle=0,
                 description='', color='#000000'):
        super(Furniture, self).__init__()

        self.canvas = canvas
        self.origin = (x, y)
        self.limit = (xL, yL)

        self.editable = {
            'scale':   'lineEdit',
            # 'angle':    QtGui.QLineEdit(self),
            'color':    'color'
        }

        self._setName(name)
        self._setX(x)
        self._setY(y)
        self._setScale(scale)
        self._setAngle(angle)
        self._setDescription(description)
        self._setColor(color)

        # Add ourself to the canvas and set as drag-able.
        self.canvas.scene.addItem(self)
        self.setFlag(QtGui.QGraphicsItem.ItemIsMovable)

        self.setToolTip(str(self.attrs['name']) + ':\n' +
                        str(self.attrs['description']))
        self.setCursor(QtCore.Qt.OpenHandCursor)

        # Create QItems
        self.redraw()
        self.updatePos()


    def mousePressEvent(self, e):
        if e.button() == 1:
            self.setCursor(QtCore.Qt.ClosedHandCursor)
    def mouseReleaseEvent(self, e):
        # This runs the default event method, which allows
        #   the dragging to work properly.
        QtGui.QGraphicsItem.mouseReleaseEvent(self, e)

        self.setCursor(QtCore.Qt.OpenHandCursor)
        self.top()

        self.updatePos()
        self.redraw()


    def updatePos(self):
        self._setX(self.x()+self.origin[0])
        self._setY(self.y()+self.origin[1])

        if self.attrs['x'] > self.limit[0] - self.boundingRect().width():
            self._setX(self.canvas.boat.attrs['x'] + self.limit[0] - self.boundingRect().width())
        elif self.attrs['x'] < self.canvas.boat.attrs['bow'] + self.canvas.boat.attrs['wallWidth']:
            self._setX(self.canvas.boat.attrs['bow'] + self.canvas.boat.attrs['wallWidth'])

        if self.attrs['y'] > self.limit[1] + self.origin[1] - self.boundingRect().height():
            self._setY(self.canvas.boat.attrs['y'] + self.limit[1] - self.boundingRect().height())
        elif self.attrs['y'] < self.canvas.boat.attrs['wallWidth']:
            self._setY(self.canvas.boat.attrs['wallWidth'])


    def updateAttr(self, attr, value):
        if attr == 'x': self.setX(value)
        elif attr == 'y': self.setY(value)
        elif attr == 'scale': self.setScale(value)
        elif attr == 'angle': self.setAngle(value)
        elif attr == 'description': self.setDescription(value)
        elif attr == 'color': self.setColor(value)

    # Each 'set' method has a private one for internal use which does the work
    #   and validates the input, and a public one which uses the private one
    #   then redraws the canvas.

    def _setScale(self, scale):
        try:
            self.attrs['scale'] = float(scale)
        except ValueError:
            sys.exit('Fatal error: Invalid scale attribute for Furniture item')
    def setScale(self, scale):
        self._setScale(scale)
        self.redraw()

    def _setAngle(self, angle):
        try:
            self.attrs['angle'] = float(angle)
        except ValueError:
            sys.exit('Fatal error: Invalid angle attribute for Furniture item')
    def setAngle(self, angle):
        self._setAngle(angle)
        self.redraw()


class Wall(items.item.Item):

    def __init__(self, canvas, x, y, xL, yL, doorY=0.1, doorWidth=0.7, scale=1, description='', color='#000000'):
        super(Wall, self).__init__()

        self.canvas = canvas
        self.origin = (x, y)
        self.limit = (xL, yL)

        self.editable = {
            'doorY':        'lineEdit',
            'doorWidth':    'lineEdit',
            'color':        'color',
            'scale':        'lineEdit'
        }

        self._setName('wall')
        self._setX(x)
        self._setY(y)
        self._setDoorY(doorY)
        self._setDoorWidth(doorWidth)
        self._setScale(scale)
        self._setDescription(description)
        self._setColor(color)

        # Add ourself to the canvas and set as drag-able.
        self.canvas.scene.addItem(self)
        self.setFlag(QtGui.QGraphicsItem.ItemIsMovable)

        self.setToolTip('Wall:\n' +
                        str(self.attrs['description']))
        self.setCursor(QtCore.Qt.OpenHandCursor)

        # Create QItems
        self.redraw()
        self.updatePos()


    def mousePressEvent(self, e):
        if e.button() == 1:
            self.setCursor(QtCore.Qt.ClosedHandCursor)
    def mouseReleaseEvent(self, e):
        # This runs the default event method, which allows
        #   the dragging to work properly.
        QtGui.QGraphicsItem.mouseReleaseEvent(self, e)

        self.setCursor(QtCore.Qt.OpenHandCursor)
        self.top()

        self.updatePos()
        self.redraw()


    def updatePos(self):
        self._setX(self.x()+self.origin[0])
        self._setY(self.y()+self.origin[1])

        if self.attrs['x'] > self.limit[0] - self.boundingRect().width():
            self._setX(self.canvas.boat.attrs['x'] + self.limit[0] - self.boundingRect().width())
        elif self.attrs['x'] < self.canvas.boat.attrs['bow'] + self.canvas.boat.attrs['wallWidth']:
            self._setX(self.canvas.boat.attrs['bow'] + self.canvas.boat.attrs['wallWidth'])

        if self.attrs['y'] > self.limit[1] + self.origin[1] - self.boundingRect().height():
            self._setY(self.canvas.boat.attrs['y'] + self.limit[1] - self.boundingRect().height())
        elif self.attrs['y'] < self.canvas.boat.attrs['wallWidth']:
            self._setY(self.canvas.boat.attrs['wallWidth'])


    def updateAttr(self, attr, value):
        if attr == 'x': self.setX(value)
        elif attr == 'y': self.setY(value)
        elif attr == 'doorY': self.setDoorY(value)
        elif attr == 'doorWidth': self.setDoorWidth(value)
        elif attr == 'scale': self.setScale(value)
        elif attr == 'description': self.setDescription(value)
        elif attr == 'color': self.setColor(value)

    # Each 'set' method has a private one for internal use which does the work
    #   and validates the input, and a public one which uses the private one
    #   then redraws the canvas.

    def _setScale(self, scale):
        try:
            self.attrs['scale'] = float(scale)
        except ValueError:
            sys.exit('Fatal error: Invalid scale attribute for Wall item')
    def setScale(self, scale):
        self._setScale(scale)
        self.redraw()

    def _setDoorY(self, doorY):
        try:
            self.attrs['doorY'] = float(doorY)
        except ValueError:
            sys.exit('Fatal error: Invalid doorY attribute for Wall item')
    def setDoorY(self, doorY):
        self._setDoorY(doorY)
        self.redraw()

    def _setDoorWidth(self, doorWidth):
        try:
            self.attrs['doorWidth'] = float(doorWidth)
        except ValueError:
            sys.exit('Fatal error: Invalid doorWidth attribute for Wall item')
    def setDoorWidth(self, doorWidth):
        self._setDoorWidth(doorWidth)
        self.redraw()