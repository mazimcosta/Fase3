MINI BOSS — LOCADORA DE VEÍCULOS

Objetivo:
Construir uma API completa utilizando:

✓ FastAPI
✓ SQLite
✓ Arquitetura em Camadas
✓ HTTPException
✓ CRUD

========================================
CENÁRIO
========================================

Você foi contratado para desenvolver o backend
de uma pequena locadora de veículos.

O sistema deve permitir:

- cadastrar veículos
- listar veículos
- buscar veículos
- alugar veículos
- devolver veículos
- remover veículos

========================================
BANCO DE DADOS
========================================

Criar banco:

locadora.db

Criar tabela:

veiculos

Campos:

id INTEGER PRIMARY KEY AUTOINCREMENT
modelo TEXT NOT NULL
marca TEXT NOT NULL
ano INTEGER
disponivel INTEGER

Observação:

1 = disponível

0 = alugado

========================================
ARQUITETURA
========================================

Estrutura obrigatória:

projeto/

├── main.py
├── models/
│   └── veiculo.py
├── services/
│   └── veiculo_service.py
├── repositories/
│   └── veiculo_repository.py

========================================
MODEL
========================================

Criar:

class Veiculo(BaseModel)

Campos:

modelo
marca
ano
disponivel

========================================
ENDPOINTS
========================================

LISTAR VEÍCULOS

GET /veiculos

Retornar todos os veículos.

========================================

BUSCAR VEÍCULO

GET /veiculos/{modelo}

Se não existir:

404

========================================

CADASTRAR VEÍCULO

POST /veiculos

status_code=201

Se já existir:

400

========================================

ALUGAR VEÍCULO

PUT /veiculos/{modelo}/alugar

Regras:

Se não existir:

404

Se já estiver alugado:

400

Se estiver disponível:

Atualizar disponivel para 0

========================================

DEVOLVER VEÍCULO

PUT /veiculos/{modelo}/devolver

Regras:

Se não existir:

404

Se já estiver disponível:

400

Se estiver alugado:

Atualizar disponivel para 1

========================================

REMOVER VEÍCULO

DELETE /veiculos/{modelo}

Se não existir:

404

========================================
RESPONSABILIDADES
========================================

Repository:

Responsável por:

SELECT

INSERT

UPDATE

DELETE

Não deve conter regras de negócio.

========================================

Service:

Responsável por:

Validações

Verificar existência

Verificar disponibilidade

Tomar decisões

========================================

Main:

Responsável apenas por:

Rotas

HTTPException

Status Codes

========================================
TESTES OBRIGATÓRIOS
========================================

Cadastrar:

Corolla

Civic

Onix

========================================

Testar:

GET /veiculos

GET /veiculos/Corolla

PUT /veiculos/Corolla/alugar

PUT /veiculos/Corolla/alugar novamente

PUT /veiculos/Corolla/devolver

DELETE /veiculos/Corolla

GET /veiculos/Corolla

========================================
CONCEITOS TREINADOS
========================================

FastAPI

SQLite

Service

Repository

Model

HTTPException

Status Codes

fetchone()

fetchall()

SELECT

INSERT

UPDATE

DELETE

Arquitetura em Camadas

========================================
DESAFIO EXTRA
========================================

Criar endpoint:

GET /veiculos/disponiveis

Retornar apenas os veículos
com disponivel = 1

========================================
META FINAL
========================================

Conseguir explicar o fluxo:

Cliente
↓
FastAPI
↓
Service
↓
Repository
↓
SQLite
↓
Repository
↓
Service
↓
JSON
↓
Cliente