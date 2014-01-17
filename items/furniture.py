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
        elif self.attrs['x'] < self.origin[0]:
            self._setX(self.origin[0])

        if self.attrs['y'] > self.limit[1] + self.origin[1] - self.boundingRect().height():
            self._setY(self.canvas.boat.attrs['y'] + self.limit[1] - self.boundingRect().height())
        elif self.attrs['y'] < self.origin[1]:
            self._setY(self.origin[1])


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

    def __init__(self, x=0, doorY=0, description=''):
        self.editable = {
            'width':    'lineEdit',
            'door y':   'lineEdit',
            'color':    'color'
        }