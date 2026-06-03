from models.cliente import Cliente
from repositories.cliente_repository import ClienteRepository

class ClienteService:

    def __init__(self,repositorio):
        self.repositorio=repositorio

    def listar_clientes(self):
        lista=self.repositorio.listar_clientes()
        if not lista:
            raise ValueError('Nao ha clientes cadastrados')
        return lista
    
    def buscar_cliente_id(self,id):
        cliente=self.repositorio.buscar_por_id(id)
        if not cliente:
            raise ValueError('Cliente nao cadastrado')
        return cliente
    
    def cadastrar_cliente(self,cliente:Cliente):
        cliente_existe=self.repositorio.buscar_por_cpf(cliente.cpf)
        if cliente_existe:
            raise ValueError('Cliente ja cadastrado')
        self.repositorio.cadastrar_cliente(cliente)

    def remover_cliente(self,id):
        cliente_existe=self.repositorio.buscar_por_id(id)
        if not cliente_existe:
            raise ValueError('Cliente nao encontrado')
        self.repositorio.remover_por_id(id)