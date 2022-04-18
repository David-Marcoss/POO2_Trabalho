import socket

class conectar_servidor:

    def __init__(self):

        self.host = 'localhost'
        self.porta = 8040
        self.ta_conectado = False
        self.conexao = None

    def enviar_mensagem(self,msg_entrada):

        #print(msg_entrada)

        if self.ta_conectado == False:

            try:
                addr = (self.host, self.porta)
                self.conexao = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  # cria o socket e define o tipo de conexao e o tipo do protocolo de comunicaço
                self.conexao.connect(addr)
                self.ta_conectado = True

            except ConnectionRefusedError:
                return None

        if self.ta_conectado == True:
            self.conexao.send(msg_entrada.encode())
            msg_saida = self.conexao.recv(1024).decode()

            if (msg_entrada == 'encerrar'):
                print('\nconexao encerrada...')
                self.conexao.close()
                self.ta_conectado = False
                return 'conexao encerrada...'

            else:
                #print(msg_saida)
                return msg_saida.split(',')


if __name__ == '__main__':
    cliente = conectar_servidor()

    msg = ''
    while(msg != 'encerrar'):
        msg = input('digite a operação: ')

        saida = cliente.enviar_mensagem(msg)
        print(f"\n{saida}\n")
















