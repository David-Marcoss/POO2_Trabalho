from datetime import datetime

class historico:
    def __init__(self):
        self.data = datetime.today()
        self.transacoes = []

    def salvar_transacao(self,transacao):
        self.transacoes.append(transacao)

    def imprimir_historico(self):
        print(f"\nTransações feitas apartir da data: {self.data}\n")
        for i in self.transacoes:
            print(f"- {i}")
