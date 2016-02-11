import main as UI
from PyQt4 import QtCore, QtGui
import sys
import database as DB

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class mid(QtGui.QMainWindow, UI.Ui_MainWindow):
    def __init__(self, parent=None):
        super(mid, self).__init__(parent)
        self.setupUi(self)
        # aqui voce faz os bindings com funcoes do python
        self.connect(self.pushButton_cancel_item,QtCore.SIGNAL("clicked()"),self.cancel_item)
        self.connect(self.pushButton_cancel_venda,QtCore.SIGNAL("clicked()"),self.cancel_venda)
        self.connect(self.pushButton_fechar_venda,QtCore.SIGNAL("clicked()"),self.fechar_venda)

        #self.actionTool.setObjectName(_fromUtf8("actionTool"))
        self.actionTool.triggered.connect(self.Tool)
        self.actionSearch.triggered.connect(self.Search)
        self.actionFood.triggered.connect(self.Food)
        self.actionDrink.triggered.connect(self.Drink)
        self.actionPhone.triggered.connect(self.Phone)
        self.actionCalendar.triggered.connect(self.Calendar)
        self.actionBd.triggered.connect(self.Bd)
        self.actionCredit.triggered.connect(self.Credit)
        self.actionSignin.triggered.connect(self.Signin)
        self.actionSignout.triggered.connect(self.Signout)


    def cancel_item(self):
        pass
        #metodo para cancelar item
    def cancel_venda(self):
        pass
        #metodo para cancelar venda
    def fechar_venda(self):
        pass
        #metodo para fechar venda
    def Tool(self):
        print("clique actionTool")
    def Search(self):
        print("clique actionTool")
    def Food(self):
        pass
    def Drink(self):
        pass
    def Phone(self):
        pass
    def Calendar(self):
        pass
    def Bd(self):
        pass
    def Credit(self):
        pass
    def Signin(self):
        pass
    def Signout(self):
        pass


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main_window = mid()
    main_window.show()
    app.exec_()