from class_cliente import *
from class_historico import *


class conta:

    __slots__ = ['_id_conta', '_cliente', '_saldo', '_limite', '_historico','_senha']

    def __init__(self, id_conta, cliente, saldo,senha,limite=1000):
        self._id_conta = id_conta
        self._cliente = cliente
        self._saldo = saldo
        self._limite = limite
        self._senha = senha
        self._historico = historico()

    def extrato(self):
        print(f"Seu saldo e de: R$ {self._saldo:.2f}")

    def sacar(self,valor):
        if(valor > self._saldo or valor <= 0):
            return False
        else:
            self._saldo-= valor
            self._historico.salvar_transacao(f"saque feito no valor de R$ {valor}")

            return True
    def depositar(self,valor):

        if (valor <= 0):
            return False
        else:
            self._saldo += valor
            self._historico.salvar_transacao(f"Deposito feito no valor de R$ {valor}")
            return True

    def transfere(self,valor,destino):

        if (valor > self._saldo or valor <= 0):
            return False
        else:
            self._saldo -= valor
            destino.botao_depositar(valor)
            self._historico.salvar_transacao(f"Transferencia feito no valor de R$ {valor} para a conta {destino.id_conta}")

            return True

    @property
    def id_conta(self):
        return self._id_conta
    @id_conta.setter
    def id_conta(self,numero):
        self._id_conta = numero

    @property
    def cliente(self):
        return self._cliente

    @cliente.setter
    def cliente(self, cliente):
        self._cliente = cliente

    @property
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self, limite):
        self._limite = limite

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, senha):
        self._senha = senha

    @property
    def saldo(self):
        return self._saldo

    @property
    def historico(self):
        return self._historico





