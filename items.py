import sys
import math

from templates import TEMPLATES

class Item(object):
    def __init__(self):
        pass

    def formatEval(self, template):
        # First put the values in place as normal.
        s = template.format(**self.attrs)
        # Then split it at the quotes into a list.
        s = s.split('"')
        ret = s
        for i, section in enumerate(s):
            # Take the even elements from the list to get the bits between the quotes.
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
    def __init__(self, name, x, y, scale, angle, description, color):
        super(Furniture, self).__init__()
        
        self.attrs = {}

        self.setName(name)
        self.setX(x)
        self.setY(y)
        self.setScale(scale)
        self.setAngle(angle)
        self.setDescription(description)
        self.setColor(color)

    def generateXML(self):
        return self.formatEval(TEMPLATES[self.attrs['name']]['XML'])

    def generateSVG(self):
        return self.formatEval(TEMPLATES[self.attrs['name']]['SVG'])

    def generateVectors(self):
        svg = self.generateSVG()

        vectorItems = []
        item = True
        while item:
            item = svg[svg.find('<')+1 : svg.find('>')]
            svg = svg[svg.find('>')+1:]

            name = item.split(' ')[0]

            if name == 'line':
                vectorItems.append([name, {
                        'x1': self.getSVGItemAttrValue(item, 'x1'),
                        'y1': self.getSVGItemAttrValue(item, 'y1'),
                        'x2': self.getSVGItemAttrValue(item, 'x2'),
                        'y2': self.getSVGItemAttrValue(item, 'y2')
                    }
                ])

            elif name == 'rect':
                pass

        return vectorItems

    def getSVGItemAttrValue(self, item, attr):
        # Find attr.
        for section in item.split(' '):
            pos = section.find(attr)
            if not pos == -1:
                break
        # Get attr's value.
        return section.split('"')[1]

    def setName(self, name):
        self.attrs['name'] = name

    def setX(self, x):
        try:
            self.attrs['x'] = float(x)
        except ValueError:
            sys.exit('Fatal error: Invalid x attribute for Furniture item')

    def setY(self, y):
        try:
            self.attrs['y'] = float(y)
        except ValueError:
            sys.exit('Fatal error: Invalid y attribute for Furniture item')

    def setScale(self, scale):
        try:
            self.attrs['scale'] = float(scale)
        except ValueError:
            sys.exit('Fatal error: Invalid scale attribute for Furniture item')

    def setAngle(self, angle):
        try:
            self.attrs['angle'] = float(angle)
        except ValueError:
            sys.exit('Fatal error: Invalid angle attribute for Furniture item')

    def setDescription(self, description):
        self.attrs['description'] = description

    def setColor(self, color):
        self.attrs['color'] = color

    def setDescription(self, description):
        self.attrs['description'] = description

    def setColor(self, color):
        self.attrs['color'] = color


def main():
    chair1 = Furniture('chair', 100, 100, 1.5, 0, 'My Seat', '#000000')
    print(chair1.generateXML())
    print(chair1.generateSVG())
    print(chair1.generateVectors())

if __name__ == '__main__':
    main()