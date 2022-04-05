import mysql.connector as mysql
from class_cliente import cliente
from classes_conta import conta
from datetime import date

class banco:

    """
     - Esta função tem como objetivo fazer a conexão com o banco de dados do
       nosso sistema e realizar as operações de inserção, busca e remoção de
       dados do banco de dados.
    """

    def __init__(self):
        """
            - Metodo construtor da Classe possui os parametro para receber
            a conexão com o banco de dados.
        """

        self._conexao = None
        self._cursor = None

    def conecta_banco(self):
        """
         - Esté metodo faz a conexão com o banco de dados do sistema
         :return: sem retorno
        """
        self._conexao = mysql.connect(host='localhost', db='Banco', user='suporte', passwd='12345678')
        self._cursor = self._conexao.cursor()

    def desconectar_banco(self):
        """
            -Está função desconecta o Banco de dados.
        :return:
        """
        self._conexao.close()

    def inserir_cliente(self,nome,sobrenome,data_nascimento,cpf):
        """
        :param nome: string com nome do cliente
        :param sobrenome: string com sobrenome do cliente
        :param data_nascimento: string com data de nascimento
        :param cpf: string com cpf do cliente

        - Este metodo recebe os dados de um cliente e insere o cliente no
         banco de dados se ele ainda não foi inserido

        :return: True se o cliente foi inserido no banco de dados
                 False se o cliente nao foi inserido no banco de dados
        """
        if self.retorna_dado_cliente('cpf','cpf',cpf) == None:  #verifica se o cliente já foi cadastrado ou Nao

            self._cursor.execute(" INSERT INTO `Banco`.`Cliente` (`nome`, `sobrenome`, `data_nascimento`, `cpf`) VALUES(%s,%s,%s,%s);",(nome,sobrenome,data_nascimento,cpf))
            self._conexao.commit()

            return True
        else:
            return False

    def retorna_dado_cliente(self,dado,atributo,parametro):
        """
        :param dado: dado: recebe uma string com o dado de um cliente
         que se deseja obter do banco de dados EX:(nome,*,id,etc)

        :param atributo: recebe uma string com o atributo de comparação
        para busca Ex:(cpf,nome,etc)

        :param parametro: recebe uma string com o parametro de busca
        no banco Ex:('david','1',etc)

        - Está função retorna um dado de um cliente que esta no Banco de dados

        :return: dado se a busca for bem sucedida
                 None se o dado nao foi e encontrado
        """
        self._cursor.execute('USE Banco;')
        self._cursor.execute(f"select {dado} from Cliente where {atributo} = {parametro}")

        valor = self._cursor.fetchall()

        if valor == []:
            return None
        else:
            return valor

    def retorna_cliente(self,cpf):
        """
        :param cpf: recebe o cpf de uma pessoa

            -Está função Busca um cliente no banco de dados e retorna os dados cliente

        :return: Cliente: se o cliente buscado foi encontrado
                 None: se o cliente ainda não foi encontrado
        """
        valor = self.retorna_dado_cliente('*','cpf',cpf)

        if valor == None:
            return None
        else:
            c = cliente(valor[0][0],valor[0][4],valor[0][1],valor[0][2],valor[0][3])

            return c

    def retorna_dado_conta(self,dado,atributo,parametro):
        """
        :param dado: dado: recebe uma string com o dado de um cliente
         que se deseja obter do banco de dados EX:(nome,*,id,etc)

        :param atributo: recebe uma string com o atributo de comparação
        para busca Ex:(cpf,nome,etc)

        :param parametro: recebe uma string com o parametro de busca
        no banco Ex:('david','1',etc)

        - Está função retorna um dado de um cliente que esta no Banco de dados

        :return: dado se a busca for bem sucedida
                 None se o dado nao foi e encontrado
        """
        self._cursor.execute('USE Banco;')
        self._cursor.execute(f'select {dado} from Conta where {atributo} = {parametro}')

        valor = self._cursor.fetchall()

        if valor == []:
            return None
        else:
            return valor


    def inserir_conta(self,cpf,saldo,limite,senha,user):
        """

        :param cpf: do cliente
        :param saldo: saldo da conta
        :param limite: limite da conta
        :param senha: senha da conta
        :param user: usuario da conta

            -Está função recebe o cpf de um cliente ja cadastrado no banco e
            os dados de uma conta, e cria uma conta para o cliente e insere
            os dados da conta no banco de dados

        :return: True se a conta foi criada com sucesso ou
                 False se nao foi possivael criar conta
        """

        id_cliente = self.retorna_dado_cliente('Id_cliente', 'cpf',cpf)
        id_cliente = id_cliente[0][0]

        if ( self.retorna_dado_conta('Id_conta','Cliente_Id_cliente',id_cliente) == None and self.retorna_dado_conta('user_login','user_login',f"'{user}'") == None ):

            self._cursor.execute('USE Banco;')
            self._cursor.execute(f"INSERT INTO `Banco`.`Conta` (`saldo`, `limite`, `Cliente_Id_cliente`, `senha`, `user_login`) VALUES ({saldo},{limite},{id_cliente},sha2('{senha}', 256),'{user}');")
            self._conexao.commit()

            id_conta = self.retorna_dado_conta('Id_conta','Cliente_Id_cliente',id_cliente)
            id_conta = id_conta[0][0]

            self.inserir_transacao_historico(id_conta,'-Conta criada')

            return True
        else:
            return False


    def logar_conta(self,user,password):
        """
        :param user:  usuario de uma conta
        :param password: senha de uma conta

            -Esté metodo faz o login com uma conta do banco e se o usuario e
            senha da conta for validos esté metodo devolve para o sistema a
            conta logada

        :return: conta se o login foi concluido com sucesso
                 None se nao foi possivel fazer login
        """
        self._cursor.execute('USE Banco;')
        self._cursor.execute(f"select * from Conta where user_login = '{user}' and senha = sha2('{password}', 256)")

        valor = self._cursor.fetchall()

        if valor != []:
            id_cliente = valor[0][3]

            dados_cliente = self.retorna_dado_cliente('*','Id_cliente',id_cliente)


            id_conta = int(valor[0][0])
            saldo = float(valor[0][1])
            limite = float(valor[0][2])
            senha = str(valor[0][4])
            user = str(valor[0][5])

            cliente_logado = cliente(dados_cliente[0][0], dados_cliente[0][4], dados_cliente[0][1], dados_cliente[0][2], dados_cliente[0][3])

            c = conta(id_conta, cliente_logado, saldo,senha,user,limite)

            return c

        else:
            return None

    def atualiza_dado_conta(self,id_conta,dado,valor):
        """
        :param id_conta:  Recebe o id da conta que se deseja alterar
        o dado

        :param dado:  Recebe o dado da contaque se deseja alterar no
        banco ex(saldo,limite,senha e etc)

        :param valor: recebe o novo valor que vai ser atribuido ao
        dado alterado no banco

        :return: Retorna a conta com o dado atualizado
        """

        self._cursor.execute('USE Banco;')
        self._cursor.execute(f'UPDATE `Banco`.`Conta` SET {dado} = {valor} WHERE (Id_conta = {id_conta});')
        self._conexao.commit()


    def inserir_transacao_historico(self,id_conta,transacao):
        """

        :param transacao: recebe uma string contendo a descrição de uma
        operação realizada na conta e inseres a transação no banco de dados

        :return: sem retorno.
        """
        self._cursor.execute('USE Banco;')
        self._cursor.execute(f"INSERT INTO historico(`transacao`,`data_transacao`,`Conta_Id_conta`) VALUES('{transacao}','{date.today()}',{id_conta});")
        self._conexao.commit()

    def historico_conta(self,id_conta):
        self._cursor.execute('USE Banco;')
        self._cursor.execute(f'SELECT transacao,data_transacao FROM historico WHERE Conta_Id_conta = {id_conta};')

        historico = ''

        for i in self._cursor:
            historico += '\n' + i[0] + ' na data: ' + f'{i[1]}' + '\n'

        return historico

    def transferencia(self,conta_logada,id_conta_destino,valor):
        conta_destino = self.retorna_dado_conta('saldo','Id_conta',id_conta_destino)

        print(conta_destino)

        if conta_destino != None:
            saldo_destino = conta_destino[0][0]     #valor do saldo da conta de destino

            if conta_logada.sacar(valor) != None:

                self.atualiza_dado_conta(conta_logada.id_conta, 'saldo', conta_logada.saldo)
                self.inserir_transacao_historico(conta_logada.id_conta,f'   -Transferencia no valor de: R$ {valor} enviada para conta: {id_conta_destino}')

                saldo_destino+= valor
                self.atualiza_dado_conta(id_conta_destino, 'saldo', saldo_destino)
                self.inserir_transacao_historico(id_conta_destino,f'    -Transferencia recebida no valor de: R$ {valor} da conta : {conta_logada.id_conta}')
                return True

            else:
                return False
        else:
            return False

    def remover_conta_banco(self,conta_logada):

        self._cursor.execute('USE Banco;')

        self._cursor.execute(f'DELETE FROM historico WHERE Conta_Id_conta = {conta_logada.id_conta};')
        self._cursor.execute(f'DELETE FROM Conta WHERE Id_conta =  {conta_logada.id_conta};')
        self._cursor.execute(f'DELETE FROM Cliente WHERE Id_cliente = {conta_logada.cliente.cliente_id};')
        self._conexao.commit()

        conta_logada = None

        return conta_logada

    def remover_cliente(self,cpf):
        self._cursor.execute('USE Banco;')
        self._cursor.execute(f'DELETE FROM Cliente WHERE cpf = {cpf};')
        self._conexao.commit()

