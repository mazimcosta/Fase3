from datetime import datetime
class Emprestimo:

    def __init__(self,usuario_id,livro_id,data_emprestimo=datetime.now(),data_devolucao=None):
        self.usuario_id=usuario_id
        self.livro_id=livro_id
        self.data_emprestimo=data_emprestimo
        self.data_devolucao=data_devolucao

        
        