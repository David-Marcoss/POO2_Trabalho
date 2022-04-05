import sys

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

from class_cliente import cliente
from classes_conta import conta

from Class_Banco_dados import banco

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

        self.Banco.conecta_banco()

        nome = self.tela_cadastro.lineEdit.text()
        sobrenome = self.tela_cadastro.lineEdit_2.text()
        cpf = self.tela_cadastro.lineEdit_3.text()
        nascimento = self.tela_cadastro.dateEdit.text()

        saldo = self.tela_cadastro.lineEdit_8.text()
        limite= self.tela_cadastro.lineEdit_6.text()
        senha = self.tela_cadastro.lineEdit_15.text()
        user =  self.tela_cadastro.lineEdit_7.text()


        if (nome != '' and cpf != '' and sobrenome != '' and nascimento != '' and saldo != '' and limite != '' and senha != '' and user != ''):

            saldo = self.ler_float(saldo)
            limite = self.ler_float(limite)
            nascimento = self.trata_data(nascimento)

            if saldo == None or saldo < 1:
                self.tela_cadastro.lineEdit_8.setText('')
                QMessageBox.information(None, 'msg', 'Valor invalido!! Digite um valor valido para o deposito!!')


            elif limite == None or limite < 1:
                self.tela_cadastro.lineEdit_6.setText('')
                QMessageBox.information(None, 'msg', 'Valor invalido!! Digite um valor valido para o limite!!')

            else:
                aux = self.Banco.inserir_cliente(nome,sobrenome,nascimento,cpf)

                if(aux):

                    aux = self.Banco.inserir_conta(cpf,saldo,limite,senha,user)

                    if (aux):

                        QMessageBox.information(None, 'msg', 'Conta cadastrada com Sucesso !!')

                        self.tela_cadastro.lineEdit.setText('')
                        self.tela_cadastro.lineEdit_2.setText('')
                        self.tela_cadastro.lineEdit_3.setText('')
                        self.tela_cadastro.lineEdit_8.setText('')
                        self.tela_cadastro.lineEdit_6.setText('')
                        self.tela_cadastro.lineEdit_7.setText('')
                        self.tela_cadastro.lineEdit_15.setText('')

                        self.voltarLogin()

                    else:
                        self.Banco.remover_cliente(cpf)
                        QMessageBox.information(None, 'msg', 'Nao foi possivel criar conta!! Numero da conta invalido')
                        self.abrir_telaCadastro()
                else:
                    QMessageBox.information(None, 'msg', 'Nao foi possivel criar conta!! Cpf já cadastrado no sistema')
                    self.abrir_telaCadastro()


        else:
            QMessageBox.information(None, 'msg', 'Preencha todos os campos para criar conta !!')
            self.abrir_telaCadastro()

    def botao_logar(self):
        user = self.tela_login.lineEdit.text()
        senha = self.tela_login.lineEdit_2.text()
        self.Banco.conecta_banco()

        if (user != '' and senha != ''):

            self.conta_logada = self.Banco.logar_conta(user,senha)

            self.tela_login.lineEdit.setText('')
            self.tela_login.lineEdit_2.setText('')

            if (self.conta_logada != None):

                self.abrir_telaMenu()
            else:
                QMessageBox.information(None, 'msg', 'Nao foi possivel fazer login!! usuario invalido !!')



        else:
            QMessageBox.information(None, 'msg', 'Preencha todos os campos para fazer login !!')



    def botao_sacar(self):

        valor = self.tela_saque.lineEdit.text()

        if(valor !=''):
            valor = self.ler_float(valor)

            if valor == None or valor < 1:
                self.tela_saque.lineEdit.setText('')
                QMessageBox.information(None, 'msg', 'Valor invalido!! Digite um valor valido para o deposito!!')

            else:
                transacao = self.conta_logada.sacar(valor)

                if (transacao != None):
                    QMessageBox.information(None, 'msg', 'Saque feito com sucesso !!')

                    self.Banco.atualiza_dado_conta(self.conta_logada.id_conta, 'saldo', self.conta_logada.saldo)
                    self.Banco.inserir_transacao_historico(self.conta_logada.id_conta,transacao)

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

            valor = self.ler_float(valor)

            if valor == None or valor < 1:
                self.tela_deposito.lineEdit.setText('')
                QMessageBox.information(None, 'msg', 'Valor invalido!! Digite um valor valido para o deposito!!')

            else:
                transacao = self.conta_logada.depositar(valor)

                if (transacao != None):
                    QMessageBox.information(None, 'msg', 'Deposito feito com sucesso !!')

                    self.Banco.atualiza_dado_conta(self.conta_logada.id_conta, 'saldo', self.conta_logada.saldo)
                    self.Banco.inserir_transacao_historico(self.conta_logada.id_conta, transacao)

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
            valor = self.ler_float(valor)
            id_destino = self.ler_int(id_destino)

            if valor == None or valor < 1:
                self.tela_transferencia.lineEdit.setText('')
                QMessageBox.information(None, 'msg', 'Valor invalido!! Digite um valor valido para o Transferencia!!')

            elif id_destino == None or id_destino < 1:
                self.tela_transferencia.lineEdit_5.setText('')
                QMessageBox.information(None, 'msg', 'Valor invalido!! Digite um valor valido para a conta de destino!!')

            else:
                conta_destino = self.Banco.transferencia(self.conta_logada,id_destino,valor)  #recebe a conta de destino se existir

                if (conta_destino):
                    QMessageBox.information(None, 'msg', 'Transferencia concluida com sucesso !! ')
                    self.tela_transferencia.lineEdit.setText('')
                    self.tela_transferencia.lineEdit_5.setText('')
                    self.abrir_telaMenu()

                else:
                    QMessageBox.information(None, 'msg', 'Nao foi possivel concluir transferencia!! valores de entrada invalidos')
                    self.tela_transferencia.lineEdit.setText('')
                    self.tela_transferencia.lineEdit_5.setText('')
        else:
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
        self.tela_menu.lineEdit_5.setText(f"{self.conta_logada.id_conta} ")
        self.tela_menu.lineEdit_8.setText(f"R$ {self.conta_logada.saldo} ")

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
        self.Banco.remover_conta_banco(self.conta_logada)

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
        self.tela_historico.textEdit.setText(self.Banco.historico_conta(self.conta_logada.id_conta))

        self.QtStack.setCurrentIndex(8)

    def voltarLogin(self):
        self.conta_logada = None
        self.Banco.conecta_banco()
        self.Banco.desconectar_banco()
        self.QtStack.setCurrentIndex(0)

    def ler_int(self,valor):
        try:
            valor = int(valor)
        except ValueError:
            return None

        else:
            return valor

    def ler_float(self,valor):
        try:
            valor = float(valor)
        except ValueError:
            return None

        else:
            return valor

    def trata_data(self,data):
        data = data.split('/')
        data = f"{data[2]}/{data[1]}/{data[0]}"

        return data

if __name__ == '__main__':
    app= QApplication(sys.argv)
    show_main = main()
    sys.exit(app.exec_())

