from PyQt4 import QtGui, QtCore

import items.item

class Furniture(items.item.Item):
    """
        An QGraphicsItemGroup which holds all the QItems 
            and can return its XML or SVG.
    """
    
    def __init__(self, canvas, name, x=0, y=0, scale=1, angle=0, 
                 description='', color='#000000'):
        super(Furniture, self).__init__()

        self.canvas = canvas
        
        self.attrs = {}
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


    def mousePressEvent(self, e):
        if e.button() == 1:
            self.setCursor(QtCore.Qt.ClosedHandCursor)
    def mouseReleaseEvent(self, e):
        # This runs the default event method, which allows 
        #   the dragging to work properly.
        QtGui.QGraphicsItem.mouseReleaseEvent(self, e)

        self.setCursor(QtCore.Qt.OpenHandCursor)
        self.top()

        self.setX(self.x()/(self.canvas.scale * self.canvas.ppm))
        self.setY(self.y()/(self.canvas.scale * self.canvas.ppm))


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
        pass