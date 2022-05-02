import mysql.connector

class cliente:

    def __init__(self):

        self._cliente_id = ''
        self._cpf = ''
        self._nome = ''
        self._sobrenome = ''
        self._data_nascimento = ''

        self._conexao = mysql.connector.connect(host='localhost', db='Banco', user='suporte', passwd='Info@1234')
        self._cursor = self._conexao.cursor()

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
        self.reiniciar_conexao_db()
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
        self.reiniciar_conexao_db()
        self._cursor.execute('USE Banco;')
        self._cursor.execute(f"select {dado} from Cliente where {atributo} = {parametro}")

        valor = self._cursor.fetchall()

        if valor == []:
            return None
        else:
            return valor

    def remover_cliente(self,cpf):
        self.reiniciar_conexao_db()
        self._cursor.execute('USE Banco;')
        self._cursor.execute(f'DELETE FROM Cliente WHERE cpf = {cpf};')
        self._conexao.commit()

    def reiniciar_conexao_db(self):
        """
            reinicia a conexao com o banco de dados
            para caso aja a alteração de um dado do banco por outra instancia
            nao tenha conflito de valores da conta
        """

        self._conexao.close()
        self._conexao = mysql.connector.connect(host='localhost', db='Banco', user='suporte', passwd='Info@1234')
        self._cursor = self._conexao.cursor()


    def desconectar(self):
        self._conexao.close()

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self,cpf):
        self._cpf = cpf

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def sobrenome(self):
        return self._sobrenome

    @sobrenome.setter
    def sobrenome(self, sobrenome):
        self._sobrenome = sobrenome

    @property
    def data_nascimento(self):
        return self._data_nascimento

    @property
    def cliente_id(self):
        return self._cliente_id

