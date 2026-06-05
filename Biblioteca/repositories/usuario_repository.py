
from models.usuario import Usuario
from database.connection import conectar

class UsuarioRepository:

    def __init__(self):
        ...

    
    def listar_usuario(self):
        conexao=conectar()
        cursor=conexao.cursor()

        cursor.execute('''SELECT * FROM usuarios ''')
        lista=cursor.fetchall()
        cursor.close()
        conexao.close()
        return lista

    def buscar_por_id(self,id):
        conexao=conectar()
        cursor=conexao.cursor()

        cursor.execute("""SELECT * FROM usuarios WHERE id = %s """,(id,))
        usuario=cursor.fetchone()
        cursor.close()
        conexao.close()
        return usuario
    
    def buscar_por_cpf(self,cpf):
        conexao=conectar()
        cursor=conexao.cursor()

        cursor.execute("""SELECT * FROM usuarios WHERE cpf = %s """,(cpf,))
        usuario=cursor.fetchone()
        cursor.close()
        conexao.close()
        return usuario

    

    def cadastrar_usuario(self,usuario:Usuario):
        conexao=conectar()
        cursor=conexao.cursor()

        cursor.execute(""" INSERT INTO usuarios (nome,cpf)
                       VALUES(%s,%s)""",(usuario.nome,usuario.cpf))
        conexao.commit()
        cursor.close()
        conexao.close()

    def remover_usuario(self,id):
        conexao=conectar()
        cursor=conexao.cursor()

        cursor.execute("""DELETE FROM usuarios WHERE id = %s """,(id,))
        conexao.commit()
        cursor.close()
        conexao.close()