class cliente:

    __slots__ = ['_cpf','_nome','_sobrenome']

    def __init__(self,cpf,nome,sobrenome):
        self._cpf = cpf
        self._nome = nome
        self._sobrenome = sobrenome

    def dados(self):
        print(f"\nnome: {self.nome}\nsobrenome: {self.sobrenome}\ncpf: {self.cpf}")

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

