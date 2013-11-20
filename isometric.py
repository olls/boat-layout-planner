import sys
import math
import random
from PyQt4 import QtGui, QtCore

class Boat3D(QtGui.QMainWindow):
    """
        The window which displays the 3D isometric image of the boat widget.
    """
    def __init__(self, length, pos):
        super(Boat3D, self).__init__()

        self.pos = pos

        self.length = length
        self.wallHeight = 60

        # Creates the boat.
        self.image = Drawing(self.length, self.wallHeight)

        self.initUI()
        
    def initUI(self):

        # Center the boat image in the window.
        mainF = QtGui.QFrame()

        hbox = QtGui.QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.image)
        hbox.addStretch(1)

        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        vbox.addStretch(1)
        
        mainF.setLayout(vbox)
        self.setCentralWidget(mainF)


        self.statusBar()
        menubar = self.menuBar()

        exitAction = QtGui.QAction('&Exit', self)        
        exitAction.setShortcut('Ctrl+D')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        saveAction = QtGui.QAction('&Save', self)
        saveAction.setShortcut('Ctrl+S')
        saveAction.setStatusTip('Save the image to a file')
        saveAction.triggered.connect(lambda: self.image.save(self.statusBar))

        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(saveAction)
        fileMenu.addAction(exitAction)

        toolbar = self.addToolBar('File')
        toolbar.addAction(exitAction)
        toolbar.addAction(saveAction)


        # Center the window on the pos passed to it.
        self.setGeometry(0, 0, 350, 350)
        self.setGeometry(self.pos.x() - (self.frameGeometry().width()/2), 
                         self.pos.y() - (self.frameGeometry().height()/2), 
                         350, 350)

        self.setWindowTitle('Boat 3D')

