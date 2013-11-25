import sys
from PyQt4 import QtGui, QtCore


class Edit(QtGui.QMainWindow):
    """
        The window to edit the parameters of an item.
    """

    def __init__(self, item):
        super(Edit, self).__init__()

        self.item = item

        self.initUI()


    def initUI(self):
        mainF = QtGui.QFrame()
        self.grid = QtGui.QGridLayout()

        if 'Boat' in str(self.item.__class__):
            self.boatUI()

        elif 'Furniture' in str(self.item.__class__):
            self.furnitureUI()

        elif 'Wall' in str(self.item.__class__):
            self.wallUI()

        self.grid.addWidget(QtGui.QPushButton('OK'), 9, 0)

        mainF.setLayout(self.grid)
        self.setCentralWidget(mainF)

        self.setWindowTitle('Editing '+ self.item.attrs['name'])


    def boatUI(self):
        self.grid.addWidget(QtGui.QLabel('Length:'), 0, 0)
        self.grid.addWidget(QtGui.QLineEdit(self), 1, 0)
        
        self.grid.addWidget(QtGui.QLabel('Width:'), 2, 0)
        self.grid.addWidget(QtGui.QLineEdit(self), 3, 0)

        self.grid.addWidget(QtGui.QLabel('Height:'), 4, 0)
        self.grid.addWidget(QtGui.QLineEdit(self), 5, 0)

        self.grid.addWidget(QtGui.QPushButton('Color'), 6, 0)

        self.grid.addWidget(QtGui.QLabel('Description:'), 0, 1)
        self.grid.addWidget(QtGui.QTextEdit(self), 1, 1, 9, 1)


    def furnitureUI(self):
        pass

    def wallUI(self):
        pass


def main():
    app = QtGui.QApplication(sys.argv)
    win = Edit()
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()