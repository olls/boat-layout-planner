import sys
from PyQt4 import QtGui, QtCore


class Edit(QtGui.QMainWindow):
    """
        The window to edit the parameters of an item.
    """

    def __init__(self, item):
        super(Edit, self).__init__()

        self.item = item

        self.fieldsTypes = {
            'lineEdit': lambda: QtGui.QLineEdit(self),
            'color': lambda: ColorPicker()
        }
        self.fields = {}

        self.initUI()


    def initUI(self):
        mainF = QtGui.QFrame()
        self.grid = QtGui.QGridLayout()

        y = 0
        for key, value in self.item.editable.items():

            # Create the field object by running the
            #   lambda in the fieldsTypes dict.
            field = self.fieldsTypes[value]()

            field.insert(str(self.item.attrs[key]))

            # Give line edits labels:
            if isinstance(field, QtGui.QLineEdit):
                self.grid.addWidget(QtGui.QLabel(Edit.capt(key)+':'), y, 0)
                y += 1

            self.grid.addWidget(field, y, 0)
            y += 1

            # Add the field object to the dict so we
            #    can save the value later.
            self.fields.update({key: field})

        # Create the description that all of them have.
        self.description = QtGui.QTextEdit(self)
        self.description.append(self.item.attrs['description'])

        self.grid.addWidget(QtGui.QLabel('Description:'), 0, 1)
        self.grid.addWidget(self.description, 1, 1, y, 1)


        btn = QtGui.QPushButton('OK')
        btn.clicked.connect(self.ok)
        self.grid.addWidget(btn, y, 0)

        mainF.setLayout(self.grid)
        self.setCentralWidget(mainF)

        self.setWindowTitle('Edit: '+ self.item.attrs['name'])

    def ok(self):
        """ Updates self.item with the data in self.fields. """

        print('\nUpdating \''+str(self.item.attrs['name'])+'\':')

        for key, field in self.fields.items():

            # Extract the data from the field:
            data = field.text()

            # Find the data type
            try:
                data = float(data)
            except ValueError:
                data = str(data)

            # Update the item with the new data
            print(str(key)+': '+str(data))
            self.item.updateAttr(key, data)

        print('description: '+str(self.description.toPlainText()))
        self.item.setDescription(str(self.description.toPlainText()))

        print('\n')
        self.close()

    def capt(string):
        """ Takes a string, and capitalizes the first letter. """
        return string[:1].upper() + string[1:]

class ColorPicker(QtGui.QPushButton):
    """ A button widget which activates a color
        picker, and it is the color it is given. """
    def __init__(self):
        super(ColorPicker, self).__init__('Color')

        self.color = QtGui.QColor(0, 0, 0)
        self.clicked.connect(self.showDialog)

    def update(self):
        self.setStyleSheet('QPushButton { background-color: '+self.text()+'; color: ' + str('white' if self.color.lightness() < 127 else 'black') + '}')

    def showDialog(self):
        self.color = QtGui.QColorDialog.getColor(self.color)
        self.update()

    def insert(self, color):
        self.color = QtGui.QColor(color)
        self.update()

    def text(self):
        return self.color.name()

def main():
    app = QtGui.QApplication(sys.argv)
    win = Edit()
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()