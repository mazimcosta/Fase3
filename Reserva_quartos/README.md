# Sistema de Reserva de Quartos

Projeto desenvolvido em Python com foco em arquitetura em camadas, regras de negócio e persistência de dados utilizando SQLite.

## Objetivo

Simular o funcionamento básico de um sistema de reservas de hotel, permitindo:

- Cadastro de clientes
- Cadastro de quartos
- Criação de reservas
- Cancelamento de reservas
- Controle de disponibilidade dos quartos
- Persistência dos dados em banco SQLite

Este projeto foi desenvolvido como parte da minha formação em Backend Python.

---

## Tecnologias Utilizadas

- Python 3
- SQLite
- Programação Orientada a Objetos (POO)

---

## Estrutura do Projeto

```text
reserva_quartos/

├── data/
│   └── hotel.db
│
├── models/
│   ├── cliente.py
│   ├── quarto.py
│   └── reserva.py
│
├── repositories/
│   ├── cliente_repository.py
│   ├── quarto_repository.py
│   └── reserva_repository.py
│
├── services/
│   ├── cliente_service.py
│   ├── quarto_service.py
│   └── reserva_service.py
│
└── main.py
```

---

## Arquitetura

O projeto segue uma separação simples de responsabilidades:

### Models

Responsáveis por representar as entidades do sistema.

Exemplos:

- Cliente
- Quarto
- Reserva

### Repositories

Responsáveis pelo acesso ao banco de dados.

Exemplos:

- Inserção de registros
- Consultas
- Atualizações
- Exclusões

### Services

Responsáveis pelas regras de negócio.

Exemplos:

- Verificar se o cliente existe
- Verificar se o quarto existe
- Verificar disponibilidade do quarto
- Criar reservas
- Cancelar reservas

---

## Regras de Negócio

### Cadastro de Cliente

- Não permite CPF duplicado.

### Cadastro de Quarto

- Não permite número de quarto duplicado.

### Criação de Reserva

- Cliente deve existir.
- Quarto deve existir.
- Quarto deve estar disponível.

### Cancelamento de Reserva

- Reserva deve existir.
- O quarto volta a ficar disponível.

---

## Banco de Dados

O sistema utiliza SQLite para armazenar os dados.

Tabelas criadas:

- clientes
- quartos
- reservas

---

## Tratamento de Erros

O projeto utiliza `ValueError` para regras de negócio inválidas.

Exemplos:

```python
raise ValueError("Cliente nao cadastrado")
raise ValueError("Quarto nao cadastrado")
raise ValueError("Quarto indisponivel")
```

---

## Aprendizados

Durante o desenvolvimento deste projeto foram praticados:

- Programação Orientada a Objetos
- Encapsulamento
- Separação de responsabilidades
- Arquitetura em camadas
- Repository Pattern
- Service Layer
- Integração Python + SQLite
- Validação de regras de negócio
- Tratamento de exceções

---

## Próximos Passos

- Refatoração para PostgreSQL
- Testes automatizados
- API com FastAPI
- Docker
- Deploy

---

## Autor

Desenvolvido por Mazim durante sua jornada de formação Backend Python.