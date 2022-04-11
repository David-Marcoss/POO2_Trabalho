from classes_conta import *
from funcoes_auxiliares import *

import socket


host = 'localhost'
porta = 8039

addr = (host,porta)

servidor = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #cria o socket e define o tipo de conexao e o tipo do protocolo de comunicaço
servidor.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) #reinicializa o socket, para que possamos usar a porta novamente
servidor.bind(addr) #define o endereçõ do servidor
servidor.listen(10) #define o limite de conexao

print('\nAGUARDANDO CONEXAO...')

conexao, c = servidor.accept() # servidor aguarda uma conexao

msg_recebida = ''

contab = conta()

while(msg_recebida != 'encerrar'):

    msg_recebida = conexao.recv(1024).decode()
    print(f'{msg_recebida}')
    operacao = trata_mensagen(msg_recebida)

    if(operacao[0] == 'cadastrar'): #[op 0,nome 1,sobrenome 2,data 3,cpf 4,saldo 5,limite 6,senha 7,usuario 8][cadastrar,sara,mendes,12/03/1950,89898989898,1000,10000,123,sara]
        cpf = valida_cpf(operacao[4])
        saldo = v_float(operacao[5])
        limite = v_float(operacao[6])
        data_nascimento = trata_data(operacao[3])

        if saldo != None and cpf == True and limite != None:

            if contab.cliente.inserir_cliente(operacao[1],operacao[2],data_nascimento,operacao[4]):
                if contab.inserir_conta(operacao[4],saldo,limite,operacao[7],operacao[8]):

                    conexao.send('0,Cadastro realizado com sucesso!!!'.encode())
                else:
                    contab.cliente.remover_cliente(operacao[4])
                    conexao.send('1,Nao foi possivel realizar cadastro nome de ususario ja cadastrado!!!'.encode())
            else:
                conexao.send('1,Nao foi possivel realizar cadastro cpf ja cadastrado!!!'.encode())

        else:
            conexao.send('1,Nao foi possivel realizar cadastro dados invalidos!!!'.encode())


    elif (operacao[0] == 'logar'): #[op 0, usuario 1, senha 2]

        if contab.logar_conta(operacao[1],operacao[2]):
            conexao.send('0,Login realizado com sucesso!!!'.encode())
        else:
            conexao.send('1,Nao foi possivel fazer login dados usuario ou senha invalido!!!'.encode())


    elif (operacao[0] == 'ver dados'):
        dados_conta = contab.dados_conta()

        if dados_conta != None:
            dados_conta = concatenar_operacao(dados_conta)
            conexao.send(('0,' + dados_conta).encode())
        else:
            conexao.send('1,Nao foi possivel concluida operaçao!!!'.encode())


    elif (operacao[0] == 'extrato'):

        extrato  = contab.extrato()
        if(extrato != None):
            conexao.send(('0,' +extrato).encode())
        else:
            conexao.send('1,Nao foi possivel concluida operaçao!!!'.encode())


    elif (operacao[0] == 'sacar'): # [op 0, valor 1]
        valor = v_float(operacao[1])

        if valor != None:
            if contab.sacar(valor):
                conexao.send('0,Operaçao concluida com sucesso'.encode())
            else:
                conexao.send('1,Nao foi possivel concluida operaçao!!!'.encode())
        else:
            conexao.send('1,Nao foi possivel concluida operaçao entrada invalida!!!'.encode())


    elif (operacao[0] == 'depositar'):  # [op 0, valor 1]
        valor = v_float(operacao[1])

        if valor != None:
            if contab.depositar(valor):
                conexao.send('0,Operaçao concluida com sucesso'.encode())
            else:
                conexao.send('1,Nao foi possivel concluida operaçao!!!'.encode())
        else:
            conexao.send('1,Nao foi possivel concluida operaçao entrada invalida!!!'.encode())

    elif (operacao[0] == 'transferir'):  # [op 0, id_destino 1, valor 2]
        id_destino = v_int(operacao[1])
        valor = v_float(operacao[2])

        if valor != None and id_destino != None:

            if contab.transferencia(id_destino,valor):
                conexao.send('0,Operaçao concluida com sucesso'.encode())
            else:
                conexao.send('1,Nao foi possivel concluida operaçao!!\nverifique se o valor e o numero da conta de destino estao certos!!'.encode())
        else:
            conexao.send('1,Nao foi possivel concluida operaçao entrada invalida!!!'.encode())

    elif (operacao[0] == 'historico'):  # [op 0, valor 1]

        hist = contab.historico_transacoes()
        if hist != None:
            conexao.send(('0,' +hist).encode())
        else:
            conexao.send('1,Nao foi possivel concluida operaçao!!!'.encode())

    elif (operacao[0] == 'remover conta'):  # [op 0, valor 1]

        if contab.remover_conta_banco():
            conexao.send(('0,Conta Removida com sucesso').encode())
        else:
            conexao.send('1,Nao foi possivel concluida operaçao!!!\nA conta ainda possui saldo!!!'.encode())


    elif (operacao[0] == 'deslogar'):  # [op 0, valor 1]
        contab.deslogar()
        conexao.send('1,Usuario deslogado!!!'.encode())

    else:
        conexao.send('1,OPERACAO INVALIDA'.encode())

conexao.send('1,Conexao encerrada!!!'.encode())
contab.desconectar()
servidor.close()

