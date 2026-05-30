🚗 Locadora de Veículos

Projeto desenvolvido durante minha formação em Backend Python com o objetivo de praticar conceitos de programação orientada a objetos, banco de dados SQLite e arquitetura em camadas.

📚 Objetivos do Projeto

- Praticar SQL e SQLite
- Aplicar arquitetura em camadas
- Trabalhar com Repository Pattern
- Implementar regras de negócio em Service
- Simular um sistema real de locadora de veículos

🏗️ Estrutura do Projeto

Projeto_locadora/
│
├── data/
│   └── locadora.db
│
├── models/
│   └── veiculo.py
│
├── repository/
│   └── veiculo_repository.py
│
├── service/
│   └── veiculo_service.py
│
└── main.py

🚘 Funcionalidades

- Cadastrar veículo
- Listar veículos
- Buscar veículo por ID
- Atualizar disponibilidade do veículo
- Remover veículo
- Alugar veículo
- Devolver veículo

🗄️ Banco de Dados

O projeto utiliza SQLite para armazenamento local dos dados.

Tabela principal:

CREATE TABLE veiculos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    modelo TEXT NOT NULL,
    marca TEXT NOT NULL,
    ano INTEGER,
    disponivel INTEGER NOT NULL
);

Disponibilidade

1 = Disponível
0 = Alugado

🔄 Fluxo da Aplicação

Main
 ↓
Service
 ↓
Repository
 ↓
SQLite

Responsabilidades

Repository

- Comunicação com o banco de dados
- Consultas SQL
- Inserção, busca, atualização e remoção de registros

Service

- Regras de negócio
- Validações
- Controle de aluguel e devolução

🛠️ Tecnologias Utilizadas

- Python
- SQLite
- SQL
- Git
- GitHub

🎯 Aprendizados

Durante o desenvolvimento deste projeto foram praticados conceitos como:

- CRUD completo
- SQL parametrizado
- fetchone() e fetchall()
- Separação de responsabilidades
- Arquitetura em camadas
- Modelagem de dados
- Repository Pattern

🚀 Próximos Passos

- Adicionar FastAPI
- Criar endpoints REST
- Migrar para PostgreSQL
- Implementar testes automatizados
- Adicionar Docker
- Realizar deploy da aplicação

👨‍💻 Autor

Projeto desenvolvido como parte da jornada de estudos em Backend Python.
