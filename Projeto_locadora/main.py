from models.veiculo import Veiculo
from services.veiculo_service import VeiculoService
from repositories.veiculo_repository import VeiculoRepository
import sqlite3
def fluxo_normal():
    repositorio=VeiculoRepository()
    locadora=VeiculoService(repositorio)
    veiculo5=Veiculo('Camaro','onix',2024,1)
    
    
    
    return repositorio,locadora

repositorio,locadora=fluxo_normal()
#locadora.alugar_veiculo(5, 0)
#print(locadora.buscar_veiculo(5))

#locadora.devolver_veiculo(5, 1)
#print(locadora.buscar_veiculo(5))
try:
    locadora.buscar_veiculo(999)
except ValueError as erro:
    print(erro)

print('Fluxo concluido com sucesso!!!')