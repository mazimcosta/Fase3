from models.tarefa import Tarefa


class TarefaService:

    def __init__(self,repositorio):
        self.repositorio=repositorio

    
    def listar_tarefas(self):
        lista=self.repositorio.listar_tarefas()
        if not lista:
            raise ValueError('Nao ha tarefas cadastradas')
        return lista
    
    def buscar_tarefa(self,id):
        tarefa=self.repositorio.buscar_tarefa(id)
        if not tarefa:
            raise ValueError('Tarefa nao cadastrada')
        return tarefa
    
    def cadastrar_tarefa(self,tarefa:Tarefa):
        tarefa_existe=self.repositorio.buscar_por_titulo(tarefa.titulo)
        if  tarefa_existe:
            raise ValueError('Tarefa ja cadastrada')
        self.repositorio.cadastrar_tarefa(tarefa)

    
    def concluir_tarefa(self,id,status='concluida'):
        tarefa=self.buscar_tarefa(id)
        if tarefa.status=='concluida':
            raise ValueError('Tarefa ja concluida')
        self.repositorio.concluir_tarefa(id,status)
