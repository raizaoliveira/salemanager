# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 509)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.frame = QtGui.QFrame(self.tab)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout_2 = QtGui.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.lineEdit_item = QtGui.QLineEdit(self.frame)
        self.lineEdit_item.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_item.setObjectName(_fromUtf8("lineEdit_item"))
        self.gridLayout_2.addWidget(self.lineEdit_item, 2, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(45)
        self.label_5.setFont(font)
        self.label_5.setAutoFillBackground(False)
        self.label_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 0, 2, 1, 2)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        self.label = QtGui.QLabel(self.frame)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 1, 1, 1, 1)
        self.lineEdit_desc = QtGui.QLineEdit(self.frame)
        self.lineEdit_desc.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_desc.setObjectName(_fromUtf8("lineEdit_desc"))
        self.gridLayout_2.addWidget(self.lineEdit_desc, 2, 1, 1, 1)
        self.lineEdit_Qtd = QtGui.QLineEdit(self.frame)
        self.lineEdit_Qtd.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_Qtd.setObjectName(_fromUtf8("lineEdit_Qtd"))
        self.gridLayout_2.addWidget(self.lineEdit_Qtd, 3, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 3, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.frame)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 4, 0, 1, 1)
        self.lcdNumber_Sub = QtGui.QLCDNumber(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber_Sub.sizePolicy().hasHeightForWidth())
        self.lcdNumber_Sub.setSizePolicy(sizePolicy)
        self.lcdNumber_Sub.setMinimumSize(QtCore.QSize(30, 50))
        self.lcdNumber_Sub.setAutoFillBackground(True)
        self.lcdNumber_Sub.setFrameShape(QtGui.QFrame.Panel)
        self.lcdNumber_Sub.setObjectName(_fromUtf8("lcdNumber_Sub"))
        self.gridLayout_2.addWidget(self.lcdNumber_Sub, 4, 1, 1, 1)
        self.listView_cx = QtGui.QListView(self.frame)
        self.listView_cx.setAutoFillBackground(True)
        self.listView_cx.setObjectName(_fromUtf8("listView_cx"))
        self.gridLayout_2.addWidget(self.listView_cx, 1, 2, 6, 3)
        self.lcdNumber_Tot = QtGui.QLCDNumber(self.frame)
        self.lcdNumber_Tot.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber_Tot.sizePolicy().hasHeightForWidth())
        self.lcdNumber_Tot.setSizePolicy(sizePolicy)
        self.lcdNumber_Tot.setAutoFillBackground(True)
        self.lcdNumber_Tot.setFrameShape(QtGui.QFrame.Panel)
        self.lcdNumber_Tot.setObjectName(_fromUtf8("lcdNumber_Tot"))
        self.gridLayout_2.addWidget(self.lcdNumber_Tot, 5, 0, 1, 2)
        self.groupBox_btn = QtGui.QGroupBox(self.frame)
        self.groupBox_btn.setTitle(_fromUtf8(""))
        self.groupBox_btn.setObjectName(_fromUtf8("groupBox_btn"))
        self.pushButton_cancel_item = QtGui.QPushButton(self.groupBox_btn)
        self.pushButton_cancel_item.setGeometry(QtCore.QRect(10, 0, 121, 27))
        self.pushButton_cancel_item.setObjectName(_fromUtf8("pushButton_cancel_item"))
        self.pushButton_cancel_venda = QtGui.QPushButton(self.groupBox_btn)
        self.pushButton_cancel_venda.setGeometry(QtCore.QRect(130, 0, 131, 27))
        self.pushButton_cancel_venda.setObjectName(_fromUtf8("pushButton_cancel_venda"))
        self.pushButton_fechar_venda = QtGui.QPushButton(self.groupBox_btn)
        self.pushButton_fechar_venda.setGeometry(QtCore.QRect(260, 0, 121, 27))
        self.pushButton_fechar_venda.setObjectName(_fromUtf8("pushButton_fechar_venda"))
        self.gridLayout_2.addWidget(self.groupBox_btn, 7, 2, 1, 2)
        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout_5 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setEnabled(True)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setAutoFillBackground(False)
        self.menubar.setDefaultUp(False)
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuCadastro = QtGui.QMenu(self.menubar)
        self.menuCadastro.setObjectName(_fromUtf8("menuCadastro"))
        self.menuEstoque = QtGui.QMenu(self.menubar)
        self.menuEstoque.setObjectName(_fromUtf8("menuEstoque"))
        self.menuConsultar = QtGui.QMenu(self.menubar)
        self.menuConsultar.setObjectName(_fromUtf8("menuConsultar"))
        self.menuAjuda = QtGui.QMenu(self.menubar)
        self.menuAjuda.setObjectName(_fromUtf8("menuAjuda"))
        self.menuRelat_rios = QtGui.QMenu(self.menubar)
        self.menuRelat_rios.setObjectName(_fromUtf8("menuRelat_rios"))
        self.menuRelat_rio_de_vendas = QtGui.QMenu(self.menuRelat_rios)
        self.menuRelat_rio_de_vendas.setObjectName(_fromUtf8("menuRelat_rio_de_vendas"))
        self.menuRelat_rio_de_estoque = QtGui.QMenu(self.menuRelat_rios)
        self.menuRelat_rio_de_estoque.setObjectName(_fromUtf8("menuRelat_rio_de_estoque"))
        self.menuAjuda_2 = QtGui.QMenu(self.menubar)
        self.menuAjuda_2.setObjectName(_fromUtf8("menuAjuda_2"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionCadastrar_produto = QtGui.QAction(MainWindow)
        self.actionCadastrar_produto.setObjectName(_fromUtf8("actionCadastrar_produto"))
        self.actionCadastrar_item_card_pio = QtGui.QAction(MainWindow)
        self.actionCadastrar_item_card_pio.setObjectName(_fromUtf8("actionCadastrar_item_card_pio"))
        self.actionCadastrar_funcion_rio = QtGui.QAction(MainWindow)
        self.actionCadastrar_funcion_rio.setObjectName(_fromUtf8("actionCadastrar_funcion_rio"))
        self.actionSair = QtGui.QAction(MainWindow)
        self.actionSair.setObjectName(_fromUtf8("actionSair"))
        self.actionCadastrar_novo_item = QtGui.QAction(MainWindow)
        self.actionCadastrar_novo_item.setCheckable(False)
        self.actionCadastrar_novo_item.setChecked(False)
        self.actionCadastrar_novo_item.setObjectName(_fromUtf8("actionCadastrar_novo_item"))
        self.actionAtualizar_estoque = QtGui.QAction(MainWindow)
        self.actionAtualizar_estoque.setObjectName(_fromUtf8("actionAtualizar_estoque"))
        self.actionAtualizar_Estoque = QtGui.QAction(MainWindow)
        self.actionAtualizar_Estoque.setObjectName(_fromUtf8("actionAtualizar_Estoque"))
        self.actionSair_2 = QtGui.QAction(MainWindow)
        self.actionSair_2.setObjectName(_fromUtf8("actionSair_2"))
        self.actionConsultar_produto = QtGui.QAction(MainWindow)
        self.actionConsultar_produto.setObjectName(_fromUtf8("actionConsultar_produto"))
        self.actionConsultar_funcion_rio = QtGui.QAction(MainWindow)
        self.actionConsultar_funcion_rio.setObjectName(_fromUtf8("actionConsultar_funcion_rio"))
        self.actionConsultar_Estoque = QtGui.QAction(MainWindow)
        self.actionConsultar_Estoque.setObjectName(_fromUtf8("actionConsultar_Estoque"))
        self.actionSair_3 = QtGui.QAction(MainWindow)
        self.actionSair_3.setObjectName(_fromUtf8("actionSair_3"))
        self.actionSupore = QtGui.QAction(MainWindow)
        self.actionSupore.setObjectName(_fromUtf8("actionSupore"))
        self.actionSair_4 = QtGui.QAction(MainWindow)
        self.actionSair_4.setObjectName(_fromUtf8("actionSair_4"))
        self.actionSair_5 = QtGui.QAction(MainWindow)
        self.actionSair_5.setObjectName(_fromUtf8("actionSair_5"))
        self.actionVendas_por_per_odo = QtGui.QAction(MainWindow)
        self.actionVendas_por_per_odo.setObjectName(_fromUtf8("actionVendas_por_per_odo"))
        self.actionRelat_rio_por_per_odo = QtGui.QAction(MainWindow)
        self.actionRelat_rio_por_per_odo.setObjectName(_fromUtf8("actionRelat_rio_por_per_odo"))
        self.actionRelat_rio_por_produto = QtGui.QAction(MainWindow)
        self.actionRelat_rio_por_produto.setObjectName(_fromUtf8("actionRelat_rio_por_produto"))
        self.actionSobre = QtGui.QAction(MainWindow)
        self.actionSobre.setObjectName(_fromUtf8("actionSobre"))
        self.actionTool = QtGui.QAction(MainWindow)

        self.actionTool = QtGui.QAction(QtGui.QIcon('um.png'), 'Tolls', MainWindow)
        self.actionTool.setObjectName(_fromUtf8("actionTool"))

        self.actionSearch = QtGui.QAction(QtGui.QIcon('dois.png'), 'Tolls', MainWindow)
        self.actionSearch.setObjectName(_fromUtf8("actionSearch"))

        self.actionFood = QtGui.QAction(QtGui.QIcon('tres.png'), 'Tolls', MainWindow)
        self.actionFood.setObjectName(_fromUtf8("actionFood"))

        self.actionDrink = QtGui.QAction(QtGui.QIcon('quatro.png'), 'Tolls', MainWindow)
        self.actionDrink.setObjectName(_fromUtf8("actionDrink"))

        self.actionPhone = QtGui.QAction(QtGui.QIcon('cinco.png'), 'Tolls', MainWindow)
        self.actionPhone.setObjectName(_fromUtf8("actionPhone"))

        self.actionCalendar = QtGui.QAction(QtGui.QIcon('seis.png'), 'Tolls', MainWindow)
        self.actionCalendar.setObjectName(_fromUtf8("actionCalendar"))

        self.actionBd = QtGui.QAction(QtGui.QIcon('sete.png'), 'Tolls', MainWindow)
        self.actionBd.setObjectName(_fromUtf8("actionBd"))

        self.actionCredit = QtGui.QAction(QtGui.QIcon('oito.png'), 'Tolls', MainWindow)
        self.actionCredit.setObjectName(_fromUtf8("actionCredit"))

        self.actionSignin = QtGui.QAction(QtGui.QIcon('nove.png'), 'Tolls', MainWindow)
        self.actionSignin.setObjectName(_fromUtf8("actionSignin"))

        self.actionSignout = QtGui.QAction(QtGui.QIcon('dez.png'), 'Tolls', MainWindow)
        self.actionSignout.setObjectName(_fromUtf8("actionSignout"))

        self.menuCadastro.addAction(self.actionCadastrar_produto)
        self.menuCadastro.addAction(self.actionCadastrar_item_card_pio)
        self.menuCadastro.addAction(self.actionCadastrar_funcion_rio)
        self.menuCadastro.addSeparator()
        self.menuCadastro.addAction(self.actionSair)
        self.menuEstoque.addAction(self.actionCadastrar_novo_item)
        self.menuEstoque.addAction(self.actionAtualizar_estoque)
        self.menuEstoque.addAction(self.actionAtualizar_Estoque)
        self.menuEstoque.addSeparator()
        self.menuEstoque.addAction(self.actionSair_2)
        self.menuConsultar.addAction(self.actionConsultar_produto)
        self.menuConsultar.addAction(self.actionConsultar_funcion_rio)
        self.menuConsultar.addAction(self.actionConsultar_Estoque)
        self.menuConsultar.addSeparator()
        self.menuConsultar.addAction(self.actionSair_3)
        self.menuAjuda.addAction(self.actionSupore)
        self.menuAjuda.addSeparator()
        self.menuAjuda.addAction(self.actionSair_5)
        self.menuRelat_rio_de_vendas.addAction(self.actionVendas_por_per_odo)
        self.menuRelat_rio_de_estoque.addAction(self.actionRelat_rio_por_per_odo)
        self.menuRelat_rio_de_estoque.addAction(self.actionRelat_rio_por_produto)
        self.menuRelat_rio_de_estoque.addSeparator()
        self.menuRelat_rios.addAction(self.menuRelat_rio_de_vendas.menuAction())
        self.menuRelat_rios.addAction(self.menuRelat_rio_de_estoque.menuAction())
        self.menuRelat_rios.addSeparator()
        self.menuRelat_rios.addAction(self.actionSair_4)
        self.menuAjuda_2.addAction(self.actionSobre)
        self.menuAjuda_2.addSeparator()
        self.menubar.addAction(self.menuCadastro.menuAction())
        self.menubar.addAction(self.menuEstoque.menuAction())
        self.menubar.addAction(self.menuConsultar.menuAction())
        self.menubar.addAction(self.menuAjuda.menuAction())
        self.menubar.addAction(self.menuRelat_rios.menuAction())
        self.menubar.addAction(self.menuAjuda_2.menuAction())
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionTool)
        self.toolBar.addAction(self.actionSearch)
        self.toolBar.addAction(self.actionFood)
        self.toolBar.addAction(self.actionDrink)
        self.toolBar.addAction(self.actionPhone)
        self.toolBar.addAction(self.actionCalendar)
        self.toolBar.addAction(self.actionBd)
        self.toolBar.addAction(self.actionCredit)
        self.toolBar.addAction(self.actionSignin)
        self.toolBar.addAction(self.actionSignout)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Desktop", None))
        self.label_5.setText(_translate("MainWindow", "Volte Sempre !", None))
        self.label.setText(_translate("MainWindow", "Item:", None))
        self.label_3.setText(_translate("MainWindow", "Descrição:", None))
        self.label_2.setText(_translate("MainWindow", "Quantidade:", None))
        self.label_4.setText(_translate("MainWindow", "Subtotal:", None))
        self.pushButton_cancel_item.setText(_translate("MainWindow", "Cancelar Item", None))
        self.pushButton_cancel_venda.setText(_translate("MainWindow", "Cancelar Venda", None))
        self.pushButton_fechar_venda.setText(_translate("MainWindow", "Fechar Venda", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Caixa", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Mesas", None))
        self.menuCadastro.setTitle(_translate("MainWindow", "Cadastro", None))
        self.menuEstoque.setTitle(_translate("MainWindow", "Estoque", None))
        self.menuConsultar.setTitle(_translate("MainWindow", "Consultar", None))
        self.menuAjuda.setTitle(_translate("MainWindow", "Financeiro", None))
        self.menuRelat_rios.setTitle(_translate("MainWindow", "Relatórios", None))
        self.menuRelat_rio_de_vendas.setTitle(_translate("MainWindow", "Relatório de vendas", None))
        self.menuRelat_rio_de_estoque.setTitle(_translate("MainWindow", "Relatório de estoque", None))
        self.menuAjuda_2.setTitle(_translate("MainWindow", "Ajuda", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionCadastrar_produto.setText(_translate("MainWindow", "Cadastrar produto", None))
        self.actionCadastrar_item_card_pio.setText(_translate("MainWindow", "Cadastrar item cardápio", None))
        self.actionCadastrar_funcion_rio.setText(_translate("MainWindow", "Cadastrar funcionário", None))
        self.actionSair.setText(_translate("MainWindow", "Sair ", None))
        self.actionCadastrar_novo_item.setText(_translate("MainWindow", "Cadastrar novo item", None))
        self.actionAtualizar_estoque.setText(_translate("MainWindow", "Excluir item", None))
        self.actionAtualizar_Estoque.setText(_translate("MainWindow", "Atualizar Estoque", None))
        self.actionSair_2.setText(_translate("MainWindow", "Sair", None))
        self.actionConsultar_produto.setText(_translate("MainWindow", "Consultar produto", None))
        self.actionConsultar_funcion_rio.setText(_translate("MainWindow", "Consultar funcionário", None))
        self.actionConsultar_Estoque.setText(_translate("MainWindow", "Consultar Estoque", None))
        self.actionSair_3.setText(_translate("MainWindow", "Sair", None))
        self.actionSupore.setText(_translate("MainWindow", "Movimento financeiro", None))
        self.actionSair_4.setText(_translate("MainWindow", "Sair", None))
        self.actionSair_5.setText(_translate("MainWindow", "Sair", None))
        self.actionVendas_por_per_odo.setText(_translate("MainWindow", "Vendas por período", None))
        self.actionRelat_rio_por_per_odo.setText(_translate("MainWindow", "Relatório por período", None))
        self.actionRelat_rio_por_produto.setText(_translate("MainWindow", "Relatório por produto", None))
        self.actionSobre.setText(_translate("MainWindow", "Sobre...", None))
        self.actionTool.setText(_translate("MainWindow", "tool", None))
        self.actionTool.setToolTip(_translate("MainWindow", "<html><head/><body><p>play</p></body></html>", None))
        self.actionSearch.setText(_translate("MainWindow", "search", None))
        self.actionSearch.setToolTip(_translate("MainWindow", "search", None))
        self.actionFood.setText(_translate("MainWindow", "food", None))
        self.actionDrink.setText(_translate("MainWindow", "drink", None))
        self.actionPhone.setText(_translate("MainWindow", "phone", None))
        self.actionCalendar.setText(_translate("MainWindow", "calendar", None))
        self.actionCalendar.setToolTip(_translate("MainWindow", "Calendario", None))
        self.actionBd.setText(_translate("MainWindow", "bd", None))
        self.actionCredit.setText(_translate("MainWindow", "credit", None))
        self.actionSignin.setText(_translate("MainWindow", "signin", None))
        self.actionSignout.setText(_translate("MainWindow", "signout", None))
