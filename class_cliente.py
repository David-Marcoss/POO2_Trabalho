class cliente:

    __slots__ = ['_cliente_id','_cpf','_nome','_sobrenome','_data_nascimento']

    def __init__(self,id,cpf,nome,sobrenome,data):

        self._cliente_id = id
        self._cpf = cpf
        self._nome = nome
        self._sobrenome = sobrenome
        self._data_nascimento = data

    def dados(self):
        print(f"\nid: {self.cliente_id}\nnome: {self.nome}\nsobrenome: {self.sobrenome}\ncpf: {self.cpf}\nnascimento:{self.data_nascimento}")

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

