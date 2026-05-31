CREATE TABLE veiculos(
id SERIAL PRIMARY KEY,
modelo varchar(100) NOT NULL,
marca varchar(100) NOT NULL,
ano INTEGER NOT NULL,
disponivel BOOLEAN NOT NULL
)