# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_dados.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class tela_dados(object):
    def setupUi(self, tela_dados):
        tela_dados.setObjectName("tela_dados")
        tela_dados.resize(900, 748)
        tela_dados.setMinimumSize(QtCore.QSize(540, 650))
        tela_dados.setMaximumSize(QtCore.QSize(1024, 748))
        self.centralwidget = QtWidgets.QWidget(tela_dados)
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
        self.frame_2.setGeometry(QtCore.QRect(190, 120, 530, 554))
        self.frame_2.setStyleSheet("background-color:rgba(255, 253, 253, 38);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setGeometry(QtCore.QRect(230, 70, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border-radius: 5px;\n"
"background-color: rgba(255, 255, 255, 198);\n"
"border: 1px solid rgba(3, 20, 52, 150);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setPlaceholderText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(230, 130, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("border-radius: 5px;\n"
"background-color: rgba(255, 255, 255, 198);\n"
"border: 1px solid rgba(3, 20, 52, 150);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setPlaceholderText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(230, 190, 251, 31))
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
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setPlaceholderText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(230, 250, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("border-radius: 5px;\n"
"background-color: rgba(255, 255, 255, 198);\n"
"border: 1px solid rgba(3, 20, 52, 150);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_4.setMaxLength(16)
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setPlaceholderText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(230, 320, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("border-radius: 5px;\n"
"background-color: rgba(255, 255, 255, 198);\n"
"border: 1px solid rgba(3, 20, 52, 150);\n"
"color: rgb(0, 0, 0);\n"
"")
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_5.setPlaceholderText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(230, 390, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setStyleSheet("border-radius: 5px;\n"
"background-color: rgba(255, 255, 255, 198);\n"
"border: 1px solid rgba(3, 20, 52, 150);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_6.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_6.setReadOnly(True)
        self.lineEdit_6.setPlaceholderText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(16, 70, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(32, 74, 135);\n"
"border-radius: 3px;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(20, 130, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(32, 74, 135);\n"
"border-radius: 3px;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(20, 190, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(32, 74, 135);\n"
"border-radius: 3px;")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(20, 250, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgb(32, 74, 135);\n"
"border-radius: 3px;")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(20, 320, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: rgb(32, 74, 135);\n"
"border-radius: 3px;")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(20, 390, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: rgb(32, 74, 135);\n"
"border-radius: 3px;")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(70, 480, 141, 41))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"\n"
"background-color: rgb(52, 101, 164);    \n"
"border-radius: 10px;\n"
"border: 2px rgb(2, 19, 44);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(52, 101, 164);\n"
"    border: 5px solid rgb(32, 74, 135);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_3.setGeometry(QtCore.QRect(300, 480, 141, 41))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"\n"
"background-color: rgb(0, 0, 0);    \n"
"border-radius: 10px;\n"
"border: 2px rgb(2, 19, 44);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border: 5px solid rgb(2, 19, 44);\n"
"\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(190, 80, 531, 41))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(270, 20, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Sawasdee")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.frame)
        tela_dados.setCentralWidget(self.centralwidget)

        self.retranslateUi(tela_dados)
        QtCore.QMetaObject.connectSlotsByName(tela_dados)

    def retranslateUi(self, tela_dados):
        _translate = QtCore.QCoreApplication.translate
        tela_dados.setWindowTitle(_translate("tela_dados", "MainWindow"))
        self.label.setText(_translate("tela_dados", "Nome"))
        self.label_2.setText(_translate("tela_dados", "Sobrenome"))
        self.label_5.setText(_translate("tela_dados", "Cpf"))
        self.label_6.setText(_translate("tela_dados", "Numero da conta"))
        self.label_7.setText(_translate("tela_dados", "Saldo"))
        self.label_8.setText(_translate("tela_dados", "Limite"))
        self.pushButton_2.setText(_translate("tela_dados", "Menu"))
        self.pushButton_3.setText(_translate("tela_dados", "Remover conta"))
        self.label_9.setText(_translate("tela_dados", "Dados da Conta"))
        self.label_4.setText(_translate("tela_dados", "My Bank"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    tela = QtWidgets.QMainWindow()
    ui = tela_dados()
    ui.setupUi(tela)
    tela.show()
    sys.exit(app.exec_())
