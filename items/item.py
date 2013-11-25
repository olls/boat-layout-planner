import sys
import math
from PyQt4 import QtGui, QtCore

# import items.edit
from items.templates import TEMPLATES


class Item(QtGui.QGraphicsItemGroup):
    """
        An Item class which all displayed items on the canvas are derived from.
    """

    def __init__(self):
        super(Item, self).__init__()

        self.TEMPLATES = self.flatten(TEMPLATES)


    def redraw(self):
        """ Creates vector information for this object, which is 
            then displayed on the canvas. """

        # First remove all items from group.
        for child in self.childItems():
            self.removeFromGroup(child)

        # It converts the SVG vector information to QItems.
        svg = self.generateSVG()

        self._setX(self.x() / (self.canvas.scale * self.canvas.ppm))
        self._setY(self.y() / (self.canvas.scale * self.canvas.ppm))

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
                    QtCore.QLineF(float(self.getSVGItemAttrValue(item, 'x1'))*self.canvas.scale*self.canvas.ppm,
                                  float(self.getSVGItemAttrValue(item, 'y1'))*self.canvas.scale*self.canvas.ppm,
                                  float(self.getSVGItemAttrValue(item, 'x2'))*self.canvas.scale*self.canvas.ppm,
                                  float(self.getSVGItemAttrValue(item, 'y2'))*self.canvas.scale*self.canvas.ppm)
                )

            elif name == 'rect':
                pass

            # Add the QItem to ourself so it is a part of the group.
            self.addToGroup(QItem)
        self.top()


    def generateXML(self):
        """ Creates XML code for this object using the template and attrs """
        return self.formatEval(self.TEMPLATES[self.attrs['name']]['XML'])

    def generateSVG(self):
        """ Creates SVG code for this object using the template and attrs """
        return self.formatEval(self.TEMPLATES[self.attrs['name']]['SVG'])

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

    def flatten(self, dic):
        out = {}
        for key in dic:
            if isinstance(dic[key], dict):
                out.update(dic[key])
            else:
                out.update({key: d[key]})
        return out

    def getSVGItemAttrValue(self, item, attr):
        """ Takes an SVG item and returns the value of a given attribute. """

        # Find attribute.
        for section in item.split(' '):
            pos = section.find(attr)
            if not pos == -1:
                break

        # Get attributes value.
        return section.split('"')[1]


    def top(self):
        """ Brings us to the top. """
        # Sets our Z value to one.
        self.setZValue(1)
        # Set every colliding items Z value to 0
        for sibling in self.collidingItems():
            sibling.setZValue(0)

    
    def mouseDoubleClickEvent(self, e):
        """ Opens the edit window when double clicked. """
        # self.win = items.edit.Edit(self)
        # self.win.show()
        pass


    # Each 'set' method has a private one for internal use which does the work
    #   and validates the input, and a public one which uses the private one
    #   then redraws the canvas.

    def _setName(self, name):
        self.attrs['name'] = name    
    def setName(self, name):
        self._setName(name)
        self.redraw()

    def _setX(self, x):
        try:
            self.attrs['x'] = float(x)
        except ValueError:
            sys.exit('Fatal error: Invalid x attribute for Furniture item')
    def setX(self, x):
        self._setX(x)
        self.redraw()

    def _setY(self, y):
        try:
            self.attrs['y'] = float(y)
        except ValueError:
            sys.exit('Fatal error: Invalid y attribute for Furniture item')
    def setY(self, y):
        self._setY(y)
        self.redraw()

    def _setDescription(self, description):
        self.attrs['description'] = description
    def setDescription(self, description):
        self._setDescription(description)
        self.redraw()

    def _setColor(self, color):
        self.attrs['color'] = color
    def setColor(self, color):
        self._setColor(color)
        self.redraw()


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