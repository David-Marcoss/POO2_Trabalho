from classes_conta import *
import sys
sys.path.insert(1, '../')

from funcoes_auxiliares import *

import threading


class cliente_Thread(threading.Thread):

    def __init__(self,clienteaddr,clientsoket,sinc):
        threading.Thread.__init__(self)
        self.conexao = clientsoket
        self.contab = conta()
        self.sinc = sinc
        print(f"Nova coneção de: {clienteaddr}")

    def run(self) -> None:
        msg_recebida = ''

        while(msg_recebida != 'encerrar'):

            msg_recebida = self.conexao.recv(1024).decode()
            print(f'{msg_recebida}')
            operacao = trata_mensagen(msg_recebida)

            if(operacao[0] == 'cadastrar'): #[op 0,nome 1,sobrenome 2,data 3,cpf 4,saldo 5,limite 6,senha 7,usuario 8][cadastrar,sara,mendes,12/03/1950,89898989898,1000,10000,123,sara]
                cpf = valida_cpf(operacao[4])
                saldo = v_float(operacao[5])
                limite = v_float(operacao[6])
                data_nascimento = trata_data(operacao[3])

                if saldo != None and cpf == True and limite != None:

                    self.sinc.acquire()
                    if self.contab.cliente.inserir_cliente(operacao[1],operacao[2],data_nascimento,operacao[4]):
                        if self.contab.inserir_conta(operacao[4],saldo,limite,operacao[7],operacao[8]):

                            self.conexao.send('0,Cadastro realizado com sucesso!!!'.encode())
                        else:
                            self.contab.cliente.remover_cliente(operacao[4])
                            self.conexao.send('1,Nao foi possivel realizar cadastro nome de ususario ja cadastrado!!!'.encode())
                    else:
                        self.conexao.send('1,Nao foi possivel realizar cadastro cpf ja cadastrado!!!'.encode())

                    self.sinc.release()

                else:
                    self.conexao.send('1,Nao foi possivel realizar cadastro dados invalidos!!!'.encode())


            elif (operacao[0] == 'logar'): #[op 0, usuario 1, senha 2]
                self.sinc.acquire()

                if self.contab.logar_conta(operacao[1],operacao[2]):
                    self.conexao.send('0,Login realizado com sucesso!!!'.encode())
                else:
                    self.conexao.send('1,Nao foi possivel fazer login dados usuario ou senha invalido!!!'.encode())

                self.sinc.release()

            elif (operacao[0] == 'ver dados'):
                self.sinc.acquire()
                dados_conta = self.contab.dados_conta()

                if dados_conta != None:
                    dados = concatenar_operacao(dados_conta)
                    self.conexao.send(('0,' + dados).encode())
                else:
                    self.conexao.send('1,Nao foi possivel concluida operaçao!!!'.encode())
                self.sinc.release()

            elif (operacao[0] == 'extrato'):
                self.sinc.acquire()
                extrato  = self.contab.extrato()
                if(extrato != None):
                    self.conexao.send(('0,' +extrato).encode())
                else:
                    self.conexao.send('1,Nao foi possivel concluida operaçao!!!'.encode())
                self.sinc.release()

            elif (operacao[0] == 'sacar'): # [op 0, valor 1]
                valor = v_float(operacao[1])
                self.sinc.acquire()

                if valor != None:
                    if self.contab.sacar(valor):
                        self.conexao.send('0,Operaçao concluida com sucesso'.encode())
                    else:
                        self.conexao.send('1,Nao foi possivel concluida operaçao!!!'.encode())
                else:
                    self.conexao.send('1,Nao foi possivel concluida operaçao entrada invalida!!!'.encode())

                self.sinc.release()

            elif (operacao[0] == 'depositar'):  # [op 0, valor 1]
                valor = v_float(operacao[1])

                self.sinc.acquire()
                if valor != None:
                    if self.contab.depositar(valor):
                        self.conexao.send('0,Operaçao concluida com sucesso'.encode())
                    else:
                        self.conexao.send('1,Nao foi possivel concluida operaçao!!!'.encode())
                else:
                    self.conexao.send('1,Nao foi possivel concluida operaçao entrada invalida!!!'.encode())

                self.sinc.release()

            elif (operacao[0] == 'transferir'):  # [op 0, id_destino 1, valor 2]

                id_destino = v_int(operacao[1])
                valor = v_float(operacao[2])
                self.sinc.acquire()

                if valor != None and id_destino != None:

                    if self.contab.transferencia(id_destino,valor):
                        self.conexao.send('0,Operaçao concluida com sucesso'.encode())
                    else:
                        self.conexao.send('1,Nao foi possivel concluida operaçao!!\nverifique se o valor e o numero da conta de destino estao certos!!'.encode())
                else:
                    self.conexao.send('1,Nao foi possivel concluida operaçao entrada invalida!!!'.encode())

                self.sinc.release()

            elif (operacao[0] == 'historico'):  # [op 0, valor 1]
                self.sinc.acquire()

                hist = self.contab.historico_transacoes()
                if hist != None:
                    self.conexao.send(('0,' +hist).encode())
                else:
                    self.conexao.send('1,Nao foi possivel concluida operaçao!!!'.encode())

                self.sinc.release()

            elif (operacao[0] == 'remover conta'):  # [op 0, valor 1]

                self.sinc.acquire()

                if self.contab.remover_conta_banco():
                    self.conexao.send(('0,Conta Removida com sucesso').encode())
                else:
                    self.conexao.send('1,Nao foi possivel concluida operaçao!!!\nA conta ainda possui saldo!!!'.encode())

                self.sinc.release()


            elif (operacao[0] == 'deslogar'):  # [op 0, valor 1]
                self.sinc.acquire()
                self.contab.deslogar()
                self.conexao.send('1,Usuario deslogado!!!'.encode())

                self.sinc.release()

            elif(operacao[0] == 'dados menu'):
                self.sinc.acquire()
                dados_conta = self.contab.dados_menu()

                if dados_conta != None:
                    dados = concatenar_operacao(dados_conta)
                    self.conexao.send(('0,' + dados).encode())
                else:
                    self.conexao.send('1,Nao foi possivel concluida operaçao!!!'.encode())

                self.sinc.release()


            else:
                try:
                    self.conexao.send('1,OPERACAO INVALIDA'.encode())

                except BrokenPipeError:
                    self.contab.desconectar()
                    break





