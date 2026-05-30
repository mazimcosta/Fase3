-- Criando uma tabela com SQlite
CREATE TABLE alunos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NON NULL,
    idade INTEGER,
    email TEXT
)