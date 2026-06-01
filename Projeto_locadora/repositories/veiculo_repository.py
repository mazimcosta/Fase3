import sqlite3
from models.veiculo import Veiculo
class VeiculoRepository:

    def __init__(self,caminho_arquivo='Projeto_locadora//data//veiculos.db'):
        self.caminho_arquivo=caminho_arquivo

    def conectar(self):
        conexao=sqlite3.connect(self.caminho_arquivo)
        return conexao
    
    def listar_veiculos(self):
        conexao=self.conectar()
        cursor=conexao.cursor()

        cursor.execute('''SELECT * FROM veiculos ''')
        lista=cursor.fetchall()
        conexao.close()
        return lista
    
    def buscar_por_id(self,id):
        conexao=self.conectar()
        cursor=conexao.cursor()

        cursor.execute('''SELECT * FROM veiculos WHERE id = ? ''',(id,))
        veiculo_id=cursor.fetchone()
        conexao.close()
        return veiculo_id
    
    def cadastrar_veiculo(self,veiculo:Veiculo):
        conexao=self.conectar()
        cursor=conexao.cursor()

        cursor.execute(''' INSERT INTO veiculos (modelo,marca,ano,disponivel) VALUES(?,?,?,?)''',(veiculo.modelo,veiculo.marca,veiculo.ano,veiculo.disponivel))
        conexao.commit()
        conexao.close()
        
    def remover_por_id(self,id):
        conexao=self.conectar()
        cursor=conexao.cursor() 
        cursor.execute('''DELETE FROM veiculos WHERE id = ? ''',(id,))
        conexao.commit()
        conexao.close() 

    def atualizar_disponibilidade(self,id:int,disponivel:int):
        conexao=self.conectar()
        cursor=conexao.cursor()

        cursor.execute('''UPDATE veiculos SET disponivel = ? WHERE id = ? ''',(disponivel,id))
        conexao.commit()
        conexao.close()