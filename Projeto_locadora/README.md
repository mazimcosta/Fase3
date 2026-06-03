# 🚗 Sistema de Locadora de Veículos

Projeto desenvolvido durante minha formação em Backend Python com o objetivo de praticar arquitetura em camadas, Programação Orientada a Objetos, SQL e persistência de dados utilizando SQLite.

## 📚 Objetivos

* Consolidar conceitos de POO
* Praticar SQL na aplicação
* Implementar arquitetura em camadas
* Aplicar Repository Pattern
* Separar regras de negócio da persistência
* Simular um sistema real de locadora de veículos

---

## 🏗️ Arquitetura

```text
Main
 ↓
Service
 ↓
Repository
 ↓
SQLite
```

### Responsabilidades

#### Service

* Regras de negócio
* Validações
* Controle de aluguel e devolução
* Tratamento de erros da aplicação

#### Repository

* Comunicação com banco de dados
* Consultas SQL
* Inserção de registros
* Atualização de registros
* Remoção de registros

#### SQLite

* Persistência dos dados

---

## 📂 Estrutura do Projeto

```text
Projeto_locadora/
│
├── data/
│   └── veiculos.db
│
├── models/
│   └── veiculo.py
│
├── repositories/
│   └── veiculo_repository.py
│
├── services/
│   └── veiculo_service.py
│
├── main.py
│
└── README.md
```

---

## 🚘 Funcionalidades Implementadas

### Veículos

* ✅ Cadastrar veículo
* ✅ Buscar veículo por ID
* ✅ Listar veículos
* ✅ Remover veículo
* ✅ Atualizar disponibilidade

### Locação

* ✅ Alugar veículo
* ✅ Devolver veículo
* ✅ Validação de veículo inexistente
* ✅ Controle de disponibilidade

---

## 🗄️ Banco de Dados

Tabela principal:

```sql
CREATE TABLE veiculos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    modelo TEXT NOT NULL,
    marca TEXT NOT NULL,
    ano INTEGER NOT NULL,
    disponivel INTEGER NOT NULL
);
```

### Disponibilidade

```text
1 = Disponível
0 = Alugado
```

---

## 🛠️ Tecnologias Utilizadas

* Python 3
* SQLite
* SQL
* Git
* GitHub

---

## 🎯 Conceitos Praticados

* Programação Orientada a Objetos
* Encapsulamento
* Repository Pattern
* Arquitetura em Camadas
* CRUD Completo
* SQL Parametrizado
* SQLite
* Regras de Negócio
* Tratamento de Exceções
* Separação de Responsabilidades

---

## 🧪 Fluxos Testados

### Cadastro de veículo

```text
Cadastrar veículo
↓
Persistir no SQLite
↓
Retornar sucesso
```

### Aluguel

```text
Buscar veículo
↓
Verificar disponibilidade
↓
Atualizar para indisponível
```

### Devolução

```text
Buscar veículo
↓
Atualizar para disponível
```

### Veículo inexistente

```text
Buscar veículo
↓
ValueError
```

---

## 🚀 Próximas Evoluções

* [ ] Criar sistema de clientes
* [ ] Criar sistema de reservas
* [ ] Relacionamento entre entidades
* [ ] Migrar SQLite → PostgreSQL
* [ ] Criar API com FastAPI
* [ ] Implementar testes automatizados
* [ ] Dockerizar aplicação
* [ ] Deploy

---

## 👨‍💻 Autor

Projeto desenvolvido como parte da minha jornada de formação em Backend Python e Engenharia de Software.

---

## 📈 Status do Projeto

✅ Concluído (Versão SQLite)

Este projeto representa a conclusão do primeiro mini-boss da Fase 3 da formação Backend Python, consolidando:

* Arquitetura em camadas
* Repository Pattern
* SQLite
* SQL aplicado
* CRUD completo
* Regras de negócio
* Tratamento de erros
* Organização de projeto profissional

Próxima etapa: Sistema de Reserva de Quartos utilizando SQLite e relacionamentos entre entidades.
