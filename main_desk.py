#!/usr/bin/env python
# -*- coding: utf-8 -*-
import main as UI
from PyQt4 import QtCore, QtGui
import sys
import dialogclass
import database as DB


class mid(QtGui.QMainWindow, UI.Ui_MainWindow):
    def __init__(self, parent=None):
        super(mid, self).__init__(parent)
        self.setupUi(self)
        # bindings com funcoes do python
        self.connect(self.pushButton_cancel_item,QtCore.SIGNAL("clicked()"),self.cancel_item)
        self.connect(self.pushButton_cancel_venda,QtCore.SIGNAL("clicked()"),self.cancel_venda)
        self.connect(self.pushButton_fechar_venda,QtCore.SIGNAL("clicked()"),self.fechar_venda)

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

        self.actionCadastrar_produto.triggered.connect(self.Cad_Prod)
        self.actionCadastrar_item_card_pio.triggered.connect(self.Cad_Item)
        self.actionCadastrar_funcion_rio.triggered.connect(self.Cad_Func)
        #self.actionSair = QtGui.QAction(MainWindow)
        self.actionCadastrar_novo_item.triggered.connect(self.Cad_Item)

        self.actionAtualizar_estoque.triggered.connect(self.Cad_Prod)
         #self.actionSair_2 = QtGui.QAction(MainWindow)

        self.actionConsultar_produto.triggered.connect(self.Search)
        self.actionConsultar_funcion_rio.triggered.connect(self.Cad_Prod)
        self.actionConsultar_Estoque.triggered.connect(self.Search)
        # self.actionSair_3 = QtGui.QAction(MainWindow)

        self.actionSupore.triggered.connect(self.Suport)
         #self.actionSair_4 = QtGui.QAction(MainWindow)

        self.actionVendas_por_per_odo.triggered.connect(self.Relat_Vend_periodo)
        self.actionRelat_rio_por_per_odo.triggered.connect(self.Relat_Vend_periodo)
        self.actionRelat_rio_por_produto.triggered.connect(self.Relat_Vend_prod)
         #self.actionSair_5 = QtGui.QAction(MainWindow)


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
        #app = QtGui.QApplication(sys.argv)
        dlg = dialogclass.Dialog_Tool(self)
        dlg.show()

    def Search(self):
        dlg = dialogclass.Dialog_Cons_Est(self)
        dlg.show()

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

    def Cad_Prod(self):
        dlg = dialogclass.Dialog_Cad_Prod(self)
        dlg.show()
    def Cad_Item(self):
        dlg = dialogclass.Dialog_Cad_Item(self)
        dlg.show()
    def Cad_Func(self):
        dlg = dialogclass.Dialog_Cad_Func(self)
        dlg.show()

    def Suport(self):
        pass
    def Relat_Vend_periodo(self):
        pass

    def Relat_Vend_prod(self):
        pass

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main_window = mid()
    main_window.show()
    app.exec_()