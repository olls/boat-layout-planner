from PyQt4 import QtGui


def error(self, error, msg):
    QtGui.QMessageBox.warning(self, error, '<center><b>' + error + ':</b> ' + msg + '</center>', buttons=QtGui.QMessageBox.Ok)
