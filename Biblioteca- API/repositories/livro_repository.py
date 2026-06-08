from models.livro import Livro
from database.connection import conectar
class LivroRepository:

    def __init__(self):
        ...

    
    def listar_livros(self):
        conexao=conectar()
        cursor=conexao.cursor()

        cursor.execute("""SELECT * FROM livros """)
        dados=cursor.fetchall()
        cursor.close()
        conexao.close()
        lista=[]
        if not dados:
            return None
        for dado in dados:
            livro=Livro(id=dado[0],titulo=dado[1],autor=dado[2],isbn=dado[3],disponivel=dado[4])
            lista.append(livro)
        return lista



    
    def buscar_livro(self,id):
        conexao=conectar()
        cursor=conexao.cursor()

        cursor.execute("""SELECT * FROM livros WHERE id = %s """,(id,))
        dados=cursor.fetchone()
        cursor.close()
        conexao.close()
        if not dados:
            return None
        livro=Livro(id=dados[0],titulo=dados[1],autor=dados[2],isbn=dados[3],disponivel=dados[4])
        return livro
    
    def buscar_por_isbn(self,isbn):
        conexao=conectar()
        cursor=conexao.cursor()

        cursor.execute("""SELECT * FROM livros WHERE isbn = %s """,(isbn,))
        dados=cursor.fetchone()
        cursor.close()
        conexao.close()
        if not dados:
            return None
        livro=Livro(id=dados[0],titulo=dados[1],autor=dados[2],isbn=dados[3],disponivel=dados[4])
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

    