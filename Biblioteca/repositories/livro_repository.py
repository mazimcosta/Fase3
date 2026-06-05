from models.livro import Livro
from database.connection import conectar
class LivroRepository:

    def __init__(self):
        ...

    
    def listar_livros(self):
        conexao=conectar()
        cursor=conexao.cursor()

        cursor.execute("""SELECT * FROM livros """)
        lista=cursor.fetchall()
        cursor.close()
        conexao.close()
        return lista
    
    def buscar_livro(self,id):
        conexao=conectar()
        cursor=conexao.cursor()

        cursor.execute("""SELECT * FROM livros WHERE id = %s """,(id,))
        livro=cursor.fetchone()
        cursor.close()
        conexao.close()
        return livro
    
    def buscar_por_isbn(self,isbn):
        conexao=conectar()
        cursor=conexao.cursor()

        cursor.execute("""SELECT * FROM livros WHERE isbn = %s """,(isbn,))
        livro=cursor.fetchone()
        cursor.close()
        conexao.close()
        return livro
    
    def cadastrar_livro(self,livro:Livro):
        conexao=conectar()
        cursor=conexao.cursor()

        cursor.execute("""INSERT INTO livros (titulo,autor,isbn,disponivel)
                       VALUES(%s,%s,%s,%s) """,(livro.titulo,livro.autor,livro.isbn,livro.disponivel))
        conexao.commit()
        cursor.close()
        conexao.close()

    def atualizar_disponibilidade(self,id,disponivel:bool):
        conexao=conectar()
        cursor=conexao.cursor()

        cursor.execute("""UPDATE livros  SET disponivel = %s WHERE id = %s""",(disponivel,id))
        conexao.commit()
        cursor.close()
        conexao.close()

    