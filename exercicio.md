EXERCÍCIO — PYTHON + SQLITE

Objetivo:
substituir o dict em memória por persistência em banco.

NÃO usar:
- FastAPI
- SQLAlchemy
- ORM
- Docker

Usar apenas:

import sqlite3

========================================
PARTE 1 — CRIAR BANCO
========================================

Criar:

escola.db

Criar tabela:

alunos

Campos:

id INTEGER PRIMARY KEY AUTOINCREMENT
nome TEXT NOT NULL
idade INTEGER
email TEXT

========================================
PARTE 2 — CONEXÃO
========================================

Criar conexão:

conexao = sqlite3.connect("escola.db")

Criar cursor:

cursor = conexao.cursor()

========================================
PARTE 3 — CADASTRAR ALUNO
========================================

Criar:

def cadastrar_aluno(nome, idade, email):

Usar:

INSERT INTO

Lembrar:

conexao.commit()

========================================
PARTE 4 — LISTAR ALUNOS
========================================

Criar:

def listar_alunos():

Usar:

SELECT * FROM alunos

Retornar:

cursor.fetchall()

Pergunta:

Por que fetchall()?

========================================
PARTE 5 — BUSCAR ALUNO
========================================

Criar:

def buscar_aluno(nome):

Usar:

SELECT * FROM alunos
WHERE nome = ?

Passar parâmetro corretamente:

(nome,)

Retornar:

cursor.fetchone()

Pergunta:

Por que fetchone()?

========================================
PARTE 6 — ATUALIZAR EMAIL
========================================

Criar:

def atualizar_email(nome, novo_email):

Usar:

UPDATE alunos
SET email = ?
WHERE nome = ?

Passar os parâmetros na ordem correta.

Lembrar:

conexao.commit()

========================================
PARTE 7 — REMOVER ALUNO
========================================

Criar:

def remover_aluno(nome):

Usar:

DELETE FROM alunos
WHERE nome = ?

Lembrar:

conexao.commit()

========================================
PARTE 8 — TESTES
========================================

Cadastrar:

Joao
Maria
Pedro

Listar todos.

Buscar Maria.

Atualizar email de Pedro.

Remover Joao.

Listar novamente.

========================================
CONCEITOS PARA FIXAR
========================================

Classe Python
↓
Tabela SQL

Objeto
↓
Linha

Atributo
↓
Coluna

========================================
CONCEITOS NOVOS
========================================

sqlite3.connect()

cursor()

execute()

commit()

fetchone()

fetchall()

========================================
META
========================================

Conseguir explicar:

filmes.get(nome)

equivale aproximadamente a:

SELECT * FROM filmes
WHERE nome = ?

e entender quando usar:

fetchone()

ou

fetchall()