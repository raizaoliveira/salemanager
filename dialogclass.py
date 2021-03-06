#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import sys

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

class Dialog_Tool(QtGui.QDialog):
    def __init__(self, parent):
        super(Dialog_Tool, self).__init__(parent)
        self.setWindowTitle(_fromUtf8("Configurações"))
        self.resize(400, 300)
        self.setObjectName("dialog_tool")
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.buttonBox = QtGui.QDialogButtonBox(self)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(20, 30, 161, 17))
        self.label.setObjectName("label")
        self.spinBox = QtGui.QSpinBox(self)
        self.spinBox.setGeometry(QtCore.QRect(180, 20, 60, 27))
        self.spinBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.spinBox.setMaximum(90)
        self.spinBox.setProperty("value", 0)
        self.spinBox.setObjectName("spinBox")

class Dialog_Cad_Prod(QtGui.QDialog):
    def __init__(self, parent):
        super(Dialog_Cad_Prod, self).__init__(parent)
        self.setObjectName(_fromUtf8("Dialog"))
        self.resize(399, 327)
        self.buttonBox = QtGui.QDialogButtonBox(self)
        self.buttonBox.setGeometry(QtCore.QRect(10, 280, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(20, 20, 91, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 91, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit_2 = QtGui.QLineEdit(self)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 20, 301, 31))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.spinBox = QtGui.QSpinBox(self)
        self.spinBox.setGeometry(QtCore.QRect(110, 80, 60, 27))
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.label_3 = QtGui.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(10, 130, 101, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.doubleSpinBox = QtGui.QDoubleSpinBox(self)
        self.doubleSpinBox.setGeometry(QtCore.QRect(110, 120, 62, 27))
        self.doubleSpinBox.setObjectName(_fromUtf8("doubleSpinBox"))
        self.label_4 = QtGui.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(10, 170, 81, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self)
        self.plainTextEdit.setGeometry(QtCore.QRect(80, 170, 291, 91))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))

        self.retranslateUi(self)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), self.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), self.reject)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Cadastro de Produto", None))
        self.label.setText(_translate("Dialog", "Nome:", None))
        self.label_2.setText(_translate("Dialog", "Quantidade:", None))
        self.label_3.setText(_translate("Dialog", "Valor Unitario:", None))
        self.label_4.setText(_translate("Dialog", "Descrição:", None))


class Dialog_Cad_Item(QtGui.QDialog):
    def __init__(self, parent):
        super(Dialog_Cad_Item, self).__init__(parent)
        self.setObjectName(_fromUtf8("Dialog"))
        self.resize(400, 300)
        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(10, 30, 131, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(140, 20, 241, 27))
        self.lineEdit.setText(_fromUtf8(""))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label_2 = QtGui.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 111, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit_2 = QtGui.QLineEdit(self)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 60, 241, 27))
        self.lineEdit_2.setText(_fromUtf8(""))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label_3 = QtGui.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(10, 106, 121, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.textEdit = QtGui.QTextEdit(self)
        self.textEdit.setGeometry(QtCore.QRect(140, 110, 241, 91))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.pushButton = QtGui.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(280, 240, 98, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 240, 98, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Cadastro de Produto", None))
        self.label.setText(_translate("Dialog", "Nome do produto:", None))
        self.label_2.setText(_translate("Dialog", "Preço:", None))
        self.label_3.setText(_translate("Dialog", "Descrição:", None))
        self.pushButton.setText(_translate("Dialog", "Salvar", None))
        self.pushButton_2.setText(_translate("Dialog", "Cancelar", None))


class Dialog_Cons_Est(QtGui.QDialog):
    def __init__(self, parent):
        super(Dialog_Cons_Est, self).__init__(parent)
        self.setObjectName(_fromUtf8("Dialog"))
        self.resize(409, 106)
        self.buttonBox = QtGui.QDialogButtonBox(self)
        self.buttonBox.setGeometry(QtCore.QRect(50, 70, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(10, 30, 131, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(140, 30, 261, 31))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))

        self.retranslateUi(self)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), self.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), self.reject)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Consultar estoque", None))
        self.label.setText(_translate("Dialog", "Nome do produto:", None))


