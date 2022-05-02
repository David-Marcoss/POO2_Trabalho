
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets


from tela_cadastro import tela_cadastro
from tela_dados import tela_dados
from tela_deposito import tela_deposito
from tela_extrato import tela_extrato
from tela_historico import tela_historico
from tela_login import tela_login
from tela_menu import tela_menu
from tela_saque import tela_saque
from tela_transferencia import tela_transferencia

import sys
sys.path.insert(1, '../')

from funcoes_auxiliares import concatenar_operacao
from cliente import conectar_servidor

class main_telas(QtWidgets.QWidget):

    def setupUi(self,Main):
        Main.setObjectName('Main')
        Main.resize(900, 748) #tamanho tela

        self.QtStack = QtWidgets.QStackedLayout()

        self.QtStack0 = QtWidgets.QMainWindow()
        self.QtStack1 = QtWidgets.QMainWindow()
        self.QtStack2 = QtWidgets.QMainWindow()
        self.QtStack3 = QtWidgets.QMainWindow()
        self.QtStack4 = QtWidgets.QMainWindow()
        self.QtStack5 = QtWidgets.QMainWindow()
        self.QtStack6 = QtWidgets.QMainWindow()
        self.QtStack7 = QtWidgets.QMainWindow()
        self.QtStack8 = QtWidgets.QMainWindow()

        self.tela_login = tela_login()
        self.tela_login.setupUi(self.QtStack0)

        self.tela_cadastro = tela_cadastro()
        self.tela_cadastro.setupUi(self.QtStack1)

        self.tela_menu = tela_menu()
        self.tela_menu.setupUi(self.QtStack2)


        self.tela_dados = tela_dados()
        self.tela_dados.setupUi(self.QtStack3)

        self.tela_extrato = tela_extrato()
        self.tela_extrato.setupUi(self.QtStack4)

        self.tela_saque = tela_saque()
        self.tela_saque.setupUi(self.QtStack5)

        self.tela_deposito = tela_deposito()
        self.tela_deposito.setupUi(self.QtStack6)

        self.tela_transferencia = tela_transferencia()
        self.tela_transferencia.setupUi(self.QtStack7)

        self.tela_historico = tela_historico()
        self.tela_historico.setupUi(self.QtStack8)

        self.QtStack.addWidget(self.QtStack0)  #tela login
        self.QtStack.addWidget(self.QtStack1)  #tela cadatro
        self.QtStack.addWidget(self.QtStack2)  #tela menu
        self.QtStack.addWidget(self.QtStack3)  #tela dados
        self.QtStack.addWidget(self.QtStack4)  #tela extrato
        self.QtStack.addWidget(self.QtStack5)  #tela saque
        self.QtStack.addWidget(self.QtStack6)  #tela deposito
        self.QtStack.addWidget(self.QtStack7)  #tela trasnferencia
        self.QtStack.addWidget(self.QtStack8)  #tela historico


