
from pydantic import BaseModel

class TarefaCreate(BaseModel):
    titulo:str
    descricao:str


class TarefaResponse(BaseModel):
    id:int
    titulo:str
    descricao:str
    status:str