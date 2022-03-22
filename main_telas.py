import sys
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QApplication, QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication

from Telas.tela_menu import tela_menu
from Telas.tela_cadastro import tela_cadastro
from Telas.tela_login import tela_login
from Telas.tela_historico import tela_historico
from Telas.tela_saque import tela_saque
from Telas.tela_deposito import tela_deposito
from Telas.tela_dados import tela_dados
from Telas.tela_transferencia import tela_transferencia
from Telas.tela_extrato import tela_extrato


from class_banco import banco
from classes_conta import conta
from class_cliente import cliente
from class_historico import historico

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

        self.QtStack.addWidget(self.QtStack0)
        self.QtStack.addWidget(self.QtStack1)
        self.QtStack.addWidget(self.QtStack2)
        self.QtStack.addWidget(self.QtStack3)
        self.QtStack.addWidget(self.QtStack4)
        self.QtStack.addWidget(self.QtStack5)
        self.QtStack.addWidget(self.QtStack6)
        self.QtStack.addWidget(self.QtStack7)
        self.QtStack.addWidget(self.QtStack8)


class main(QMainWindow,main_telas):

    def __init__(self,parent=None):
        super(main_telas,self).__init__(parent)
        self.setupUi(self)

        self.Banco = banco() #armazena as contas
        self.conta_logada = None

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

        id_conta = self.tela_cadastro.lineEdit_4.text()
        saldo = self.tela_cadastro.lineEdit_8.text()
        limite= self.tela_cadastro.lineEdit_6.text()
        senha = self.tela_cadastro.lineEdit_7.text()


        if (nome != '' and cpf != '' and sobrenome != '' and id_conta != '' and saldo != '' and limite != '' and senha != ''):

            id_conta = int(id_conta)
            saldo = float(saldo)
            limite = float(limite)

            client = cliente(cpf,nome,sobrenome)
            cont = conta(id_conta, client, saldo,senha,limite)

            if (self.Banco.criar_conta(cont)):

                QMessageBox.information(None, 'msg', 'Conta cadastrada com Sucesso !!')

                self.tela_cadastro.lineEdit.setText('')
                self.tela_cadastro.lineEdit_2.setText('')
                self.tela_cadastro.lineEdit_3.setText('')
                self.tela_cadastro.lineEdit_4.setText('')
                self.tela_cadastro.lineEdit_8.setText('')
                self.tela_cadastro.lineEdit_6.setText('')
                self.tela_cadastro.lineEdit_7.setText('')

                self.voltarLogin()

            else:
                QMessageBox.information(None, 'msg', 'Nao foi possivel criar conta!! Numero da conta invalido')

        else:
            QMessageBox.information(None, 'msg', 'Preencha todos os campos para criar conta !!')

    def botao_logar(self):
        user = self.tela_login.lineEdit.text()
        senha = self.tela_login.lineEdit_2.text()

        if (user != '' and senha != ''):
            user = int(user)

            conta = self.Banco.buscar_conta(user)
            self.tela_login.lineEdit.setText('')
            self.tela_login.lineEdit_2.setText('')

            if (conta != None):

                if (senha == conta.senha):
                    self.conta_logada = conta # recebe a conta logada para que possa fazer as operações apos entrar no sistema
                    self.abrir_telaMenu()

                else:
                    QMessageBox.information(None, 'msg', 'Nao foi possivel fazer login!! senha invalida !!')

            else:
                QMessageBox.information(None, 'msg', 'Nao foi possivel fazer login!! usuario invalido !!')



        else:
            QMessageBox.information(None, 'msg', 'Preencha todos os campos para fazer login !!')



    def botao_sacar(self):

        valor = self.tela_saque.lineEdit.text()

        if(valor !=''):
            valor = float(valor)

            aux = self.conta_logada.sacar(valor)

            if (aux):
                QMessageBox.information(None, 'msg', 'Saque feito com sucesso !!')
                self.tela_saque.lineEdit.setText('')
                self.abrir_telaMenu()
            else:
                QMessageBox.information(None, 'msg', 'Nao foi possivel concluir Saque !! ')
                self.tela_saque.lineEdit.setText('')
        else:
            QMessageBox.information(None, 'msg', 'Preencha todos os campos para concluir Saque!! ')

    def botao_depositar(self):
        valor = self.tela_deposito.lineEdit.text()

        if(valor != ''):

            valor = float(valor)

            aux = self.conta_logada.depositar(valor)

            if (aux):
                QMessageBox.information(None, 'msg', 'Deposito feito com sucesso !!')
                self.tela_deposito.lineEdit.setText('')
                self.abrir_telaMenu()
            else:
                QMessageBox.information(None, 'msg', 'Nao foi possivel concluir deposito Deposito !! ')
                self.tela_deposito.lineEdit.setText('')
        else:
            QMessageBox.information(None, 'msg', 'Preencha todos os campos para concluir Deposito!! ')

    def botao_transferencia(self):
        valor = self.tela_transferencia.lineEdit.text()

        id_destino = self.tela_transferencia.lineEdit_5.text() #recebe o id da conta de destino

        if(valor != '' and id_destino != ''):
            valor = float(valor)
            id_destino = float(id_destino)

            conta_destino = self.Banco.buscar_conta(id_destino)  #recebe a conta de destino se existir

            if (conta_destino != None):
                aux = self.conta_logada.sacar(valor)

                if ( aux ):
                    conta_destino.depositar(valor)

                    QMessageBox.information(None, 'msg', 'Transferencia concluida com sucesso !! ')
                    self.tela_transferencia.lineEdit.setText('')
                    self.tela_transferencia.lineEdit_5.setText('')
                    self.abrir_telaMenu()
                else:
                    QMessageBox.information(None, 'msg', 'Nao foi possivel concluir transferencia!! Valor invalido !! ')
                    self.tela_transferencia.lineEdit.setText('')
                    self.tela_transferencia.lineEdit_5.setText('')

            else:
                QMessageBox.information(None, 'msg', 'Nao foi possivel concluir transferencia!! Conta de destino invalida !! ')
                self.tela_transferencia.lineEdit.setText('')
                self.tela_transferencia.lineEdit_5.setText('')
        else:
            QMessageBox.information(None, 'msg','Preencha todos os campos para concluir transferencia!! ')

    def abrir_telaCadastro(self):
        self.tela_login.lineEdit.setText('')
        self.tela_login.lineEdit_2.setText('')
        self.QtStack.setCurrentIndex(1)

    def abrir_telaMenu(self):
        self.QtStack.setCurrentIndex(2)

    def abrir_telaDados(self):
        self.tela_dados.lineEdit.setText(f'{self.conta_logada.cliente.nome}')
        self.tela_dados.lineEdit_2.setText(f'{self.conta_logada.cliente.sobrenome}')
        self.tela_dados.lineEdit_3.setText(f'{self.conta_logada.cliente.cpf}')
        self.tela_dados.lineEdit_4.setText(f'{self.conta_logada.id_conta}')
        self.tela_dados.lineEdit_5.setText(f'R$ {self.conta_logada.saldo}')
        self.tela_dados.lineEdit_6.setText(f'R$ {self.conta_logada.limite}')

        self.QtStack.setCurrentIndex(3)

    def botao_remover_conta(self):
        self.Banco.remover_conta(self.conta_logada.id_conta)

        QMessageBox.information(None, 'msg', 'Conta removida com sucesso!!')
        self.voltarLogin()

    def abrir_telaExtrato(self):

        self.tela_extrato.lineEdit.setText(f"R$ {self.conta_logada.saldo} ")
        self.QtStack.setCurrentIndex(4)

    def abrir_telaSacar(self):
        self.tela_saque.lineEdit_2.setText(f"R$ {self.conta_logada.saldo} ")
        self.QtStack.setCurrentIndex(5)

    def abrir_telaDepositar(self):

        self.QtStack.setCurrentIndex(6)

    def abrir_telaTransferencia(self):
        self.tela_transferencia.lineEdit_2.setText(f"R$ {self.conta_logada.saldo} ")
        self.QtStack.setCurrentIndex(7)

    def abrir_telaHistorico(self):
        self.QtStack.setCurrentIndex(8)

    def voltarLogin(self):
        self.conta_logada = None
        self.QtStack.setCurrentIndex(0)


if __name__ == '__main__':
    app= QApplication(sys.argv)
    show_main = main()
    sys.exit(app.exec_())