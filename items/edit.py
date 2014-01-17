import sys
from PyQt4 import QtGui, QtCore


class Edit(QtGui.QMainWindow):
    """
        The window to edit the parameters of an item.
    """

    def __init__(self, item):
        super(Edit, self).__init__()

        self.item = item

        if 'Boat' in str(self.item.__class__):
            self.values = {
                'length':   QtGui.QLineEdit(self),
                'width':    QtGui.QLineEdit(self),
                'wallWidth':   QtGui.QLineEdit(self),
                'height':   QtGui.QLineEdit(self)#,
                # 'color':    QtGui.QPushButton('Color')
            }
        elif 'Furniture' in str(self.item.__class__):
            self.values = {
                'scale':   QtGui.QLineEdit(self),
                'angle':    QtGui.QLineEdit(self),
                'color':    QtGui.QPushButton('Color')
            }
        elif 'Wall' in str(self.item.__class__):
            self.values = {
                'width':    QtGui.QLineEdit(self),
                'door y':   QtGui.QLineEdit(self),
                'color':    QtGui.QPushButton('Color')
            }

        self.initUI()


    def initUI(self):
        mainF = QtGui.QFrame()
        self.grid = QtGui.QGridLayout()

        y = 0
        for key, value in self.values.items():
            value.insert(str(self.item.attrs[key]))
            self.grid.addWidget(QtGui.QLabel(Edit.capt(key)+':'), y, 0)
            self.grid.addWidget(value, y+1, 0)
            y += 2

        self.grid.addWidget(QtGui.QLabel('Description:'), 0, 1)
        self.description = QtGui.QTextEdit(self)
        self.description.append(self.item.attrs['description'])
        self.grid.addWidget(self.description, 1, 1, y, 1)

        btn = QtGui.QPushButton('OK')
        btn.clicked.connect(self.save)
        self.grid.addWidget(btn, y, 0)

        mainF.setLayout(self.grid)
        self.setCentralWidget(mainF)

        self.setWindowTitle('Editing '+ self.item.attrs['name'])

    def save(self):
        for key, value in self.values.items():
            v = value.text()
            try:
                v = int(v)
            except ValueError:
                try:
                    v = str(v)
                except ValueError:
                    pass
            command = 'self.item.set{key}({value})'.format(key = Edit.capt(key), value = value.text())
            print(command)
            exec(command)
        print(self.description.toPlainText())
        self.item.setDescription(str(self.description.toPlainText()))
        self.close()

    def capt(string):
        """ Takes a string, and capitalizes the first letter. """
        return string[:1].upper() + string[1:]

def main():
    app = QtGui.QApplication(sys.argv)
    win = Edit()
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()