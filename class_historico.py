from datetime import datetime

class historico:
    def __init__(self):
        self.data = datetime.today()
        self.transacoes = []

    def salvar_transacao(self,transacao):
        self.transacoes.append(transacao)

    def imprimir_historico(self):
        historicos = ('----'*20) + '\n'
        historicos += f"\nTransações feitas apartir da data: {self.data}\n"
        historicos += ('----' * 20) + '\n'
        for i in self.transacoes:
            historicos += i + '\n'+ ('----'*20) + '\n'

        return historicos
