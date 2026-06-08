from models.livro import Livro
from repositories.livro_repository import LivroRepository
from services.livro_service import LivroService
from schemas.livro_schema import LivroCreate,LivroResponse
from fastapi import APIRouter
from fastapi import HTTPException


livro_repositorio=LivroRepository()
livro_service=LivroService(livro_repositorio)

router=APIRouter(prefix="/livros",tags=["Livros"])

@router.get('/',status_code=200,response_model=list[LivroResponse])
def listar_livros():
    try:
        return livro_service.listar_livros()
    except ValueError as error:
        raise HTTPException(status_code=404,detail=str(error))
    
@router.get('/{id}',status_code=200,response_model=LivroResponse)
def buscar_livro(id:int):
    try:
        return livro_service.buscar_livro(id)
    except ValueError as error:
        raise HTTPException(status_code=404,detail=str(error))
    
@router.post('/',status_code=201)
def cadastrar_livro(livro:LivroCreate):
    livro=Livro(titulo=livro.titulo,autor=livro.autor,isbn=livro.isbn)
    try:
        livro_service.cadastrar_livro(livro)
        return {"mensagem":"Livro cadastrado com sucesso"}
    except ValueError as error:
        raise HTTPException(status_code=400,detail=str(error))
    
@router.put('/{id}',status_code=200)
def atualizar_disponibilidade(id:int,disponivel:bool):
    try:
        livro_service.atualizar_disponibilidade(id,disponivel)
        return {'mensagem':"Disponibilidade atualizada com sucesso"}
    except ValueError as error:
        raise HTTPException(status_code=400,detail=str(error))
    