

class banco:
    def __init__(self):
        self._contas = {}

    def criar_conta(self,conta):
        if self.buscar_conta(conta.id_conta) == None:

            self._contas[conta.id_conta] = conta
            return True
        else:
            return False

    def buscar_conta(self,id_conta):

        if id_conta in self._contas.keys():
            return self._contas[id_conta]
        else:
            return None

    def remover_conta(self,id_conta):
        conta = self.buscar_conta(id_conta)

        if conta != None:
            del self._contas[id_conta]

            return True
        else:
            return False


