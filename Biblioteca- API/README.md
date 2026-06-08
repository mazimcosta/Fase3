# 📚 Sistema de Biblioteca - API REST com FastAPI

API desenvolvida para gerenciamento de biblioteca utilizando FastAPI, PostgreSQL e SQLAlchemy.

O sistema permite:

- Cadastro de usuários
- Cadastro de livros
- Controle de empréstimos
- Controle de devoluções
- Consulta de registros
- Validação de regras de negócio

---

# 🚀 Tecnologias Utilizadas

- Python 3.12
- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic
- Uvicorn

---

# 📂 Estrutura do Projeto

```text
biblioteca_api/
│
├── database/
│   └── conexao.py
│
├── models/
│   ├── usuario.py
│   ├── livro.py
│   └── emprestimo.py
│
├── schemas/
│   ├── usuario_schema.py
│   ├── livro_schema.py
│   └── emprestimo_schema.py
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
├── routes/
│   ├── usuarios.py
│   ├── livros.py
│   └── emprestimos.py
│
└── main.py