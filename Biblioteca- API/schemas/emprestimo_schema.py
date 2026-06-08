
from pydantic import BaseModel
from datetime import datetime
class EmprestimoCreate(BaseModel):
    usuario_id:int
    livro_id:int
    

class EmprestimoResponse(BaseModel):
    id:int
    usuario_id:int
    livro_id:int
    data_emprestimo:datetime
    data_devolucao:datetime | None