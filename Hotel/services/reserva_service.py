
from models.reserva import Reserva
from repositories.reserva_repository import ReservaRepository

class ReservaService:

    def __init__(self,repositorio,cliente_repositorio,quarto_repositorio):
        self.repositorio=repositorio
        self.cliente_repositorio=cliente_repositorio
        self.quarto_repositorio=quarto_repositorio


    def listar_reserva(self):
        lista=self.repositorio.listar_reservas()
        if not lista:
            raise ValueError('Nao ha reservas cadastradas')
        return lista
    
    def buscar_reserva(self,id):
        reserva=self.repositorio.buscar_por_id(id)
        if not reserva:
            raise ValueError('Reserva nao encontrada')
        
        return reserva
    
    def cancelar_reserva(self,id):
        reserva=self.buscar_reserva(id)
        if not reserva:
            raise ValueError('Reserva nao encontrada')
        
        quarto_id=reserva[2]
        self.quarto_repositorio.atualizar_disponibilidade(quarto_id,1)
        self.repositorio.remover_por_id(id)


    def criar_reserva(self,reserva:Reserva):
                
        cliente=self.cliente_repositorio.buscar_por_id(reserva.cliente_id)
        if not cliente:
            raise ValueError('Cliente nao cadastrado')
        
        quarto=self.quarto_repositorio.buscar_por_id(reserva.quarto_id)
        if not quarto:
            raise ValueError('Quarto nao cadastrado')
        
        if quarto[4]==0:
            raise ValueError('Quarto indisponivel')
        
        self.repositorio.cadastrar_reserva(reserva)
        self.quarto_repositorio.atualizar_disponibilidade(reserva.quarto_id,0)
        
