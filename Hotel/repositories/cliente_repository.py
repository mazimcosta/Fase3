
from models.cliente import Cliente
import sqlite3

class ClienteRepository:

    def __init__(self,caminho_arquivo='data//hotel.db'):
        self.caminho_arquivo=caminho_arquivo


    def conectar(self):
        conexao=sqlite3.connect(self.caminho_arquivo)
        return conexao
    
    def listar_clientes(self):
        conexao=self.conectar()
        cursor=conexao.cursor()

        cursor.execute('''SELECT * FROM clientes ''')
        lista=cursor.fetchall()
        conexao.close()
        return lista
    
    def buscar_por_id(self,id):
        conexao=self.conectar()
        cursor=conexao.cursor()

        cursor.execute('''SELECT * FROM clientes WHERE id = ? ''',(id,))
        cliente=cursor.fetchone()
        conexao.close()
        return cliente
    
    def buscar_por_cpf(self,cpf):
        conexao=self.conectar()
        cursor=conexao.cursor()

        cursor.execute('''SELECT * FROM clientes WHERE cpf = ? ''',(cpf,))
        cliente=cursor.fetchone()
        conexao.close()
        return cliente
    
    def cadastrar_cliente(self,cliente:Cliente):
        conexao=self.conectar()
        cursor=conexao.cursor()

        cursor.execute('''INSERT INTO clientes (nome,cpf)
                       VALUES (?,?) ''',(cliente.nome,cliente.cpf))
        conexao.commit()
        conexao.close()

    
    def remover_por_id(self,id):
        conexao=self.conectar()
        cursor=conexao.cursor()

        cursor.execute('''DELETE FROM clientes WHERE id =? ''',(id,))
        conexao.commit()
        conexao.close()