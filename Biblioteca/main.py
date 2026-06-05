
from services.emprestimo_service import EmprestimoService
from services.livro_service import LivroService
from services.usuario_service import UsuarioService
from repositories.usuario_repository import UsuarioRepository
from repositories.emprestimo_repository import EmprestimoRepository
from repositories.livro_repository import LivroRepository
from models.usuario import Usuario
from models.emprestimo import Emprestimo
from models.livro import Livro
from datetime import datetime


def fluxo_normal():

    usuario_repositorio=UsuarioRepository()
    livro_repositorio=LivroRepository()
    emprestimo_repositorio=EmprestimoRepository()
    usuario_service=UsuarioService(usuario_repositorio)
    livro_service=LivroService(livro_repositorio)
    emprestimo_service=EmprestimoService(emprestimo_repositorio,livro_repositorio,usuario_repositorio)
    emprestimo4=Emprestimo(999,1)
    # Usuario  inexistente:
    
    # try:
    #     emprestimo_service.fazer_emprestimo(emprestimo4)
    # except ValueError as error:
    #     print(error)
    # 
    # 
    emprestimo5=Emprestimo(1,1)
   # Livro inexistente
    # try:
    #     emprestimo_service.fazer_emprestimo(emprestimo5)
    # except ValueError as error:
    #     print(error)

    #Livro indisponivel
    # try:
    #     emprestimo_service.fazer_emprestimo(emprestimo5)
    # except ValueError as error:
    #     print(error)
    
    #Emprestimo inexistente:
    # try:
    #     emprestimo_service.devolver_emprestimo(999,data_devolucao=datetime.now())
    # except ValueError as error:
    #     print(error)

   # duplicidade de usuario:
    # usuario4=Usuario('Antonio','145678')
    # usuario_service.cadastrar_usuario(usuario4)
    # try:
    #     usuario_service.cadastrar_usuario(usuario4)
    # except ValueError as error:
    #     print(error)
    
    # #Usuario com o mesmo cpf:
    # usuario5=Usuario('Carlos','145678')
    # try:
    #     usuario_service.cadastrar_usuario(usuario5)
    # except ValueError as error:
    #     print(error)

    #Cadastrar livro com o mesmo isbn:
    # livro4=Livro('os loucos','Doido','1234')
    # livro_service.cadastrar_livro(livro4)
    livro5=Livro('dafdss','dasd','1234')
    try:
        livro_service.cadastrar_livro(livro5)
    except ValueError as error:
        print(error)
    
    










    
fluxo_normal()
