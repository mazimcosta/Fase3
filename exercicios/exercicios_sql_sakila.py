# =============================================================================
# EXERCÍCIOS SQL — BANCO DE DADOS SAKILA
# Ferramenta: MySQL Workbench
# Banco: sakila (já vem instalado com o MySQL)
# Meta: Resolver todos os 10 exercícios e commitar no GitHub
# =============================================================================
# ESTRUTURA DO SAKILA QUE VOCÊ VAI USAR:
#
# actor    → atores    (actor_id, first_name, last_name)
# film     → filmes    (film_id, title, rating, length, rental_rate)
# customer → clientes  (customer_id, first_name, last_name, email)
# city     → cidades   (city_id, city, country_id)
# country  → países    (country_id, country)
# payment  → pagamentos(payment_id, customer_id, amount, payment_date)
# rental   → aluguéis  (rental_id, customer_id, film_id, rental_date)
# =============================================================================
# REGRAS:
# 1. Rode cada query no Workbench antes de enviar para revisão
# 2. Cole sua solução abaixo de cada enunciado
# 3. Commite as queries em sql/exercicios_sakila.sql no GitHub
# =============================================================================


# =============================================================================
# EXERCÍCIO 01 | SELECT + ORDER BY
# Nível: Iniciante | Tabela: actor
# Status: [ ] Pendente | [ ] Enviado | [ ] Revisado | [ ] Corrigido
# =============================================================================
"""
TAREFA:
Liste o primeiro nome e sobrenome de todos os atores
em ordem alfabética pelo primeiro nome.

COLUNAS ESPERADAS:
first_name | last_name

DICA:
Use ORDER BY no final da query.
"""

# SUA SOLUÇÃO (cole a query SQL aqui):
query_01 = """

"""


# =============================================================================
# EXERCÍCIO 02 | WHERE + ORDER BY
# Nível: Iniciante | Tabela: film
# Status: [ ] Pendente | [ ] Enviado | [ ] Revisado | [ ] Corrigido
# =============================================================================
"""
TAREFA:
Liste o título e a duração (length) de todos os filmes
com duração maior que 120 minutos,
ordenados do mais longo para o mais curto.

COLUNAS ESPERADAS:
title | length

DICA:
WHERE para filtrar, ORDER BY com DESC para ordenar decrescente.
"""

# SUA SOLUÇÃO:
query_02 = """

"""


# =============================================================================
# EXERCÍCIO 03 | WHERE + LIKE
# Nível: Iniciante | Tabela: customer
# Status: [ ] Pendente | [ ] Enviado | [ ] Revisado | [ ] Corrigido
# =============================================================================
"""
TAREFA:
Liste o email de todos os clientes
cujo primeiro nome começa com a letra "J".

COLUNAS ESPERADAS:
first_name | email

DICA:
Use LIKE 'J%' — o % significa "qualquer coisa depois do J".
"""

# SUA SOLUÇÃO:
query_03 = """

"""


# =============================================================================
# EXERCÍCIO 04 | WHERE + IN + ORDER BY
# Nível: Iniciante | Tabela: film
# Status: [ ] Pendente | [ ] Enviado | [ ] Revisado | [ ] Corrigido
# =============================================================================
"""
TAREFA:
Liste o título e a classificação (rating) dos filmes
que tenham rating igual a "PG" ou "G",
em ordem alfabética pelo título.

COLUNAS ESPERADAS:
title | rating

DICA:
Use WHERE rating IN ('PG', 'G') em vez de dois WHERE separados.
"""

# SUA SOLUÇÃO:
query_04 = """

"""


# =============================================================================
# EXERCÍCIO 05 | WHERE com múltiplas tabelas
# Nível: Médio | Tabelas: customer, address, city
# Status: [ ] Pendente | [ ] Enviado | [ ] Revisado | [ ] Corrigido
# =============================================================================
"""
TAREFA:
Liste o primeiro nome, sobrenome e email
dos clientes que moram na cidade de "London".

COLUNAS ESPERADAS:
first_name | last_name | email

DICA:
A cidade está na tabela city, não em customer.
Você vai precisar ligar as tabelas:
customer → address → city

Tente primeiro com WHERE:
WHERE customer.address_id = address.address_id
AND address.city_id = city.city_id
AND city.city = 'London'
"""

# SUA SOLUÇÃO:
query_05 = """

"""


