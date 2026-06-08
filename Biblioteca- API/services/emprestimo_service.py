
from repositories.emprestimo_repository import EmprestimoRepository
from repositories.livro_repository import LivroRepository
from repositories.usuario_repository import UsuarioRepository
from models.emprestimo import Emprestimo
from datetime import datetime

class EmprestimoService:

    def __init__(self,emprestimo_repositorio:EmprestimoRepository,livro_repositorio:LivroRepository,usuario_repositorio:UsuarioRepository):
        self.emprestimo_repositorio=emprestimo_repositorio
        self.livro_repositorio=livro_repositorio
        self.usuario_repositorio=usuario_repositorio

    def listar_emprestimos(self):
        lista=self.emprestimo_repositorio.listar_emprestimos()
        if not lista:
            raise ValueError('Nao ha emprestimos cadastrados')
        return lista
    
    def buscar_emprestimo(self,id):
        emprestimo=self.emprestimo_repositorio.buscar_por_id(id)
        if not emprestimo:
            raise ValueError('Emprestimo nao encontrado')
        return emprestimo
    
    def fazer_emprestimo(self,emprestimo:Emprestimo):
        usuario=self.usuario_repositorio.buscar_por_id(emprestimo.usuario_id)
        if not usuario:
            raise ValueError('Usuario nao encontrado')
        
        livro=self.livro_repositorio.buscar_livro(emprestimo.livro_id)
        if not livro:
            raise ValueError('Livro inexistente')
        if livro.disponivel is False:
            raise ValueError('Livro indisponivel')
                
        self.emprestimo_repositorio.cadastrar_emprestimo(emprestimo)
        self.livro_repositorio.atualizar_disponibilidade(livro.id,disponivel=False)


    def devolver_emprestimo(self,id):
        emprestimo=self.emprestimo_repositorio.buscar_por_id(id)
        if not emprestimo:
            raise ValueError('Emprestimo nao encontrado')
        data_devolucao=datetime.now()
        
        livro=self.livro_repositorio.buscar_livro(emprestimo.livro_id)
        if livro.disponivel is True:
            raise ValueError('Livro ja esta disponivel')
                
        self.livro_repositorio.atualizar_disponibilidade(emprestimo.livro_id,True)
        self.emprestimo_repositorio.atualizar_data_devolucao(id,data_devolucao)
        