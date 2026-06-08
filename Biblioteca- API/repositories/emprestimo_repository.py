
from models.emprestimo import Emprestimo
from database.connection import conectar
class EmprestimoRepository:

    def __init__(self):
        ...
        
    def listar_emprestimos(self):
        conexao=conectar()
        cursor=conexao.cursor()

        cursor.execute(""" SELECT * FROM emprestimos """)
        dados=cursor.fetchall()
        cursor.close()
        conexao.close()
        if not dados:
            return None
        lista=[]
        for dado in dados:
            emprestimo=Emprestimo(id=dado[0],usuario_id=dado[1],livro_id=dado[2],data_emprestimo=dado[3],data_devolucao=dado[4])
            lista.append(emprestimo)
        return lista
    
    def buscar_por_id(self,id):
        conexao=conectar()
        cursor=conexao.cursor()
        
        cursor.execute("""SELECT * FROM emprestimos WHERE id = %s """,(id,))
        dados=cursor.fetchone()
        cursor.close()
        conexao.close()
        if not dados:
            return None
        emprestimo=Emprestimo(id=dados[0],usuario_id=dados[1],livro_id=dados[2],data_emprestimo=dados[3],data_devolucao=dados[4])
        return emprestimo
    
    def cadastrar_emprestimo(self,emprestimo:Emprestimo):
        conexao=conectar()
        cursor=conexao.cursor()

        cursor.execute("""INSERT INTO emprestimos (usuario_id,livro_id,data_emprestimo,data_devolucao)
                       VALUES (%s,%s,%s,%s) """,(emprestimo.usuario_id,emprestimo.livro_id,emprestimo.data_emprestimo,emprestimo.data_devolucao))
        conexao.commit()
        cursor.close()
        conexao.close()

    def atualizar_data_devolucao(self,id,data_devolucao):
        conexao=conectar()
        cursor=conexao.cursor()

        cursor.execute("""UPDATE emprestimos SET data_devolucao = %s WHERE id = %s  """,(data_devolucao,id))
        conexao.commit()
        cursor.close()
        conexao.close()    