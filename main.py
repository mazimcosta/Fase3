from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import HTTPException
import sqlite3

app = FastAPI()
conexao=sqlite3.connect('escola.db')
cursor=conexao.cursor()
#Exercicio Missão 2

def helper_buscar(nome):
    cursor.execute(''' SELECT * FROM alunos WHERE nome = ?''',(nome,))
    return cursor.fetchone()

@app.get('/')
def home():
    return {'mensagem':'ola'}

@app.get('/alunos',status_code=200)
def listar_alunos():
    cursor.execute('''SELECT * FROM alunos ''')
    lista=cursor.fetchall()
    if not lista:
        raise HTTPException(status_code=404,detail='Alunos nao encontrados')
    return lista

@app.get('/alunos/{nome}',status_code=200)
def buscar_aluno(nome:str):
    aluno=helper_buscar(nome)
    if not aluno:
        raise HTTPException(status_code=404,detail="Aluno nao encontrado")
    return {'id':aluno[0],'nome':aluno[1],'idade':aluno[2],'email':aluno[3]}

@app.post('/alunos'status_code=201)
def cadastrar_aluno(nome:str,idade:int,email:str):
    aluno=helper_buscar(nome)
    if aluno is not None:
        raise HTTPException(status_code=400,detail="Aluno ja cadastrado")
    cursor.execute('''INSERT  INTO alunos 
                   (nome,idade,email)
                   VALUES(?,?,?) ''',(nome,idade,email))
    conexao.commit()
    return {'mensagem': 'Aluno cadastrado com sucesso'}

@app.delete('/alunos/{nome}',status_code=200)
def remover_aluno(nome:str):
    aluno_existe=helper_buscar(nome)
    if aluno_existe is None:
        raise HTTPException(status_code=404,detail="Aluno nao encontrado")
    cursor.execute(''' DELETE FROM alunos WHERE nome = ? ''',(nome,))
    conexao.commit()
    return {'mensagem':'Aluno removido com sucesso'}


