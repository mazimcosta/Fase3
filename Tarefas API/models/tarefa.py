

class Tarefa:

    def __init__(self,titulo,descricao,status='pendente',id=None):
        self.id=id
        self.titulo=titulo
        self.descricao=descricao
        self.__status=status


    @property
    def status(self):
        return self.__status
    
    
