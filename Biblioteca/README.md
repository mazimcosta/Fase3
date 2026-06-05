# Sistema de Biblioteca

Projeto desenvolvido em Python com arquitetura em camadas utilizando PostgreSQL para persistência dos dados.

## Objetivo

Simular o funcionamento básico de uma biblioteca, permitindo:

- Cadastro de usuários
- Cadastro de livros
- Realização de empréstimos
- Devolução de empréstimos
- Controle de disponibilidade dos livros
- Persistência dos dados em banco PostgreSQL

---

## Tecnologias Utilizadas

- Python 3.13
- PostgreSQL
- Psycopg 3
- SQL

---

## Estrutura do Projeto

```text
biblioteca/
│
├── database/
│   └── connection.py
│
├── models/
│   ├── usuario.py
│   ├── livro.py
│   └── emprestimo.py
│
├── repositories/
│   ├── usuario_repository.py
│   ├── livro_repository.py
│   └── emprestimo_repository.py
│
├── services/
│   ├── usuario_service.py
│   ├── livro_service.py
│   └── emprestimo_service.py
│
├── sql/
│   └── schema.sql
│
├── main.py
├── requirements.txt
└── README.md
```

---

## Arquitetura

O projeto segue separação de responsabilidades:

### Models

Representam as entidades do sistema.

Exemplos:

- Usuario
- Livro
- Emprestimo

### Repositories

Responsáveis pela comunicação com o banco de dados.

Exemplos:

- Inserção
- Consulta
- Atualização
- Exclusão

### Services

Responsáveis pelas regras de negócio.

Exemplos:

- Verificar usuário existente
- Verificar livro disponível
- Impedir empréstimo inválido
- Registrar devolução

---

## Regras de Negócio

### Usuários

- CPF não pode ser duplicado.

### Livros

- ISBN não pode ser duplicado.

### Empréstimos

- Usuário deve existir.
- Livro deve existir.
- Livro deve estar disponível.
- Ao emprestar, o livro fica indisponível.
- Ao devolver, o livro volta a ficar disponível.

---

## Banco de Dados

O projeto utiliza PostgreSQL.

Execute o script:

```sql
sql/schema.sql
```

para criar as tabelas necessárias.

---

## Instalação

Criar ambiente virtual:

```bash
py -3.13 -m venv venv
```

Ativar:

```bash
venv\Scripts\activate
```

Instalar dependências:

```bash
pip install -r requirements.txt
```

---

## Executar

```bash
py -3.13 main.py
```

---

## Aprendizados

Durante o desenvolvimento foram praticados:

- Programação Orientada a Objetos
- Encapsulamento
- Property e Setter
- Separação de responsabilidades
- Arquitetura em camadas
- SQL
- PostgreSQL
- Tratamento de exceções
- Regras de negócio
- Integração Python + Banco de Dados

---

## Próximos Passos

- Migrar o sistema para FastAPI
- Criar endpoints REST
- Utilizar Pydantic
- Implementar testes automatizados
- Dockerizar a aplicação