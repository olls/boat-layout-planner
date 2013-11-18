import sys
from PyQt4 import QtGui

class Item(object):
    def __init__(self, description, color):
        self.description = description
        self.color = color

class Furniture(Item):
    templates = {
        'Chair':
            {'XML': '<chair scale="{scale}" x="{x}" y="{y}" color="{color}" />', 
             'SVG': '<line x="{x}"/>'}
    }
    def __init__(self, name, x, y, scale, angle, description, color):
        super(Furniture, self).__init__(description, color)

        self.name = name
        try:
            self.x = float(x)
        except ValueError:
            sys.exit('Invalid x attribute for Furniture item')
        try:
            self.y = float(y)
        except ValueError:
            sys.exit('Invalid y attribute for Furniture item')
        try:
            self.scale = float(scale)
        except ValueError:
            sys.exit('Invalid scale attribute for Furniture item')
        try:
            self.angle = float(angle)
        except ValueError:
            sys.exit('Invalid angle attribute for Furniture item')
        self.description = description
        self.color = color

        self.XML = templates[self.name]['XML']
        self.SVG = templates[self.name]['SVG']

    def generateXML(self):
        return

    def generateSVG(self):
        return

class BoatPlanner(QtGui.QMainWindow):
    def __init__(self):
        super(BoatPlanner, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        # Create Canvas
        self.canvas = QtGui.QGraphicsScene()
        self.canvasView = QtGui.QGraphicsView(self.canvas)
        
        self.setCentralWidget(self.canvasView)
        
        exitAction = QtGui.QAction(QtGui.QIcon('exit24.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)
        
        self.setWindowTitle('Boat Layout Planner')

def main():
    app = QtGui.QApplication(sys.argv)
    mainWin = BoatPlanner()
    mainWin.showMaximized()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()