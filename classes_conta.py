from class_cliente import *
from class_historico import *


class conta:

    __slots__ = ['_numero','_cliente','_saldo','_limite','historico']

    def __init__(self,numero,cliente,saldo,limite=1000):
        self._numero = numero
        self._cliente = cliente
        self._saldo = saldo
        self._limite = limite
        self.historico = historico()

    def extrato(self):
        print(F"Seu saldo e de: R$ {self._saldo:.2f}")

    def sacar(self,valor):
        if(valor > self._saldo or valor <= 0):
            return False
        else:
            self._saldo-= valor
            self.historico.salvar_transacao(f"saque feito no valor de R$ {valor}")

            return True
    def depositar(self,valor):

        if (valor <= 0):
            return False
        else:
            self._saldo += valor
            self.historico.salvar_transacao(f"Deposito feito no valor de R$ {valor}")
            return True

    def transfere(self,valor,destino):

        if (valor > self._saldo or valor <= 0):
            return False
        else:
            self._saldo -= valor
            destino.depositar(valor)
            self.historico.salvar_transacao(f"Transferencia feito no valor de R$ {valor} para a conta {destino.numero}")

            return True

    @property
    def numero(self):
        return self._numero
    @numero.setter
    def numero(self,numero):
        self._numero = numero

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





