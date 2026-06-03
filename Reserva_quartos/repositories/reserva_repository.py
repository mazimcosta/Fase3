
from models.reserva import Reserva
import sqlite3


class ReservaRepository:

    def __init__(self,caminho_arquivo='data//hotel.db'):
        self.caminho_arquivo=caminho_arquivo

    def conectar(self):
        conexao=sqlite3.connect(self.caminho_arquivo)
        return conexao
    
    def listar_reservas(self):
        conexao=self.conectar()
        cursor=conexao.cursor()

        cursor.execute('''SELECT * FROM reservas ''')
        lista=cursor.fetchall()
        conexao.close()
        return lista
    
    def buscar_por_id(self,id):
        conexao=self.conectar()
        cursor=conexao.cursor()
                
        cursor.execute('''SELECT * FROM reservas WHERE id = ? ''',(id,))
        reserva=cursor.fetchone()
        conexao.close()
        return reserva
    
   

    def cadastrar_reserva(self,reserva:Reserva):
        conexao=self.conectar()
        cursor=conexao.cursor()

        cursor.execute(''' INSERT INTO reservas (cliente_id,quarto_id,dias)
                       VALUES (?,?,?) ''',(reserva.cliente_id,reserva.quarto_id,reserva.dias))
        conexao.commit()
        conexao.close()

    def remover_por_id(self,id):
        conexao=self.conectar()
        cursor=conexao.cursor()

        cursor.execute('''DELETE FROM reservas WHERE id = ? ''',(id,))
        conexao.commit()
        conexao.close()

    