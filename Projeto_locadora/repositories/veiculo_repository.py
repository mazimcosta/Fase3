import sqlite3

class VeiculoRepository:

    def __init__(self,caminho_arquivo='data/veiculos.db'):
        self.caminho_arquivo=caminho_arquivo

    def conectar(self):
        conexao=sqlite3.connect(self.caminho_arquivo)
        return conexao
    
    def listar_veiculos(self):
        conexao=self.conectar()
        cursor=conexao.cursor()

        cursor.execute('''SELECT * FROM veiculos ''')
        lista=cursor.fetchall()
        if not lista:
            raise ValueError('Nao ha veiculos cadastrados')
        conexao.close()
        return lista
    
    def buscar_modelo(self,modelo):
        conexao=self.conectar()
        cursor=conexao.cursor()

        cursor.execute('''SELECT * FROM veiculos WHERE modelo = ? ''',(modelo,))
        modelo=cursor.fetchone()
        conexao.close()
        return modelo