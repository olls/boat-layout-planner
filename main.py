import sys
import random
from PyQt4 import QtGui, QtCore

import isometric
import layout
import canvas

class BoatPlanner(QtGui.QMainWindow):
    def __init__(self):
        super(BoatPlanner, self).__init__()

        self.canvas = layout.Canvas()

        self.initUI()

    def initUI(self):
        mainF = QtGui.QFrame()

        hbox = QtGui.QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.canvas)
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

        isoAction = QtGui.QAction('&3D View', self)
        isoAction.setStatusTip('View an isometric image of the boat.')
        isoAction.triggered.connect(self.isoView)

        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(isoAction)
        fileMenu.addAction(exitAction)

        toolbar = self.addToolBar('File')
        toolbar.addAction(exitAction)
        toolbar.addAction(isoAction)


        self.setWindowState(QtCore.Qt.WindowMaximized)
        self.setWindowTitle('Boat Layout Planner')

    def isoView(self):
        self.win = isometric.Boat3D(random.randint(0, 300))
        self.win.show()

def main():
    app = QtGui.QApplication(sys.argv)
    win = BoatPlanner()
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()