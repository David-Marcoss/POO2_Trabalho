# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_transferencia.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class tela_transferencia(object):
    def setupUi(self, tela_transferencia):
        tela_transferencia.setObjectName("tela_transferencia")
        tela_transferencia.resize(900, 748)
        tela_transferencia.setMinimumSize(QtCore.QSize(540, 650))
        tela_transferencia.setMaximumSize(QtCore.QSize(1024, 748))
        self.centralwidget = QtWidgets.QWidget(tela_transferencia)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(4, 14, 66);\n"
"color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(200, 160, 481, 391))
        self.frame_2.setStyleSheet("background-color: rgba(1, 0, 0, 99);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setGeometry(QtCore.QRect(110, 150, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border-radius: 5px;\n"
"background-color: rgba(255, 255, 255, 198);\n"
"border: 1px solid rgba(3, 20, 52, 150);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit.setText("")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(0, 10, 481, 31))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(60, 320, 131, 31))
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
        self.pushButton_2.setGeometry(QtCore.QRect(290, 320, 131, 31))
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
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 70, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(114, 159, 207);\n"
"border: 1px solid rgba(3, 20, 52, 150);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setPlaceholderText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(140, 220, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("border-radius: 5px;\n"
"background-color: rgba(255, 255, 255, 198);\n"
"border: 1px solid rgba(3, 20, 52, 150);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(10, 150, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(10, 220, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(370, 60, 141, 101))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("imagens/icons8-transferência-de-dinheiro-64.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(260, 10, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Sawasdee")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_2.raise_()
        self.frame_2.raise_()
        self.label_6.raise_()
        self.verticalLayout.addWidget(self.frame)
        tela_transferencia.setCentralWidget(self.centralwidget)

        self.retranslateUi(tela_transferencia)
        QtCore.QMetaObject.connectSlotsByName(tela_transferencia)

    def retranslateUi(self, tela_transferencia):
        _translate = QtCore.QCoreApplication.translate
        tela_transferencia.setWindowTitle(_translate("tela_transferencia", "MainWindow"))
        self.lineEdit.setPlaceholderText(_translate("tela_transferencia", "Digite o valor da transferencia"))
        self.label.setText(_translate("tela_transferencia", "Transferir"))
        self.pushButton.setText(_translate("tela_transferencia", "Transferir"))
        self.pushButton_2.setText(_translate("tela_transferencia", "Cancelar"))
        self.label_3.setText(_translate("tela_transferencia", "Saldo"))
        self.lineEdit_5.setPlaceholderText(_translate("tela_transferencia", "Numero da conta que você vai transferir"))
        self.label_4.setText(_translate("tela_transferencia", "Valor"))
        self.label_5.setText(_translate("tela_transferencia", "Conta Destino"))
        self.label_6.setText(_translate("tela_transferencia", "My Bank"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    tela_transferencia = QtWidgets.QMainWindow()
    ui = Ui_tela_transferencia()
    ui.setupUi(tela_transferencia)
    tela_transferencia.show()
    sys.exit(app.exec_())