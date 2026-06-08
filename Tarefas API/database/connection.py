
import psycopg

def conectar():
    conexao=psycopg.connect(
        dbname="seu banco",
        user="postgres",
        password="sua senha",
        host="localhost",
        port="5432"

    )
    return conexao                                                