class Drawing(QtGui.QWidget):
    """
        The widget which generates the drawing, 
        draws it in the widget and saves it as an SVG file.
    """

    def __init__(self, length, wallHeight):
        super(Drawing, self).__init__()

        self.length = length
        self.wallHeight = wallHeight
        # Calculate this here because it's being used a lot in the drawing code.
        self.COS30 = math.sqrt(3) /2

        # Calculate boat image dimensions.
        self.totLength = self.COS30 * (((5 * self.wallHeight) /2) + self.length)
        self.totHeight = (self.length /2) + ((3 * self.wallHeight) /2)
        self.origin = (self.COS30 * ((3 * self.wallHeight) /2), self.totHeight)

        self.calcualeVectors()

        self.initUI()
        
    def initUI(self):
        self.setMinimumSize(self.totLength+1, self.totHeight+1)
        self.show()

    def paintEvent(self, event):
        """ The event which triggers the redrawing of the boat. """

        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawBoat(qp)
        qp.end()

    def rLine(self, length, origin):
        """ Converts the right-hand 30 degree line to vector information 
            in the format needed for the pen.drawLine method """
        
        x = origin[0] + (self.COS30 * length) # (math.sqrt(3)/2) * length
        y = origin[1] - (length /2)

        return origin[0], origin[1], x, y

    def lLine(self, length, origin):
        """ Converts the left-hand 30 degree line to vector information 
            in the format needed for the pen.drawLine method """
        
        x = origin[0] - (self.COS30 * length) # (math.sqrt(3)/2) * length
        y = origin[1] - (length / 2)

        return origin[0], origin[1], x, y

    def vLine(self, length, origin):
        """ Converts the vertical line to vector information 
            in the format needed for the pen.drawLine method """
        
        x = origin[0]
        y = origin[1] + length

        return origin[0], origin[1], x, y

    def calcualeVectors(self):
        """ This calculates the vectors to draw the boat
            based off the length and line height """
        
        self.vectors = (
            # Left wall
            self.rLine(self.length, 
                       (self.origin[0],
                        self.origin[1] - self.wallHeight)),
            self.rLine(self.length + self.wallHeight, 
                       self.origin),
            self.vLine((self.wallHeight / 3) * 2, 
                       (self.origin[0], 
                        self.origin[1] - self.wallHeight)),
            self.vLine((self.wallHeight / 3) * 2, 
                       (self.origin[0] + (self.COS30 * self.length), 
                        self.origin[1] - self.wallHeight - (self.length / 2))),

            # Front wall
            self.lLine(self.wallHeight, 
                       (self.origin[0], 
                        self.origin[1] - (self.wallHeight / 3))),
            self.lLine(self.wallHeight, 
                       (self.origin[0], 
                        self.origin[1] - self.wallHeight)),
            self.vLine((self.wallHeight / 3) * 2, 
                       (self.origin[0] - (self.COS30 * self.wallHeight), 
                        self.origin[1] - ((3 * self.wallHeight) / 2))),

            # Roof
            self.rLine(self.length, 
                       (self.origin[0] - (self.COS30 * self.wallHeight), 
                        self.origin[1] - ((3 * self.wallHeight) / 2))),
            self.lLine(self.wallHeight, 
                       (self.origin[0] + (self.COS30 * self.length), 
                        self.origin[1] - self.wallHeight - (self.length / 2))),

            # Back
            self.rLine(self.wallHeight, 
                       (self.origin[0] + (self.COS30 * self.length), 
                        self.origin[1] - (self.length / 2) - (self.wallHeight / 3))),
            self.vLine(self.wallHeight / 3,
                       (self.origin[0] + (self.COS30 * (self.length + self.wallHeight)), 
                        self.origin[1] - (self.length / 2) - ((5 * self.wallHeight) / 6))),
            self.lLine(self.wallHeight,
                       (self.origin[0] + (self.COS30 * (self.length + self.wallHeight)), 
                        self.origin[1] - (self.length / 2) - ((5 * self.wallHeight) / 6))),
            self.rLine(self.wallHeight / 3, 
                       (self.origin[0] + (self.COS30 * self.length) - (self.COS30 * (self.wallHeight / 3)), 
                        self.origin[1] -(self.length / 2) - ((7 * self.wallHeight) / 6))),

            # Point
            # Because these lines are not parallel to any 
            #   of the three axis, I cannot use the rLine, lLine 
            #   or vLine methods, so I calculate the vector information
            #   straight to the format needed for the pen.drawLine method.
            (self.origin[0], 
             self.origin[1] - (self.wallHeight / 3), 
             self.origin[0] + self.COS30 * (-3 * (self.wallHeight / 2)), 
             self.origin[1] - (self.wallHeight / 12)),
            (self.origin[0] - (self.COS30 * self.wallHeight), 
             self.origin[1] - ((5 * self.wallHeight) / 6), 
             self.origin[0] + self.COS30 * (-3 * (self.wallHeight / 2)), 
             self.origin[1] - (self.wallHeight / 12)),
            (self.origin[0], 
             self.origin[1], 
             self.origin[0] + self.COS30 * (-3 * (self.wallHeight / 2)), 
             self.origin[1] - (self.wallHeight / 12))
        )

    def drawBoat(self, qp):
        """ Draws the vectors calculated by self.calcualeVectors 
            to the widget. """
        
        pen = QtGui.QPen(QtCore.Qt.black, 1, QtCore.Qt.SolidLine)
        qp.setPen(pen)

        for vector in self.vectors:
            qp.drawLine(*vector)

    def generateSVG(self):
        """ Generates the SVG which is used when the user saves the image. """

        svg = '<?xml version="1.0"?>\n<svg width="{width}" height="{height}" version="1.1" xmlns="http://www.w3.org/2000/svg">'.format(width=int(self.totLength+2), height=(self.totHeight+2))
        for vector in self.vectors:
            vector = [int(i)+1 for i in vector]
            svg += '\n<line x1="{}" y1="{}" x2="{}" y2="{}" stroke="black" stroke-width="1"/>'.format(*vector)
        svg += '\n</svg>'
        return svg

    def save(self, statusBar):
        """ Displays a file save dialog and saves the file. """
        
        svg = self.generateSVG()

        filename = QtGui.QFileDialog.getSaveFileName(self, 'Save SVG File', 
                                                     '/home', '*.svg')
        if filename:
            if not str(filename)[-4:].lower() == '.svg':
                filename += '.svg'
            try:
                with open(filename, 'w') as f:
                    f.write(svg)
                statusBar().showMessage('Saved \'{}\' successfully.'
                                        .format(filename))
            except IOError:
                QtGui.QMessageBox.question(self, 'Error', 
                    "<center>Error while saving.<br>This could be due to not having permission<br>or using an invalid filename.</center>", 
                    QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
        else:
            statusBar().showMessage('Saving Canceled')


def main():
    try:
        length = sys.argv[1]
    except IndexError:
        length = random.randint(0, 300)

    app = QtGui.QApplication(sys.argv)
    bt1 = Boat3D(length, QtGui.QDesktopWidget().availableGeometry().center())
    bt1.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()