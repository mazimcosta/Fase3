
from models.usuario import Usuario
from repositories.usuario_repository import UsuarioRepository


class UsuarioService:

    def __init__(self,usuario_repositorio):
        self.usuario_repositorio=usuario_repositorio

    def listar_usuarios(self):

        lista=self.usuario_repositorio.listar_usuario()
        if not lista:
            raise ValueError('Nao ha usuarios cadastrados')
        return lista
    
    def buscar_usuario(self,id:int):
        usuario=self.usuario_repositorio.buscar_por_id(id)
        if not usuario:
            raise ValueError('Usuario nao cadastrado')
        return usuario
    
    def cadastrar_usuario(self,usuario:Usuario):
        usuario_existe=self.usuario_repositorio.buscar_por_cpf(usuario.cpf)
        if usuario_existe:
            raise ValueError('Usuario ja cadastrado')
        self.usuario_repositorio.cadastrar_usuario(usuario)

    def remover_usuario(self,id):
        usuario=self.buscar_usuario(id)
        self.usuario_repositorio.remover_usuario(id)
