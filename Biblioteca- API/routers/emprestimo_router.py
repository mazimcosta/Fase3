
from models.emprestimo import Emprestimo
from repositories.emprestimo_repository import EmprestimoRepository
from services.emprestimo_service import EmprestimoService
from schemas.emprestimo_schema import EmprestimoCreate,EmprestimoResponse
from fastapi import APIRouter
from fastapi import HTTPException
from repositories.livro_repository import LivroRepository
from repositories.usuario_repository import UsuarioRepository
from datetime import datetime

livro_repositorio=LivroRepository()
usuario_repositorio=UsuarioRepository()

emprestimo_repositorio=EmprestimoRepository()
emprestimo_service=EmprestimoService(emprestimo_repositorio,livro_repositorio,usuario_repositorio)




router= APIRouter(prefix="/emprestimos",tags=["Emprestimos"])

@router.get('/',status_code=200,response_model=list[EmprestimoResponse])
def listar_emprestimos():
    try:
        return emprestimo_service.listar_emprestimos()
        
    except ValueError as error:
        raise HTTPException(status_code=404,detail=str(error))


@router.get('/{id}',status_code=200,response_model=EmprestimoResponse)
def buscar_emprestimo(id:int):
    try:
        return emprestimo_service.buscar_emprestimo(id)
    except ValueError as error:
        raise HTTPException(status_code=404,detail=str(error))
    
@router.post('/',status_code=201)
def cadastrar_emprestimo(emprestimo:EmprestimoCreate):
    emprestimo=Emprestimo(usuario_id=emprestimo.usuario_id,livro_id=emprestimo.livro_id)
    try:
        emprestimo_service.fazer_emprestimo(emprestimo)
        return {"mensagem":"Emprestimo feito com sucesso"}
    except ValueError as error:
        raise HTTPException(status_code=400,detail=str(error))
    
@router.put('/{id}',status_code=200)
def devolver_emprestimo(id:int):
    try:
        emprestimo_service.devolver_emprestimo(id)
        return {"mensagem":"Livro devolvido com sucesso"}
    except ValueError as error:
        raise HTTPException(status_code=400,detail=str(error))
