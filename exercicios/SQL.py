"""
EXERCICIOS SQL — SAKILA (VERSAO CALIBRADA)

REGRAS:
- Resolver sozinho
- Nao copiar respostas
- Fazer em ordem
- JOIN limitado a 2 tabelas
"""

"""
EXERCICIO 1 — FACIL

Liste os 10 filmes mais longos.

Tabela:
film

Retorne:
- title
- length
- rating
"""

"""
EXERCICIO 2 — FACIL

Liste clientes ativos cujo sobrenome comece com:

S

Tabela:
customer

Retorne:
- first_name
- last_name
- email
"""

"""
EXERCICIO 3 — FACIL

Liste filmes com duracao entre:

90 e 120 minutos

Mas exclua filmes com rating:

    PG-13

Tabela:
film

Retorne:
- title
- length
- rating
"""

"""
EXERCICIO 4 — FACIL

Liste clientes que:

- pertencem a store_id = 1
- estao ativos

Ordene por sobrenome.

Tabela:
customer

Retorne:
- first_name
- last_name
- email
"""

"""
EXERCICIO 5 — FACIL

Liste os 15 pagamentos mais altos.

Tabela:
payment

Retorne:
- customer_id
- amount
- payment_date
"""

"""
EXERCICIO 6 — MEDIO

Liste clientes com o valor total pago.

Tabelas:
customer
payment

Retorne:
- nome
- sobrenome
- valor_total_pago

Objetivo:
Treinar JOIN + GROUP BY
"""

"""
EXERCICIO 7 — MEDIO

Liste filmes e quantas vezes cada filme aparece no inventario.

Tabelas:
film
inventory

Retorne:
- titulo
- quantidade

Objetivo:
Treinar JOIN + COUNT
"""

"""
EXERCICIO 8 — MEDIO

Liste clientes que fizeram pagamentos acima de:

8.00

Tabelas:
customer
payment

Retorne:
- nome
- sobrenome
- valor_pago
"""

"""
EXERCICIO 9 — MEDIO

Liste quantos clientes existem por loja.

Tabela:
customer

Retorne:
- store_id
- quantidade_clientes

Objetivo:
Treinar GROUP BY
"""

"""
EXERCICIO 10 — MEDIO

Liste ratings e quantidade de filmes por rating.

Tabela:
film

Retorne:
- rating
- quantidade_filmes

Objetivo:
Treinar agregacao
"""

"""
EXERCICIO 11 — DIFICIL

Descubra o cliente que mais gastou.

Tabelas:
customer
payment

Retorne:
- nome
- sobrenome
- total_gasto

Objetivo:
JOIN + GROUP BY + ORDER BY + LIMIT
"""

"""
EXERCICIO 12 — DIFICIL

Liste clientes cujo total gasto seja maior que:

100

Tabelas:
customer
payment

Retorne:
- nome
- sobrenome
- total_gasto

Objetivo:
JOIN + GROUP BY + HAVING
"""

"""
EXERCICIO 13 — DIFICIL

Liste filmes com duracao acima da media.

Tabela:
film

Retorne:
- title
- length

Objetivo:
Treinar subquery
"""

"""
EXERCICIO 14 — DIFICIL

Liste filmes que NAO existem no inventario.

Tabelas:
film
inventory

Retorne:
- title

Objetivo:
Treinar LEFT JOIN
"""

"""
EXERCICIO 15 — BOSS FIGHT

Liste clientes que fizeram mais de:

20 pagamentos

Tabelas:
customer
payment

Retorne:
- nome
- sobrenome
- quantidade_pagamentos

Objetivo:
JOIN + GROUP BY + HAVING
"""