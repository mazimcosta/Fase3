
from models.quarto import Quarto
from repositories.quarto_repository import QuartoRepository

class QuartoService:

    def __init__(self,repositorio):
        self.repositorio=repositorio

    def listar_quartos(self):
        lista=self.repositorio.listar_quartos()
        if not lista:
            raise ValueError('Quartos nao cadastrados')
        return lista
    
    def buscar_quarto(self,id):
        quarto=self.repositorio.buscar_por_id(id)
        if not quarto:
            raise ValueError('Quarto nao cadastrado')
        return quarto
    
    def buscar_por_numero(self,numero):
            quarto=self.repositorio.buscar_por_numero(numero)
            if not quarto:
                raise ValueError('Quarto nao encontrado')
            return quarto
    

    def cadastrar_quarto(self,quarto:Quarto):
        quarto_existe=self.repositorio.buscar_por_numero(quarto.numero)
        if quarto_existe:
            raise ValueError('Quarto ja cadastrado')
        self.repositorio.cadastrar_quarto(quarto)

    def remover_quarto(self,id):
        quarto_existe=self.repositorio.buscar_por_id(id)
        if not quarto_existe:
            raise ValueError('Quarto nao encontrado')
        self.repositorio.remover_por_id(id)