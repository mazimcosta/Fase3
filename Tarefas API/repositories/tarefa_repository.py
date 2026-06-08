
from database.connection import conectar
from models.tarefa import Tarefa

class TarefaRepository:

    def __init__(self):
        ...


    def listar_tarefas(self):
        conexao=conectar()
        cursor=conexao.cursor()

        cursor.execute('''SELECT * FROM tarefas ''')
        dados=cursor.fetchall()
        cursor.close()
        conexao.close()
        if not dados:
            return None
        lista=[]
        for dado in dados:
            tarefa=Tarefa(id=dado[0],titulo=dado[1],descricao=dado[2],status=dado[3])
            lista.append(tarefa)
        return lista
    
    def buscar_tarefa(self,id):
        conexao=conectar()
        cursor=conexao.cursor()

        cursor.execute("""SELECT * FROM tarefas WHERE id = %s """,(id,))
        dados=cursor.fetchone()
        cursor.close()
        conexao.close()
        if not dados:
            return None
        tarefa=Tarefa(id=dados[0],titulo=dados[1],descricao=dados[2],status=dados[3])
        return tarefa
    
            

    def buscar_por_titulo(self,titulo):
        conexao=conectar()
        cursor=conexao.cursor()

        cursor.execute("""SELECT * FROM tarefas WHERE titulo = %s """,(titulo,))
        dados=cursor.fetchone()
        cursor.close()
        conexao.close()

        if not dados:
            return None
        tarefa=Tarefa(id=dados[0],titulo=dados[1],descricao=dados[2],status=dados[3])
        return tarefa

                
    def cadastrar_tarefa(self,tarefa:Tarefa):
        conexao=conectar()
        cursor=conexao.cursor()

        try:
            cursor.execute("""INSERT INTO tarefas (titulo,descricao,status)
                           VALUES (%s,%s,%s) """,(tarefa.titulo,tarefa.descricao,tarefa.status))
            conexao.commit()
        except Exception:
            conexao.rollback()
            raise {"erro":"Operacao de cadastro nao pode ser realizada"}
        finally:
            cursor.close()
            conexao.close()

    
    def concluir_tarefa(self,id,status):
        conexao=conectar()
        cursor=conexao.cursor()

        try:
            cursor.execute("""UPDATE tarefas SET status = %s WHERE id = %s  """,(status,id))
            conexao.commit()
        except Exception:
            raise {"Erro":"Atualizacao de tarefa nao pode ser realizada"}
        finally:
            cursor.close()
            conexao.close()