from pydantic import BaseModel

class UsuarioCreate(BaseModel):
    nome:str
    cpf:str


class UsuarioResponse(BaseModel):
    id:int
    nome:str
    cpf:str