
from models.usuario import Usuario
from database.connection import conectar

class UsuarioRepository:

    def __init__(self):
        ...

    
    def listar_usuario(self):
        conexao=conectar()
        cursor=conexao.cursor()

        cursor.execute('''SELECT * FROM usuarios ''')
        dados=cursor.fetchall()
        cursor.close()
        conexao.close()
        lista=[]
        for dado in dados:
            usuario=Usuario(id=dado[0],nome=dado[1],cpf=dado[2])
            lista.append(usuario)
        if not lista:
            return None
        return lista
        

    def buscar_por_id(self,id):
        conexao=conectar()
        cursor=conexao.cursor()

        cursor.execute("""SELECT * FROM usuarios WHERE id = %s """,(id,))
        dados=cursor.fetchone()
        cursor.close()
        conexao.close()
        if not dados:
            return None
        usuario=Usuario(id=dados[0],nome=dados[1],cpf=dados[2])
        return usuario
    
    def buscar_por_cpf(self,cpf):
        conexao=conectar()
        cursor=conexao.cursor()

        cursor.execute("""SELECT * FROM usuarios WHERE cpf = %s """,(cpf,))
        dados=cursor.fetchone()
        cursor.close()
        conexao.close()
        if not dados:
            return None
        usuario=Usuario(id=dados[0],nome=dados[1],cpf=dados[2])
        return usuario
    

    def cadastrar_usuario(self,usuario:Usuario):
        conexao=conectar()
        cursor=conexao.cursor()

        cursor.execute(""" INSERT INTO usuarios (nome,cpf)
                       VALUES(%s,%s)""",(usuario.nome,usuario.cpf))
        conexao.commit()
        cursor.close()
        conexao.close()

    def remover_usuario(self, id):
        conexao = conectar()
        cursor = conexao.cursor()

        try:
            cursor.execute(
                """DELETE FROM usuarios WHERE id = %s""",
                (id,)
            )
            conexao.commit()

        except Exception:
            conexao.rollback()
            raise ValueError(
                "Nao foi possivel remover usuario. Verifique se ele possui emprestimos vinculados"
            )

        finally:
            cursor.close()
            conexao.close()