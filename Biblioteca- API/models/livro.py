
class Livro:

    def __init__(self,titulo,autor,isbn,disponivel=True,id=None):
        self.id=id
        self.titulo=titulo
        self.autor=autor
        self.isbn=isbn
        self.__disponivel=disponivel

    @property
    def disponivel(self):
        return self.__disponivel