# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_historico.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class tela_historico(object):
    def setupUi(self, tela_historico):
        tela_historico.setObjectName("tela_historico")
        tela_historico.resize(900, 748)
        tela_historico.setMinimumSize(QtCore.QSize(540, 650))
        tela_historico.setMaximumSize(QtCore.QSize(1024, 748))
        self.centralwidget = QtWidgets.QWidget(tela_historico)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(4, 14, 66);\n"
"color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(320, -10, 201, 131))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("imagens/icon_extrato2.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(360, 620, 141, 41))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"\n"
"background-color: rgb(52, 101, 164);    \n"
"border-radius: 10px;\n"
"border: 2px solid rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(52, 101, 164);\n"
"    color: rgb(0, 0, 0);\n"
"    border: 2px solid rgb(32, 74, 135);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(190, 160, 471, 431))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("background-color: rgba(51, 72, 113, 170);\n"
"color:  rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(180, 110, 471, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.frame)
        tela_historico.setCentralWidget(self.centralwidget)

        self.retranslateUi(tela_historico)
        QtCore.QMetaObject.connectSlotsByName(tela_historico)

    def retranslateUi(self, tela_historico):
        _translate = QtCore.QCoreApplication.translate
        tela_historico.setWindowTitle(_translate("tela_historico", "MainWindow"))
        self.pushButton_2.setText(_translate("tela_historico", "Menu"))
        self.textEdit.setHtml(_translate("tela_historico", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:17pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">---------------------------------------------------</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">skqmklsmlq    mlskmqmmqklsml</p></body></html>"))
        self.label.setText(_translate("tela_historico", "Historico de transações"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    tela_historico = QtWidgets.QMainWindow()
    ui = Ui_tela_historico()
    ui.setupUi(tela_historico)
    tela_historico.show()
    sys.exit(app.exec_())