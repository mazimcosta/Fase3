
class Usuario:

    def __init__(self,nome,cpf):
        self.nome=nome
        self.__cpf=cpf

    @property
    def cpf(self):
        return self.__cpf