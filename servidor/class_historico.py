import mysql.connector
from datetime import date

class historico:

    def __init__(self):
        self._conexao = mysql.connector.connect(host='localhost', db='Banco', user='suporte', passwd='Info@1234')
        self._cursor = self._conexao.cursor()


    def inserir_transacao_historico(self, id_conta, transacao):
        """

        :param transacao: recebe uma string contendo a descrição de uma
        operação realizada na conta e inseres a transação no banco de dados

        :return: sem retorno.
        """
        self._cursor.execute('USE Banco;')
        self._cursor.execute(
            f"INSERT INTO historico(`transacao`,`data_transacao`,`Conta_Id_conta`) VALUES('{transacao}','{date.today()}',{id_conta});")
        self._conexao.commit()

    def historico_conta(self, id_conta):
        self._cursor.execute('USE Banco;')
        self._cursor.execute(f'SELECT transacao,data_transacao FROM historico WHERE Conta_Id_conta = {id_conta};')

        dados = self._cursor.fetchall()
        historico = ''

        if len(dados) < 10:
            for i in dados:
                historico += '\n' + i[0] + ' na data: ' + f'{i[1]}' + '\n'
        else:
            j= len(dados)
            for i in range(0,10):
                j-=1
                historico += '\n' + dados[j][0] + ' na data: ' + f'{dados[j][1]}' + '\n'

        return historico

    def desconectar(self):
        self._conexao.close()