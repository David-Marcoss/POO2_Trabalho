from classes_conta import *
from class_cliente import *
from class_banco import banco


cliente1 = cliente("123.456.321-22","joao","carlos")
cliente2 = cliente("113.756.821-92","Maria","Antonia")
cliente3 = cliente("173.756.821-77","Claudete","Francisca")

c1 = conta(1,cliente1,100,1)
c2 = conta(2,cliente2,10000,30000,1)
c3 = conta(3,cliente3,5000,30000,1)

banco = banco()

banco.criar_conta(c1)
banco.criar_conta(c2)
banco.criar_conta(c3)

print(banco._contas)

banco.remover_conta(2)

print(banco._contas)

print(c2.extrato())


if banco.criar_conta(c1) == False:
    print("ERRO")

conta = banco.buscar_conta(1)

print(conta.id_conta)

"""
c1.extrato()
c1.depositar(1000)
c1.sacar(300)

if (c3.sacar(10000)):
    print("\nSaque concluido!!\n")
else:
    print("\nnao foi possivel concluir o saque")

if (c2.transfere(1000,c1)):
    print("\ndeposito concluido!!\n")
else:
    print("nao foi possivel concluir a a transferencia")

if (c1.transfere(11000,c1)):
    print("\ndeposito concluido!!\n")
else:
    print("nao foi possivel concluir a transferencia")


c1.historico.imprimir_historico()
c2.historico.imprimir_historico()

"""