import mysql.connector
from class_cliente import cliente
from class_historico import historico

class conta:

    def __init__(self):

        self._id_conta = ''
        self._id_cliente = ''
        self._saldo = ''
        self._limite = ''
        self._senha = ''
        self._user_login = ''
        self._cliente = cliente()
        self._hitorico_conta = historico()
        self._conta_logada = False

        self._conexao = mysql.connector.connect(host='localhost', db='Banco', user='suporte', passwd='Info@1234')
        self._cursor = self._conexao.cursor()

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
        self.reiniciar_conexao_db()

        self._cursor.execute('USE Banco;')
        self._cursor.execute(f'SELECT {dado} FROM Conta WHERE {atributo} = {parametro}')

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

        self.reiniciar_conexao_db()

        id_cliente = self.cliente.retorna_dado_cliente('Id_cliente', 'cpf',cpf)

        if id_cliente != None:
            id_cliente = id_cliente[0][0]

        else:
            return False

        if ( self.retorna_dado_conta('Id_conta','Cliente_Id_cliente',id_cliente) == None and self.retorna_dado_conta('user_login','user_login',f"'{user}'") == None ):

            self._cursor.execute('USE Banco;')
            self._cursor.execute(f"INSERT INTO `Banco`.`Conta` (`saldo`, `limite`, `Cliente_Id_cliente`, `senha`, `user_login`) VALUES ({saldo},{limite},{id_cliente},sha2('{senha}', 256),'{user}');")
            self._conexao.commit()

            id_conta = self.retorna_dado_conta('Id_conta','Cliente_Id_cliente',id_cliente)
            id_conta = id_conta[0][0]

            self.historico_conta.inserir_transacao_historico(id_conta,'-Conta criada')

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

        self.reiniciar_conexao_db()
        self._cursor.execute('USE Banco;')
        self._cursor.execute(f"select * from Conta where user_login = '{user}' and senha = sha2('{password}', 256)")

        valor = self._cursor.fetchall()

        if valor != []:

            self.id_conta = int(valor[0][0])
            self._saldo = float(valor[0][1])
            self.limite = float(valor[0][2])
            self.id_cliente = valor[0][3]
            self.senha = str(valor[0][4])
            self.user = str(valor[0][5])
            self._conta_logada = True

            return True

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
        self.reiniciar_conexao_db()
        self._cursor.execute('USE Banco;')
        self._cursor.execute(f'UPDATE `Banco`.`Conta` SET {dado} = {valor} WHERE (Id_conta = {id_conta});')
        self._conexao.commit()



    def extrato(self):
        self.reiniciar_conexao_db()
        if(self._conta_logada == True):
            return f"{self.saldo:.2f}"

        return None

    def sacar(self, valor):
        self.reiniciar_conexao_db()
        if (self._conta_logada == True):

            if valor <= self.saldo and valor > 0:

                self._saldo = self.saldo - valor
                self.atualiza_dado_conta(self.id_conta, 'saldo', self._saldo)
                self.historico_conta.inserir_transacao_historico(self.id_conta,f'  -Saque feito no valor de: R$ {valor} ')
                self._conexao.commit()

                return True
        return False

    def depositar(self, valor):
        self.reiniciar_conexao_db()
        if (self._conta_logada == True and valor > 0):

            self._saldo = self.saldo + valor
            self.atualiza_dado_conta(self.id_conta, 'saldo', self._saldo)
            self.historico_conta.inserir_transacao_historico(self.id_conta,f"  -Deposito feito no valor de R$ {valor}")
            self._conexao.commit()

            return True

        return False

    def transferencia(self,id_conta_destino, valor):
        self.reiniciar_conexao_db()

        if (self._conta_logada == True):
            conta_destino = self.retorna_dado_conta('saldo', 'Id_conta', id_conta_destino)

            if conta_destino != None and valor <= self.saldo and valor > 0 :
                saldo_destino = conta_destino[0][0]  # valor do saldo da conta de destino

                self._saldo = self.saldo - valor

                self.atualiza_dado_conta(self.id_conta, 'saldo', self._saldo)
                self.historico_conta.inserir_transacao_historico(self.id_conta,f'   -Transferencia no valor de: R$ {valor} enviada para conta: {id_conta_destino}')

                saldo_destino += valor
                self.atualiza_dado_conta(id_conta_destino, 'saldo', saldo_destino)
                self.historico_conta.inserir_transacao_historico(id_conta_destino,f'    -Transferencia recebida no valor de: R$ {valor} da conta : {self.id_conta}')
                return True

        return False

    def deslogar(self):
        self._id_conta = ''
        self._id_cliente = ''
        self._saldo = ''
        self._limite = ''
        self._senha = ''
        self._user_login = ''
        self._conta_logada = False

    def desconectar(self):
        self.historico_conta.desconectar()
        self.cliente.desconectar()
        self._conexao.close()

    def historico_transacoes(self):
        self.reiniciar_conexao_db()
        if self._conta_logada == True:
            return self.historico_conta.historico_conta(self.id_conta)
        else:
            return None

    def dados_conta(self):

        if self._conta_logada == True:
            dados_cliente = self.cliente.retorna_dado_cliente('nome,sobrenome,cpf', 'Id_cliente', self.id_cliente)
            dados_conta = []
            for i in dados_cliente[0]:
                dados_conta.append(i)

            dados_conta.append(self.id_conta)
            dados_conta.append(self.saldo)
            dados_conta.append(self.limite)

            return dados_conta
        else:
            return None

    def dados_menu(self):

        if self._conta_logada == True:

            dados_cliente = self.retorna_dado_conta('Id_conta,saldo', 'Id_conta', self.id_conta)
            dados_conta = []

            for i in dados_cliente[0]:
                dados_conta.append(i)

            return dados_conta
        else:
            return None


    def remover_conta_banco(self):
        self.reiniciar_conexao_db()

        if self._conta_logada == True and self.saldo == 0:

            self._cursor.execute('USE Banco;')

            self._cursor.execute(f'DELETE FROM historico WHERE Conta_Id_conta = {self.id_conta};')
            self._cursor.execute(f'DELETE FROM Conta WHERE Id_conta =  {self.id_conta};')
            self._cursor.execute(f'DELETE FROM Cliente WHERE Id_cliente = {self.id_cliente};')
            self._conexao.commit()

            self._conta_logada = False

            return True

        else:
            return None

    def reiniciar_conexao_db(self):
        """
            reinicia a conexao com o banco de dados
            para caso aja a alteração de um dado do banco por outra instancia
            nao tenha conflito de valores da conta
        """

        self._conexao.close()
        self._conexao = mysql.connector.connect(host='localhost', db='Banco', user='suporte', passwd='Info@1234')
        self._cursor = self._conexao.cursor()

    @property
    def id_conta(self):
        return self._id_conta

    @id_conta.setter
    def id_conta(self, numero):
        self._id_conta = numero

    @property
    def id_cliente(self):
        return self._id_cliente

    @id_cliente.setter
    def id_cliente(self,id):
        self._id_cliente = id

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
        if self._conta_logada:

            self.reiniciar_conexao_db()
            self._cursor.execute('USE Banco;')
            self._cursor.execute(f"""SELECT saldo FROM Conta WHERE Id_conta = {self.id_conta};""")

            s = self._cursor.fetchall()

            return s[0][0]
        else:
            return None

    @property
    def user_login(self):
        return self._user_login

    @user_login.setter
    def user_login(self, user):
        self._user_login = user

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico_conta(self):
        return self._hitorico_conta


if __name__ == "__main__":
   cont = conta()

   import time

   #print(cont.cliente.inserir_cliente('josef','joestar','2000/02/22','10101110101'))
   #print(cont.inserir_conta('10101010101',1000,10000,'123','jose'))

   print(cont.logar_conta('maria123','1234'))
   print(cont.dados_conta())
   print(cont.depositar(300))
   #print(cont.historico_transacoes())
   print(cont.saldo)

   time.sleep(40)

   print(cont.saldo)



