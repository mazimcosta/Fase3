from datetime import datetime
class Emprestimo:

    def __init__(self,usuario_id,livro_id,data_emprestimo=None,data_devolucao=None,id=None):
        if data_emprestimo is None:
            data_emprestimo=datetime.now()
            
        self.id=id
        self.usuario_id=usuario_id
        self.livro_id=livro_id
        self.data_emprestimo=data_emprestimo
        self.data_devolucao=data_devolucao

        
        