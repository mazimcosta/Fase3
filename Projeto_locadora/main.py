from models.veiculo import Veiculo
from services.veiculo_service import VeiculoService
from repositories.veiculo_repository import VeiculoRepository

def fluxo_normal():
    repositorio=VeiculoRepository()
    locadora=VeiculoService(repositorio)
    
    locadora.buscar_veiculo(1)
    locadora.alugar_veiculo(2,0)
    locadora.devolver_veiculo(2,1)
    locadora.listar_veiculos()
    locadora.remover_veiculo(4)

    return repositorio,locadora

fluxo_normal()

