# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_deposito.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class tela_deposito(object):
    def setupUi(self, tela_deposito):
        tela_deposito.setObjectName("tela_deposito")
        tela_deposito.resize(900, 748)
        tela_deposito.setMinimumSize(QtCore.QSize(540, 650))
        tela_deposito.setMaximumSize(QtCore.QSize(1024, 748))
        self.centralwidget = QtWidgets.QWidget(tela_deposito)
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
        self.frame_2.setGeometry(QtCore.QRect(220, 170, 481, 301))
        self.frame_2.setStyleSheet("background-color: rgba(1, 0, 0, 99);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setGeometry(QtCore.QRect(120, 80, 251, 31))
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
        self.pushButton.setGeometry(QtCore.QRect(70, 170, 131, 31))
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
        self.pushButton_2.setGeometry(QtCore.QRect(290, 170, 131, 31))
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
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(30, 80, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(380, 50, 141, 101))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("imagens/icons8-dep??sito-64.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(260, 10, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Sawasdee")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.frame)
        tela_deposito.setCentralWidget(self.centralwidget)

        self.retranslateUi(tela_deposito)
        QtCore.QMetaObject.connectSlotsByName(tela_deposito)

    def retranslateUi(self, tela_deposito):
        _translate = QtCore.QCoreApplication.translate
        tela_deposito.setWindowTitle(_translate("tela_deposito", "MainWindow"))
        self.lineEdit.setPlaceholderText(_translate("tela_deposito", "Digite o valor do deposito"))
        self.label.setText(_translate("tela_deposito", "Deposito"))
        self.pushButton.setText(_translate("tela_deposito", "Depositar"))
        self.pushButton_2.setText(_translate("tela_deposito", "Cancelar"))
        self.label_4.setText(_translate("tela_deposito", "Valor"))
        self.label_5.setText(_translate("tela_deposito", "My Bank"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    tela_deposito = QtWidgets.QMainWindow()
    ui = Ui_tela_deposito()
    ui.setupUi(tela_deposito)
    tela_deposito.show()
    sys.exit(app.exec_())
