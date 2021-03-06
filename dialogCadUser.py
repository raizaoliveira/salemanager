# -*- coding: utf-8 -*-
#commit

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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(552, 342)
        Dialog.setMinimumSize(QtCore.QSize(0, 30))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(9, 9, 41, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(230, 10, 91, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.EditName = QtGui.QLineEdit(Dialog)
        self.EditName.setGeometry(QtCore.QRect(9, 32, 191, 40))
        self.EditName.setMinimumSize(QtCore.QSize(0, 40))
        self.EditName.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.EditName.setMaxLength(20)
        self.EditName.setObjectName(_fromUtf8("EditName"))
        self.EditSobrenome = QtGui.QLineEdit(Dialog)
        self.EditSobrenome.setGeometry(QtCore.QRect(227, 32, 281, 40))
        self.EditSobrenome.setMinimumSize(QtCore.QSize(0, 40))
        self.EditSobrenome.setMaxLength(50)
        self.EditSobrenome.setObjectName(_fromUtf8("EditSobrenome"))
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(230, 110, 131, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.dateEdit = QtGui.QDateEdit(Dialog)
        self.dateEdit.setGeometry(QtCore.QRect(380, 100, 121, 40))
        self.dateEdit.setMinimumSize(QtCore.QSize(0, 40))
        self.dateEdit.setDate(QtCore.QDate(2000, 1, 2))
        self.dateEdit.setMinimumDate(QtCore.QDate(1752, 9, 15))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.EditPass = QtGui.QLineEdit(Dialog)
        self.EditPass.setGeometry(QtCore.QRect(10, 180, 191, 40))
        self.EditPass.setMinimumSize(QtCore.QSize(0, 40))
        self.EditPass.setMaxLength(8)
        self.EditPass.setObjectName(_fromUtf8("EditPass"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 240, 191, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.EditPswConf = QtGui.QLineEdit(Dialog)
        self.EditPswConf.setGeometry(QtCore.QRect(10, 260, 191, 40))
        self.EditPswConf.setMinimumSize(QtCore.QSize(0, 40))
        self.EditPswConf.setMaxLength(8)
        self.EditPswConf.setObjectName(_fromUtf8("EditPswConf"))
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(360, 310, 176, 27))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(10, 160, 51, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.EditCPF = QtGui.QLineEdit(Dialog)
        self.EditCPF.setGeometry(QtCore.QRect(230, 180, 281, 40))
        self.EditCPF.setMinimumSize(QtCore.QSize(0, 40))
        self.EditCPF.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly|QtCore.Qt.ImhPreferNumbers)
        self.EditCPF.setInputMask(_fromUtf8(""))
        self.EditCPF.setMaxLength(11)
        self.EditCPF.setObjectName(_fromUtf8("EditCPF"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(240, 160, 41, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.groupBox = QtGui.QGroupBox(Dialog)
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
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(230, 240, 66, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.Editphone = QtGui.QLineEdit(Dialog)
        self.Editphone.setGeometry(QtCore.QRect(230, 260, 281, 40))
        self.Editphone.setMinimumSize(QtCore.QSize(0, 40))
        self.Editphone.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly|QtCore.Qt.ImhPreferNumbers)
        self.Editphone.setInputMask(_fromUtf8("()xxxx-xxxx"))
        self.Editphone.setMaxLength(11)
        self.Editphone.setObjectName(_fromUtf8("Editphone"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

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


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

