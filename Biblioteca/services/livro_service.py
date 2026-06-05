
from models.livro import Livro
from repositories.livro_repository import LivroRepository


class LivroService:

    def __init__(self,livro_repositorio:LivroRepository):
        self.livro_repositorio=livro_repositorio


    def listar_livros(self):
        lista=self.livro_repositorio.listar_livros()
        if not lista:
            raise ValueError('Nao ha livros cadastrados')
        return lista
    
    def buscar_livro(self,id):
        livro=self.livro_repositorio.buscar_livro(id)
        if not livro:
            raise ValueError('Livro nao cadastrado')
        return livro
    
    def buscar_por_isbn(self,isbn):
        livro=self.livro_repositorio.buscar_por_isbn(isbn)
        if not livro:
            raise ValueError('Livro nao encontrado')
        return livro
    
    def cadastrar_livro(self,livro:Livro):
        livro_existe=self.livro_repositorio.buscar_por_isbn(livro.isbn)
        if livro_existe:
            raise ValueError('Livro ja cadastrado')
        self.livro_repositorio.cadastrar_livro(livro)

    def atualizar_disponibilidade(self,id,disponivel):
        self.buscar_livro(id)
        if type(disponivel) is not bool:
         raise ValueError('Disponibilidade deve ser True ou False')
        self.livro_repositorio.atualizar_disponibilidade(id,disponivel)