# =============================================================================
# EXERCÍCIO 06 | COUNT
# Nível: Iniciante | Tabela: film
# Status: [ ] Pendente | [ ] Enviado | [ ] Revisado | [ ] Corrigido
# =============================================================================
"""
TAREFA:
Quantos filmes existem no total?
Retorne apenas o número total com um nome de coluna legível.

RESULTADO ESPERADO:
total_filmes
1000

DICA:
Use COUNT(*) e AS para nomear a coluna.
SELECT COUNT(*) AS total_filmes FROM film
"""

# SUA SOLUÇÃO:
query_06 = """

"""


# =============================================================================
# EXERCÍCIO 07 | AVG + ROUND
# Nível: Iniciante | Tabela: film
# Status: [ ] Pendente | [ ] Enviado | [ ] Revisado | [ ] Corrigido
# =============================================================================
"""
TAREFA:
Qual é o valor médio de aluguel (rental_rate) dos filmes?
Arredonde para 2 casas decimais.

RESULTADO ESPERADO:
media_aluguel
2.98  (valor aproximado)

DICA:
Use AVG() para média e ROUND() para arredondar.
SELECT ROUND(AVG(rental_rate), 2) AS media_aluguel FROM film
"""

# SUA SOLUÇÃO:
query_07 = """

"""


# =============================================================================
# EXERCÍCIO 08 | ORDER BY + LIMIT
# Nível: Iniciante | Tabela: film
# Status: [ ] Pendente | [ ] Enviado | [ ] Revisado | [ ] Corrigido
# =============================================================================
"""
TAREFA:
Liste os 10 filmes mais caros para alugar,
mostrando título e rental_rate,
ordenados do mais caro para o mais barato.

COLUNAS ESPERADAS:
title | rental_rate

DICA:
ORDER BY rental_rate DESC e LIMIT 10 no final.
"""

# SUA SOLUÇÃO:
query_08 = """

"""


# =============================================================================
# EXERCÍCIO 09 | GROUP BY + COUNT + ORDER BY
# Nível: Médio | Tabela: film
# Status: [ ] Pendente | [ ] Enviado | [ ] Revisado | [ ] Corrigido
# =============================================================================
"""
TAREFA:
Quantos filmes existem por classificação (rating)?
Mostre o rating e a quantidade,
ordenados pela quantidade de forma decrescente.

RESULTADO ESPERADO:
rating | quantidade
PG-13  | 223
NC-17  | 210
R      | 195
PG     | 194
G      | 178

DICA:
Use GROUP BY rating e COUNT(*) para contar.
ORDER BY quantidade DESC para ordenar.
"""

# SUA SOLUÇÃO:
query_09 = """

"""


# =============================================================================
# EXERCÍCIO 10 | LIKE + WHERE
# Nível: Iniciante | Tabela: actor
# Status: [ ] Pendente | [ ] Enviado | [ ] Revisado | [ ] Corrigido
# =============================================================================
"""
TAREFA:
Liste o primeiro nome e sobrenome dos atores
cujo sobrenome contém a letra "son" em qualquer posição.

COLUNAS ESPERADAS:
first_name | last_name

DICA:
Use LIKE '%son%' — os % dos dois lados significa
"qualquer coisa antes E depois de son".
"""

# SUA SOLUÇÃO:
query_10 = """

"""


# =============================================================================
# VERIFICAÇÃO DE PROGRESSO
# =============================================================================
print("=" * 50)
print("EXERCÍCIOS SQL — SAKILA")
print("=" * 50)
exercicios = [
    "01 - SELECT + ORDER BY (atores)",
    "02 - WHERE + ORDER BY (filmes longos)",
    "03 - WHERE + LIKE (clientes com J)",
    "04 - WHERE + IN (rating PG ou G)",
    "05 - WHERE múltiplas tabelas (London)",
    "06 - COUNT (total de filmes)",
    "07 - AVG + ROUND (média aluguel)",
    "08 - ORDER BY + LIMIT (top 10 caros)",
    "09 - GROUP BY + COUNT (filmes por rating)",
    "10 - LIKE (sobrenome com son)",
]
for ex in exercicios:
    print(f"[ ] {ex}")
print("=" * 50)
print("Cole suas queries nas variáveis query_01 a query_10")
print("Depois envie para revisão")
print("=" * 50)
