from fastapi import APIRouter
from models.usuario import Usuario
from schemas.usuario_schema import UsuarioCreate,UsuarioResponse
from fastapi import HTTPException
from repositories.usuario_repository import UsuarioRepository
from services.usuario_service import UsuarioService

usuario_repositorio= UsuarioRepository()
usuario_service=UsuarioService(usuario_repositorio)


router = APIRouter(prefix='/usuarios',tags=["Usuarios"])

@router.get('/',status_code=200,response_model=list[UsuarioResponse])
def listar_usuarios():
    try:

        return usuario_service.listar_usuarios()
    except ValueError as error:
        raise HTTPException(status_code=404,detail=str(error))
    
@router.get('/{id}',status_code=200,response_model=UsuarioResponse)
def buscar_usuario(id:int):
    try:

        return usuario_service.buscar_usuario(id)
    except ValueError as error:
        raise HTTPException(status_code=404,detail=str(error))
    
@router.post('/',status_code=201)
def cadastrar_usuario(usuario:UsuarioCreate):
    try:
        usuario=Usuario(nome=usuario.nome,cpf=usuario.cpf)
        usuario_service.cadastrar_usuario(usuario)
        return {'mensagem':'Usuario cadastrado com sucesso'}
    except ValueError as error:
        raise HTTPException(status_code=400,detail=str(error))

@router.delete('/{id}')
def remover_usuario(id:int):
    try:
        usuario_service.remover_usuario(id)
        return {"mensagem":"Usuario removido com sucesso"}
    except ValueError as error:
        raise HTTPException(status_code=404,detail=str(error))