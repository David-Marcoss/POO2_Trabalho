from classes_conta import conta
import unittest

class TesteConta(unittest.TestCase):

    def test_cadastro_cliente(self):
        """
        teste função cadastrar cliente
        :return: sem retorno
        """

        banco = conta()
        self.assertEqual(banco.cliente.inserir_cliente('joao','carlos','2001/02/22','00000000000'),True)       #testa inserção de um cliente nao cadastrado
        self.assertEqual(banco.cliente.inserir_cliente('Mario', 'carlos', '2001/02/22', '00011122253'), True)  #testa inserção de um cliente nao cadastrado
        self.assertEqual(banco.cliente.inserir_cliente('Mario', 'carlos', '2001/02/22', '00011122253'), False)  #testa inserção de um cliente com cpf já cadastrado

    def test_cadastro_conta(self):
        """
        teste função cadastrar conta
        :return: sem retorno
        """
        banco = conta()
        self.assertEqual(banco.inserir_conta('00011122253',1000,10000,'123','Mario'), True)
        self.assertEqual(banco.inserir_conta('00000000000',10000,10000,'123','joao'), True)             #testa quando os dados para a criação da conta sao validos
        self.assertEqual(banco.inserir_conta('00000000000', 1000, 10000, '123', 'joaozinho'), False)   #testa quando o cliente ja possui conta
        self.assertEqual(banco.inserir_conta('00011122250',1000,10000,'123','Mario'), False)        #testa quando o nome de usuario ja foi cadastrado

    def test_login(self):
        banco = conta()
        self.assertEqual(banco.logar_conta('maria123','1234'), True)           #testa login com usuario e senha corretos
        self.assertEqual(banco.logar_conta('maria123', '12345') , None)        #testa login com senha incorreta
        self.assertEqual(banco.logar_conta('maria12','1234') , None)           #testa login com usuario incorreto

    def test_deposito(self):
        """
        teste função deposito
        :return: sem retorno
        """
        banco = conta()

        self.assertEqual(banco.depositar(100), False)  # testa depositar um valor do banco quando nao posui nenhuma conta logada

        banco.logar_conta('joao', '123')
        self.assertEqual(banco.depositar(-100), False)  # testa depositar um valor negativo
        self.assertEqual(banco.depositar(1000), True)  # testa depositar um valor valido

    def test_transferencia(self):
        """
        teste função transferencia
        :return: sem retorno
        """
        banco = conta()
        self.assertEqual(banco.transferencia(2,100), False)  # testa transferir um valor de uma conta quando nao posui nenhuma conta logada

        banco.logar_conta('joao', '123')
        self.assertEqual(banco.transferencia(1234, 100),False)  # testa transferir um valor para uma conta que nao exite
        self.assertEqual(banco.transferencia(2, -100), False)  # testa transferir um valor negativo para uma conta
        self.assertEqual(banco.transferencia(2, 100500), False)  # testa transferir um valor maior do que o saldo da conta para uma conta
        self.assertEqual(banco.transferencia(1, 1000), True)  # testa transferir um valor valido para uma conta existente

    def test_saque(self):
        """
        teste função saque
        :return: sem retorno
        """
        banco = conta()
        self.assertEqual(banco.sacar(100),False)  # testa sacar um valor do banco quando nao posui nenhuma conta logada

        banco.logar_conta('joao', '123')
        self.assertEqual(banco.sacar(-100), False)  # testa sacar um valor negativo
        self.assertEqual(banco.sacar(100500), False)  # testa sacar um valor maior do que o saldo da conta
        self.assertEqual(banco.sacar(1000), True)  # testa sacar um valor valido


    def test_remover_conta(self):
        """
        teste função remover conta
        :return: sem retorno
        """
        banco = conta()
        self.assertEqual(banco.remover_conta_banco(), None)  # testa remover uma conta quando nao posui nenhuma conta logada

        banco.logar_conta('maria1234', '123')
        self.assertEqual(banco.remover_conta_banco(),None)  # testa remover uma conta quando a conta logada ainda possui saldo

        banco.logar_conta('Mario', '123')
        banco.sacar(banco.saldo)
        self.assertEqual(banco.remover_conta_banco(),True)  # testa remover uma conta quando a conta logada ainda possui saldo


if __name__ == '__name__':
    unittest.main()