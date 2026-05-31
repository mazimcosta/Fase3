

from models.veiculo import Veiculo
from repositories.veiculo_repository import VeiculoRepository

class VeiculoService:

    def __init__(self,repositorio):
        self.__repositorio=repositorio


    def buscar_veiculo(self,id):
        veiculo_existe=self.__repositorio.buscar_por_id(id)
        if veiculo_existe is None:
            raise ValueError('Veiculo nao encontrado')
        veiculo=self.__repositorio.buscar_por_id(id)
        return veiculo
    
    def listar_veiculos(self):
        lista=self.__repositorio.listar_veiculos()
        if not lista:
            raise ValueError('Nao ha veiculos cadastrados')
        return lista
    

    def cadastrar_veiculo(self,veiculo:Veiculo):
        veiculo_existe=self.__repositorio.buscar_por_id(veiculo.id)
        if veiculo_existe is not None:
            raise ValueError('Veiculo ja cadastrado')
        self.__repositorio.cadastrar_veiculo(veiculo)

    def alugar_veiculo(self,id:int,disponivel:int):
        veiculo= self.buscar_veiculo(id)
        disponibilidade=veiculo[-1]
        if disponibilidade==0:
            raise ValueError('Veiculo ja esta alugado')
        self.__repositorio.atualizar_disponibilidade(id,disponivel)

    def devolver_veiculo(self,id:int,disponivel:int):
        veiculo=self.buscar_veiculo(id)
        disponibilidade=veiculo[-1]
        if disponibilidade==1:
            raise ValueError('Veiculo ja esta disponivel')
        self.__repositorio.atualizar_disponibilidade(id,disponivel)

    def remover_veiculo(self,id):
        self.buscar_veiculo(id)
        self.__repositorio.remover_por_id(id)
