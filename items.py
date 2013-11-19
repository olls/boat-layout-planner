import sys

from templates import TEMPLATES

class Item(object):
    def __init__(self, description, color):
        self.description = description
        self.color = color

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


class Furniture(Item):
    def __init__(self, name, x, y, scale, angle, description, color):
        super(Furniture, self).__init__(description, color)

        # Validation
        try:
            x = float(x)
        except ValueError:
            sys.exit('Fatal error: Invalid x attribute for Furniture item')
        
        try:
            y = float(y)
        except ValueError:
            sys.exit('Fatal error: Invalid y attribute for Furniture item')
        
        try:
            scale = float(scale)
        except ValueError:
            sys.exit('Fatal error: Invalid scale attribute for Furniture item')

        try:
            angle = float(angle)
        except ValueError:
            sys.exit('Fatal error: Invalid angle attribute for Furniture item')

        
        self.attrs = {'name': name,
                      'x': x,
                      'y': y,
                      'scale': scale,
                      'angle': angle,
                      'description': description,
                      'color': color}

    def generateXML(self):
        return self.formatEval(TEMPLATES[self.attrs['name']]['XML'])

    def generateSVG(self):
        return self.formatEval(TEMPLATES[self.attrs['name']]['SVG'])


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


def main():
     chair1 = Furniture('chair', 0, 0, 1, 0, 'My Seat', '#000000')
     print(chair1.generateXML())
     chair1.setX('hi')
     print(chair1.generateXML())

if __name__ == '__main__':
    main()