class main(QMainWindow,main_telas):

    def __init__(self,parent=None):
        super(main_telas,self).__init__(parent)
        self.setupUi(self)

        self.conectar_servidor = conectar_servidor()

        self.tela_login.pushButton.clicked.connect(self.botao_logar)
        self.tela_login.pushButton_2.clicked.connect(self.abrir_telaCadastro)

        self.tela_cadastro.pushButton.clicked.connect(self.Botao_cadastrar_conta)
        self.tela_cadastro.pushButton_2.clicked.connect(self.voltarLogin)

        self.tela_menu.pushButton.clicked.connect(self.abrir_telaExtrato)
        self.tela_menu.pushButton_3.clicked.connect(self.abrir_telaSacar)
        self.tela_menu.pushButton_4.clicked.connect(self.abrir_telaDepositar)
        self.tela_menu.pushButton_5.clicked.connect(self.abrir_telaTransferencia)
        self.tela_menu.pushButton_6.clicked.connect(self.abrir_telaHistorico)
        self.tela_menu.pushButton_7.clicked.connect(self.abrir_telaDados)
        self.tela_menu.pushButton_8.clicked.connect(self.voltarLogin)

        self.tela_dados.pushButton_2.clicked.connect(self.abrir_telaMenu)
        self.tela_dados.pushButton_3.clicked.connect(self.botao_remover_conta)

        self.tela_saque.pushButton.clicked.connect(self.botao_sacar)
        self.tela_saque.pushButton_2.clicked.connect(self.abrir_telaMenu)

        self.tela_extrato.pushButton_2.clicked.connect(self.abrir_telaMenu)

        self.tela_deposito.pushButton.clicked.connect(self.botao_depositar)
        self.tela_deposito.pushButton_2.clicked.connect(self.abrir_telaMenu)

        self.tela_transferencia.pushButton.clicked.connect(self.botao_transferencia)
        self.tela_transferencia.pushButton_2.clicked.connect(self.abrir_telaMenu)

        self.tela_historico.pushButton_2.clicked.connect(self.abrir_telaMenu)


    def Botao_cadastrar_conta(self):

        nome = self.tela_cadastro.lineEdit.text()
        sobrenome = self.tela_cadastro.lineEdit_2.text()
        cpf = self.tela_cadastro.lineEdit_3.text()
        nascimento = self.tela_cadastro.dateEdit.text()

        saldo = self.tela_cadastro.lineEdit_8.text()
        limite= self.tela_cadastro.lineEdit_6.text()
        senha = self.tela_cadastro.lineEdit_15.text()
        user =  self.tela_cadastro.lineEdit_7.text()


        if (nome != '' and cpf != '' and sobrenome != '' and nascimento != '' and saldo != '' and limite != '' and senha != '' and user != ''):

            msg = self.conectar_servidor.enviar_mensagem( concatenar_operacao( ['cadastrar',nome,sobrenome,nascimento,cpf,saldo,limite,senha,user]) )
            if msg != None:

                QMessageBox.information(None, 'msg',msg[1])

                self.tela_cadastro.lineEdit.setText('')
                self.tela_cadastro.lineEdit_2.setText('')
                self.tela_cadastro.lineEdit_3.setText('')
                self.tela_cadastro.lineEdit_8.setText('')
                self.tela_cadastro.lineEdit_6.setText('')
                self.tela_cadastro.lineEdit_7.setText('')
                self.tela_cadastro.lineEdit_15.setText('')

                if msg[0] == '0':
                    self.voltarLogin()
            else:
                self.voltarLogin()
                QMessageBox.information(None, 'msg', 'Desculpe Sistema fora do AR!!\nTente novamente mais tarde!!')

    def botao_logar(self):
        user = self.tela_login.lineEdit.text()
        senha = self.tela_login.lineEdit_2.text()

        if (user != '' and senha != ''):

            msg = self.conectar_servidor.enviar_mensagem(concatenar_operacao(['logar', user, senha]))
            self.tela_login.lineEdit.setText('')
            self.tela_login.lineEdit_2.setText('')

            if msg != None:
                if msg[0] == '0':
                    self.abrir_telaMenu()
                else:
                    QMessageBox.information(None, 'msg', msg[1])
            else:
                QMessageBox.information(None, 'msg', 'Desculpe Sistema fora do AR!!\nTente novamente mais tarde!!')

        else:
            QMessageBox.information(None, 'msg', 'Preencha todos os campos para fazer login !!')



    def botao_sacar(self):

        valor = self.tela_saque.lineEdit.text()

        if(valor != ''):
            msg = self.conectar_servidor.enviar_mensagem(concatenar_operacao(['sacar',valor]))
            QMessageBox.information(None, 'msg', msg[1])
            self.tela_saque.lineEdit.setText('')

            if msg[0] == '0':
                self.abrir_telaMenu()

        else:
            QMessageBox.information(None, 'msg', 'Preencha todos os campos para concluir Saque!! ')

    def botao_depositar(self):
        valor = self.tela_deposito.lineEdit.text()

        if(valor != ''):

            msg = self.conectar_servidor.enviar_mensagem(concatenar_operacao(['depositar',valor]))
            QMessageBox.information(None, 'msg', msg[1])
            self.tela_deposito.lineEdit.setText('')

            if msg[0] == '0':
                self.abrir_telaMenu()
        else:
            QMessageBox.information(None, 'msg', 'Preencha todos os campos para concluir Deposito!! ')

    def botao_transferencia(self):
        valor = self.tela_transferencia.lineEdit.text()
        id_destino = self.tela_transferencia.lineEdit_5.text() #recebe o id da conta de destino

        if(valor != '' and id_destino != ''):

            msg = self.conectar_servidor.enviar_mensagem(concatenar_operacao(['transferir',id_destino,valor]))
            QMessageBox.information(None, 'msg', msg[1])

            self.tela_transferencia.lineEdit.setText('')
            self.tela_transferencia.lineEdit_5.setText('')

            if msg[0] == '0':
                self.abrir_telaMenu()
        else:
            self.tela_transferencia.lineEdit.setText('')
            self.tela_transferencia.lineEdit_5.setText('')
            QMessageBox.information(None, 'msg','Preencha todos os campos para concluir transferencia!! ')

    def abrir_telaCadastro(self):
        self.tela_login.lineEdit.setText('')
        self.tela_login.lineEdit_2.setText('')

        self.tela_cadastro.lineEdit.setText('')
        self.tela_cadastro.lineEdit_2.setText('')
        self.tela_cadastro.lineEdit_3.setText('')
        self.tela_cadastro.lineEdit_8.setText('')
        self.tela_cadastro.lineEdit_6.setText('')
        self.tela_cadastro.lineEdit_7.setText('')
        self.tela_cadastro.lineEdit_15.setText('')

        self.QtStack.setCurrentIndex(1)

    def abrir_telaMenu(self):
        msg = self.conectar_servidor.enviar_mensagem('dados menu')
        print(msg)

        if msg[0] == '0':

            self.tela_menu.lineEdit_5.setText(f"{msg[1]} ")
            self.tela_menu.lineEdit_8.setText(f"R$ {msg[2]} ")

        self.QtStack.setCurrentIndex(2)

    def abrir_telaDados(self):
        msg = self.conectar_servidor.enviar_mensagem('ver dados')
        print(msg)

        if msg[0] == '0':

            self.tela_dados.lineEdit.setText(f'{msg[1]}')
            self.tela_dados.lineEdit_2.setText(f'{msg[2]}')
            self.tela_dados.lineEdit_3.setText(f'{msg[3]}')
            self.tela_dados.lineEdit_4.setText(f'{msg[4]}')
            self.tela_dados.lineEdit_5.setText(f'R$ {msg[5]}')
            self.tela_dados.lineEdit_6.setText(f'R$ {msg[6]}')

        else:
            QMessageBox.information(None, 'msg', msg[1])

        self.QtStack.setCurrentIndex(3)

    def botao_remover_conta(self):

        msg = self.conectar_servidor.enviar_mensagem('remover conta')
        QMessageBox.information(None, 'msg',msg[1])

        if msg[0] == '0':
            self.voltarLogin()


    def abrir_telaExtrato(self):

        msg = self.conectar_servidor.enviar_mensagem('extrato')

        if msg[0] == '0':
            self.tela_extrato.lineEdit.setText(f'R$ {msg[1]}')
        else:
            QMessageBox.information(None, 'msg',msg[1])


        self.QtStack.setCurrentIndex(4)

    def abrir_telaSacar(self):
        msg = self.conectar_servidor.enviar_mensagem('extrato')

        if msg[0] == '0':
            self.tela_saque.lineEdit_2.setText(f"R$ {msg[1]}")
        else:
            QMessageBox.information(None, 'msg', msg[1])

        self.QtStack.setCurrentIndex(5)

    def abrir_telaDepositar(self):

        self.QtStack.setCurrentIndex(6)

    def abrir_telaTransferencia(self):
        msg = self.conectar_servidor.enviar_mensagem('extrato')

        if msg[0] == '0':
            self.tela_transferencia.lineEdit_2.setText(f"R$ {msg[1]}")
        else:
            QMessageBox.information(None, 'msg', msg[1])

        self.QtStack.setCurrentIndex(7)

    def abrir_telaHistorico(self):
        msg = self.conectar_servidor.enviar_mensagem('historico')
        print(msg)
        if msg[0] == '0':
            self.tela_historico.textEdit.setText(msg[1])
        else:
            QMessageBox.information(None, 'msg',msg[1])

        self.QtStack.setCurrentIndex(8)

    def voltarLogin(self):
        self.conectar_servidor.enviar_mensagem('deslogar')
        self.QtStack.setCurrentIndex(0)

    def desconectar(self):
        self.conectar_servidor.enviar_mensagem('encerrar')


if __name__ == '__main__':
    app= QApplication(sys.argv)
    show_main = main()
    sys.exit(app.exec_())