class Dialog_Cad_Func(QtGui.QDialog):
    def __init__(self, parent):
        super(Dialog_Cad_Func, self).__init__(parent)
        self.setObjectName(_fromUtf8("Dialog"))
        self.resize(552, 342)
        self.setMinimumSize(QtCore.QSize(0, 30))
        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(9, 9, 41, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_4 = QtGui.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(230, 10, 91, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.EditName = QtGui.QLineEdit(self)
        self.EditName.setGeometry(QtCore.QRect(9, 32, 191, 40))
        self.EditName.setMinimumSize(QtCore.QSize(0, 40))
        self.EditName.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.EditName.setMaxLength(20)
        self.EditName.setObjectName(_fromUtf8("EditName"))
        self.EditSobrenome = QtGui.QLineEdit(self)
        self.EditSobrenome.setGeometry(QtCore.QRect(227, 32, 281, 40))
        self.EditSobrenome.setMinimumSize(QtCore.QSize(0, 40))
        self.EditSobrenome.setMaxLength(50)
        self.EditSobrenome.setObjectName(_fromUtf8("EditSobrenome"))
        self.label_6 = QtGui.QLabel(self)
        self.label_6.setGeometry(QtCore.QRect(230, 110, 131, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.dateEdit = QtGui.QDateEdit(self)
        self.dateEdit.setGeometry(QtCore.QRect(380, 100, 121, 40))
        self.dateEdit.setMinimumSize(QtCore.QSize(0, 40))
        self.dateEdit.setDate(QtCore.QDate(2000, 1, 2))
        self.dateEdit.setMinimumDate(QtCore.QDate(1752, 9, 15))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.EditPass = QtGui.QLineEdit(self)
        self.EditPass.setGeometry(QtCore.QRect(10, 180, 191, 40))
        self.EditPass.setMinimumSize(QtCore.QSize(0, 40))
        self.EditPass.setMaxLength(8)
        self.EditPass.setObjectName(_fromUtf8("EditPass"))
        self.label_5 = QtGui.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(10, 240, 191, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.EditPswConf = QtGui.QLineEdit(self)
        self.EditPswConf.setGeometry(QtCore.QRect(10, 260, 191, 40))
        self.EditPswConf.setMinimumSize(QtCore.QSize(0, 40))
        self.EditPswConf.setMaxLength(8)
        self.EditPswConf.setObjectName(_fromUtf8("EditPswConf"))
        self.buttonBox = QtGui.QDialogButtonBox(self)
        self.buttonBox.setGeometry(QtCore.QRect(360, 310, 176, 27))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label_7 = QtGui.QLabel(self)
        self.label_7.setGeometry(QtCore.QRect(10, 160, 51, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.EditCPF = QtGui.QLineEdit(self)
        self.EditCPF.setGeometry(QtCore.QRect(230, 180, 281, 40))
        self.EditCPF.setMinimumSize(QtCore.QSize(0, 40))
        self.EditCPF.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly|QtCore.Qt.ImhPreferNumbers)
        self.EditCPF.setInputMask(_fromUtf8(""))
        self.EditCPF.setMaxLength(11)
        self.EditCPF.setObjectName(_fromUtf8("EditCPF"))
        self.label_2 = QtGui.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(240, 160, 41, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.groupBox = QtGui.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(10, 90, 212, 70))
        self.groupBox.setMinimumSize(QtCore.QSize(0, 70))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(10, 20, 98, 22))
        self.radioButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 40, 115, 22))
        self.radioButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.label_3 = QtGui.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(230, 240, 66, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.Editphone = QtGui.QLineEdit(self)
        self.Editphone.setGeometry(QtCore.QRect(230, 260, 281, 40))
        self.Editphone.setMinimumSize(QtCore.QSize(0, 40))
        self.Editphone.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly|QtCore.Qt.ImhPreferNumbers)
        self.Editphone.setInputMask(_fromUtf8("()xxxx-xxxx"))
        self.Editphone.setMaxLength(11)
        self.Editphone.setObjectName(_fromUtf8("Editphone"))

        self.retranslateUi(self)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), self.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), self.reject)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Nome", None))
        self.label_4.setText(_translate("Dialog", "Sobrenome", None))
        self.label_6.setText(_translate("Dialog", "Data Nascimento", None))
        self.dateEdit.setDisplayFormat(_translate("Dialog", "dd/MM/yyyy", None))
        self.label_5.setText(_translate("Dialog", "Digite a senha novamente", None))
        self.label_7.setText(_translate("Dialog", "Senha", None))
        self.label_2.setText(_translate("Dialog", "CPF", None))
        self.groupBox.setTitle(_translate("Dialog", "Sexo", None))
        self.radioButton.setText(_translate("Dialog", "Feminino", None))
        self.radioButton_2.setText(_translate("Dialog", "Masculino", None))
        self.label_3.setText(_translate("Dialog", "Telefone", None))


