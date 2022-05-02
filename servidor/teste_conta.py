from classes_conta import conta

banco = conta()

print(banco.logar_conta('joao','123'))
print(banco.sacar(banco.saldo))
print(banco.remover_conta_banco())


