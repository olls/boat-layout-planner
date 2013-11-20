import sys
import math
from PyQt4 import QtGui, QtCore

from templates import TEMPLATES

class Item(QtGui.QGraphicsItemGroup):
    """
        An Item class which all displayed items on the canvas are derived from.
    """

    def __init__(self):
        super(Item, self).__init__()

    def formatEval(self, template):
        """ A method which acts like the str.format method, except it evaluates 
            the contents of quotes after inserting the values """
        # First put the values in place as normal.
        s = template.format(**self.attrs)
        # Then split it at the quotes into a list.
        s = s.split('"')
        ret = s
        for i, section in enumerate(s):
            # Take the even elements from the list to 
            #   get the bits between the quotes.
            if (i+1)%2 == 0:
                # Try to evaluate it, if it causes an error, I will assume it's 
                #   not an expression, and leave it alone.
                try:
                    result = eval(section)
                except:
                    result = section
                # Add the result back to the list.
                ret[i] = '"' + str(result) + '"'
            else:
                # The bits not in quotes are left alone.
                ret[i] = str(section)
        # Join the list back into a string.
        return ''.join(ret)


class Boat(Item):
    pass


class Wall(Item):
    pass


class Furniture(Item):
    """
        An QGraphicsItemGroup which holds all the QItems 
            and can return its XML or SVG.
    """
    
    def __init__(self, name, x, y, scale, angle, description, color, canvas):
        super(Furniture, self).__init__()
        
        self.attrs = {}

        self._setName(name)
        self._setX(x)
        self._setY(y)
        self._setScale(scale)
        self._setAngle(angle)
        self._setDescription(description)
        self._setColor(color)

        self.canvas = canvas

        # Add ourself to the canvas and set as drag-able.
        self.canvas.scene.addItem(self)
        self.setFlag(QtGui.QGraphicsItem.ItemIsMovable)
        self.setAcceptHoverEvents(True)

        # Create QItems
        self.update()

    def generateXML(self):
        """ Creates XML code for this object using the template and attrs """
        
        return self.formatEval(TEMPLATES[self.attrs['name']]['XML'])

    def generateSVG(self):
        """ Creates SVG code for this object using the template and attrs """
        
        return self.formatEval(TEMPLATES[self.attrs['name']]['SVG'])

    def update(self):
        """ Creates vector information for this object, which is 
            then displayed on the canvas. """

        # First remove all items from group.
        for child in self.childItems():
            self.removeFromGroup(child)

        # It converts the SVG vector information to QItems.
        svg = self.generateSVG()

        vectorItems = []
        item = True
        while item:
            # Goes through each SVG item and depending on the type,
            #   extracts different attributes from it and creates the QItem.
            item = svg[svg.find('<')+1 : svg.find('>')]
            svg = svg[svg.find('>')+1:]

            name = item.split(' ')[0]

            if name == 'line':
                QItem = self.canvas.scene.addLine(
                    QtCore.QLineF(float(self.getSVGItemAttrValue(item, 'x1')),
                                  float(self.getSVGItemAttrValue(item, 'y1')),
                                  float(self.getSVGItemAttrValue(item, 'x2')),
                                  float(self.getSVGItemAttrValue(item, 'y2')))
                )

            elif name == 'rect':
                pass

            # Add the QItem to ourself so it is a part of the group.
            self.addToGroup(QItem)

    def getSVGItemAttrValue(self, item, attr):
        """ Takes an SVG item and returns the value of a given attribute. """

        # Find attribute.
        for section in item.split(' '):
            pos = section.find(attr)
            if not pos == -1:
                break

        # Get attributes value.
        return section.split('"')[1]


    # Each 'set' method has a private one for internal use which does the work
    #   and validates the input, and a public one which uses the private one
    #   then updates the canvas.

    def _setName(self, name):
        self.attrs['name'] = name    
    def setName(self, name):
        self._setName(name)
        self.update()

    def _setX(self, x):
        try:
            self.attrs['x'] = float(x)
        except ValueError:
            sys.exit('Fatal error: Invalid x attribute for Furniture item')
    def setX(self, x):
        self._setX(x)
        self.update()

    def _setY(self, y):
        try:
            self.attrs['y'] = float(y)
        except ValueError:
            sys.exit('Fatal error: Invalid y attribute for Furniture item')
    def setY(self, y):
        self._setY(y)
        self.update()

    def _setScale(self, scale):
        try:
            self.attrs['scale'] = float(scale)
        except ValueError:
            sys.exit('Fatal error: Invalid scale attribute for Furniture item')
    def setScale(self, scale):
        self._setScale(scale)
        self.update()

    def _setAngle(self, angle):
        try:
            self.attrs['angle'] = float(angle)
        except ValueError:
            sys.exit('Fatal error: Invalid angle attribute for Furniture item')
    def setAngle(self, angle):
        self._setAngle(angle)
        self.update()

    def _setDescription(self, description):
        self.attrs['description'] = description
    def setDescription(self, description):
        self._setDescription(description)
        self.update()

    def _setColor(self, color):
        self.attrs['color'] = color
    def setColor(self, color):
        self._setColor(color)
        self.update()

def main():
    """
        Can't do much to test, because the Furniture class relies 
            on the canvas class
    """

    # Canvas doesn't exist so this doesn't run.
    chair1 = Furniture('chair', 100, 100, 1.5, 0, 'My Seat', '#000000', canvas)
    print(chair1.generateXML())
    print(chair1.generateSVG())
    print(chair1.generateVectors())

if __name__ == '__main__':
    main()