if __name__ == '__main__':
    banco = banco()
    banco.conecta_banco()


    #c = banco.retorna_cliente('88697949354')

    #id_cliente = banco.retorna_dado_cliente('Id_cliente','cpf','07662949354')
    #id_cliente = id_cliente[0][0]

    #contas = banco.retorna_dado_conta('*','Cliente_Id_cliente',id_cliente)

    #print(contas)



    #print(banco.inserir_cliente('Maria','Deuselita','1991/02/22','12345678922'))
    #banco.remover_cliente('22222222222')

    #print(banco.inserir_conta('12345678911',500,5000,'1234','maria123'))

    #conta_logada = banco.logar_conta('maria123', '1234')


    #banco.historico_conta(13)

    #print( banco.retorna_dado_conta('user_login', 'user_login',"'robin09'") )



    #transacao = conta_logada.sacar(400)
    #banco.atualiza_dado_conta(conta_logada.id_conta,'saldo',conta_logada.saldo)
    #banco.inserir_transacao_historico(conta_logada.id_conta,transacao)

    #banco.transferencia(conta_logada,'12',500)

    #print(banco.historico_conta(conta_logada.id_conta))
    #print(banco.historico_conta(12))

    #banco.remover_conta_banco(conta_logada)

    #print(conta_logada)


