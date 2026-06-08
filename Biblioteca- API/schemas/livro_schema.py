
from pydantic import BaseModel


class LivroCreate(BaseModel):
    titulo:str
    autor:str
    isbn:str
    

class LivroResponse(BaseModel):
    id:int
    titulo:str
    autor:str
    isbn:str
    disponivel:bool