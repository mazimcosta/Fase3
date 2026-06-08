
from models.tarefa import Tarefa
from repositories.tarefa_repository import TarefaRepository
from services.tarefa_service import TarefaService
from schemas.tarefa_schema import TarefaCreate, TarefaResponse
from fastapi import APIRouter
from fastapi import HTTPException

repositorio=TarefaRepository()
tarefa_service=TarefaService(repositorio)

router= APIRouter(prefix="/tarefas", tags=["Tarefas"])

@router.get('/',response_model=list[TarefaResponse],status_code=200)
def listar_tarefas():
    try:
        return tarefa_service.listar_tarefas()
    except ValueError as error:
        raise HTTPException(status_code=404,detail=str(error))
    
@router.get('/{id}',response_model=TarefaResponse,status_code=200)
def buscar_tarefa(id:int):
    try:
        return tarefa_service.buscar_tarefa(id)
    except ValueError as error:
        raise HTTPException(status_code=404,detail=str(error))
    

@router.post('/',status_code=201)
def cadastrar_tarefa(tarefa:TarefaCreate):
    tarefa=Tarefa(titulo=tarefa.titulo,descricao=tarefa.descricao)
    try:
        tarefa_service.cadastrar_tarefa(tarefa)
        return {"mensagem":"Tarefa cadastrada com sucesso"}
    except ValueError as error:
        raise HTTPException(status_code=400,detail=str(error))
    

@router.put('/{id}',status_code=200)
def concluir_tarefa(id:int):
    try:
        tarefa_service.concluir_tarefa(id)
        return {"mensagem":"Tarefa concluida com sucesso"}
    except ValueError as error:
        raise HTTPException(status_code=400,detail=str(error))
