from pydantic import BaseModel

class Veiculo(BaseModel):
    modelo:str
    marca:str
    ano:int
    disponivel:int

    