# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_cadastro.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class tela_cadastro(object):
    def setupUi(self, tela_cadastro):
        tela_cadastro.setObjectName("tela_cadastro")
        tela_cadastro.resize(900, 748)
        tela_cadastro.setMinimumSize(QtCore.QSize(540, 680))
        tela_cadastro.setMaximumSize(QtCore.QSize(1024, 748))
        tela_cadastro.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(tela_cadastro)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(540, 650))
        self.frame.setMaximumSize(QtCore.QSize(1024, 748))
        self.frame.setStyleSheet("background-color: rgb(4, 14, 66);\n"
"color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(0)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(180, 70, 531, 531))
        self.frame_2.setStyleSheet("background-color:rgba(255, 253, 253, 38);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setGeometry(QtCore.QRect(10, 50, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border-radius: 5px;\n"
"background-color: rgba(255, 255, 255, 198);\n"
"border: 1px solid rgba(3, 20, 52, 150);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(270, 50, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("border-radius: 5px;\n"
"background-color: rgba(255, 255, 255, 198);\n"
"border: 1px solid rgba(3, 20, 52, 150);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(70, 130, 401, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("border-radius: 5px;\n"
"background-color: rgba(255, 255, 255, 198);\n"
"border: 1px solid rgba(3, 20, 52, 150);\n"
"color: rgb(0, 0, 0);\n"
"")
        self.lineEdit_3.setMaxLength(11)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(70, 200, 401, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("border-radius: 5px;\n"
"background-color: rgba(255, 255, 255, 198);\n"
"border: 1px solid rgba(3, 20, 52, 150);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_4.setMaxLength(16)
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(70, 340, 401, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setStyleSheet("border-radius: 5px;\n"
"background-color: rgba(255, 255, 255, 198);\n"
"border: 1px solid rgba(3, 20, 52, 150);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_6.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_7.setGeometry(QtCore.QRect(70, 400, 401, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setStyleSheet("border-radius: 5px;\n"
"background-color: rgba(255, 255, 255, 198);\n"
"border: 1px solid rgba(3, 20, 52, 150);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_7.setMaxLength(16)
        self.lineEdit_7.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_7.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(90, 470, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"border-radius: 5px;\n"
"background-color: rgb(138, 226, 52);\n"
"border: 2px solid rgba(3, 20, 52, 150);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"background-color: rgb(78, 154, 6);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(330, 470, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"border-radius: 5px;\n"
"background-color: rgb(239, 41, 41);\n"
"border: 1px solid rgba(3, 20, 52, 150);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(164, 0, 0);\n"
"color: rgb(0, 0, 0)\n"
"\n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_8.setGeometry(QtCore.QRect(70, 270, 401, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setStyleSheet("border-radius: 5px;\n"
"background-color: rgba(255, 255, 255, 198);\n"
"border: 1px solid rgba(3, 20, 52, 150);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_8.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(180, 30, 531, 41))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.frame)
        tela_cadastro.setCentralWidget(self.centralwidget)

        self.retranslateUi(tela_cadastro)
        QtCore.QMetaObject.connectSlotsByName(tela_cadastro)

    def retranslateUi(self, tela_cadastro):
        _translate = QtCore.QCoreApplication.translate
        tela_cadastro.setWindowTitle(_translate("tela_cadastro", "MainWindow"))
        self.lineEdit.setPlaceholderText(_translate("tela_cadastro", "Nome"))
        self.lineEdit_2.setPlaceholderText(_translate("tela_cadastro", "Sobrenome"))
        self.lineEdit_3.setPlaceholderText(_translate("tela_cadastro", "Cpf"))
        self.lineEdit_4.setPlaceholderText(_translate("tela_cadastro", "Numero da conta"))
        self.lineEdit_6.setPlaceholderText(_translate("tela_cadastro", "Limite da Conta"))
        self.lineEdit_7.setPlaceholderText(_translate("tela_cadastro", "Senha da Conta"))
        self.pushButton.setText(_translate("tela_cadastro", "Cadastrar"))
        self.pushButton_2.setText(_translate("tela_cadastro", "Cancelar"))
        self.lineEdit_8.setPlaceholderText(_translate("tela_cadastro", "Saldo"))
        self.label.setText(_translate("tela_cadastro", "Criar Conta"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    tela_cadastro = QtWidgets.QMainWindow()
    ui = Ui_tela_cadastro()
    ui.setupUi(tela_cadastro)
    tela_cadastro.show()
    sys.exit(app.exec_())