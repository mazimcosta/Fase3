import sqlite3

conexao=sqlite3.connect('escola.db')
cursor=conexao.cursor()

def cadastrar_aluno(nome,idade,email):
    cursor.execute('''
                    INSERT  INTO alunos( 
                   nome,idade,email)

                   VALUES(?,?,?) 
                   ''',
                   (nome,idade,email))
    conexao.commit()
    return f' Aluno cadastrado com sucesso'

def listar_alunos():
    cursor.execute(''' SELECT * FROM alunos''')
    return cursor.fetchall()


def buscar_aluno(nome):
    cursor.execute(''' SELECT * FROM alunos WHERE nome = ?''',(nome,))
    return cursor.fetchone()

def atualizar_email(nome,novo_email):
    cursor.execute(''' UPDATE alunos SET email = ? WHERE  nome = ?  ''',(novo_email,nome))
    conexao.commit()
    return f'Atualização feita com sucesso'

def remover_aluno(nome):
    cursor.execute('''DELETE  FROM alunos WHERE nome = ? ''',(nome,))
    conexao.commit()
    return f'Aluno removido com sucesso'

buscar_aluno('Maria')

print(buscar_aluno('Maria'))
atualizar_email('Pedro','pedrinho@gmail.com')

