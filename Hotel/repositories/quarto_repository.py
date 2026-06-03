

from models.quarto import Quarto
import sqlite3

class QuartoRepository:

    def __init__(self,caminho_arquivo='data//hotel.db'):
        self.caminho_arquivo=caminho_arquivo


    def conectar(self):
        conexao=sqlite3.connect(self.caminho_arquivo)
        return conexao
    

    def listar_quartos(self):
        conexao=self.conectar()
        cursor=conexao.cursor()

        cursor.execute('''SELECT * FROM quartos ''')
        lista=cursor.fetchall()
        conexao.close()
        return lista
    
    def buscar_por_id(self,id):
        conexao=self.conectar()
        cursor=conexao.cursor()

        cursor.execute(''' SELECT * FROM quartos WHERE id = ? ''',(id,))
        quarto=cursor.fetchone()
        conexao.close()
        return quarto
    
    def buscar_por_numero(self,numero):
        conexao=self.conectar()
        cursor=conexao.cursor()

        cursor.execute('''SELECT * FROM quartos WHERE numero = ? ''',(numero,))
        quarto=cursor.fetchone()
        conexao.close()
        return quarto
    
    def cadastrar_quarto(self,quarto:Quarto):
        conexao=self.conectar()
        cursor=conexao.cursor()

        cursor.execute('''INSERT INTO quartos (numero,tipo,preco_diaria,disponivel)
                       VALUES (?,?,?,?) ''',(quarto.numero,quarto.tipo,quarto.preco_diaria,quarto.disponivel))
        conexao.commit()
        conexao.close()

    def atualizar_disponibilidade(self,id,disponivel):
        conexao=self.conectar()
        cursor=conexao.cursor()

        cursor.execute('''UPDATE quartos SET disponivel = ? WHERE id = ? ''',(disponivel,id))
        conexao.commit()
        conexao.close()

    def remover_por_id(self,id):
        conexao=self.conectar()
        cursor=conexao.cursor()

        cursor.execute('''DELETE FROM quartos WHERE id = ? ''',(id,))
        conexao.commit()
        conexao.close()