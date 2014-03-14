import json
from PyQt4 import QtGui


def error(self, error, msg):
    """
        The function used to create an error message box.
    """
    QtGui.QMessageBox.warning(self, error, '<center><b>' + error + ':</b> ' + msg + '</center>', buttons=QtGui.QMessageBox.Ok)


with open('items/templates.json', 'r') as templates_file:
    templates = json.load(templates_file)
