# 📝 ToDo API

API REST desenvolvida com **Python**, **FastAPI** e **PostgreSQL** para gerenciamento de tarefas.

Este projeto foi criado com foco em praticar arquitetura backend em camadas, organização de código e integração com banco de dados relacional.

---

## 🚀 Tecnologias Utilizadas

* Python 3
* FastAPI
* PostgreSQL
* Psycopg2
* Pydantic
* Uvicorn

---

## 📂 Estrutura do Projeto

```text
ProjetoTodo/

├── routers/
├── services/
├── repositories/
├── schemas/
├── database/
├── main.py
├── requirements.txt
└── README.md
```

### Arquitetura

```text
Router
 ↓
Service
 ↓
Repository
 ↓
PostgreSQL
```

* **Router:** recebe as requisições HTTP.
* **Service:** contém as regras de negócio.
* **Repository:** responsável pelas consultas SQL.
* **PostgreSQL:** persistência dos dados.

---

## 📋 Funcionalidades

### Tarefas

* ✅ Cadastrar tarefa
* ✅ Listar tarefas
* ✅ Buscar tarefa por ID
* ✅ Concluir tarefa

---

## 📌 Endpoints

### Criar tarefa

```http
POST /tarefas/
```

Exemplo:

```json
{
  "titulo": "Estudar SQL",
  "descricao": "Praticar exercícios do banco Sakila"
}
```

---

### Listar tarefas

```http
GET /tarefas/
```

---

### Buscar tarefa por ID

```http
GET /tarefas/{id}
```

---

### Concluir tarefa

```http
PUT /tarefas/{id}
```

---

## 🗄️ Estrutura da Tabela

```sql
CREATE TABLE tarefas (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    descricao TEXT,
    concluida BOOLEAN DEFAULT FALSE
);
```

---

## ▶️ Executando o Projeto

### Clonar repositório

```bash
git clone URL_DO_REPOSITORIO
```

### Instalar dependências

```bash
pip install -r requirements.txt
```

### Executar aplicação

```bash
uvicorn main:app --reload
```

---

## 📖 Documentação

Após iniciar a aplicação:

```text
http://127.0.0.1:8000/docs
```

---

## 🎯 Objetivo do Projeto

Este projeto foi desenvolvido para consolidar conhecimentos em:

* FastAPI
* PostgreSQL
* CRUD
* APIs REST
* Pydantic
* Arquitetura em Camadas
* Separação de Responsabilidades

---

## 👨‍💻 Autor

Desenvolvido como parte da jornada de formação em Backend Python e Engenharia de Dados.
