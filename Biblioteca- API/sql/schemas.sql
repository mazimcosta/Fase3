-- Table: public.usuarios

-- DROP TABLE IF EXISTS public.usuarios;

CREATE TABLE IF NOT EXISTS public.usuarios
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    nome character varying(100) COLLATE pg_catalog."default" NOT NULL,
    cpf character varying(14) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT usuarios_pkey PRIMARY KEY (id),
    CONSTRAINT usuarios_cpf_key UNIQUE (cpf)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.usuarios
    OWNER to postgres;



CREATE TABLE IF NOT EXISTS public.livros
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    titulo character varying(200) COLLATE pg_catalog."default" NOT NULL,
    autor character varying(100) COLLATE pg_catalog."default" NOT NULL,
    isbn character varying(50) COLLATE pg_catalog."default" NOT NULL,
    disponivel boolean DEFAULT true,
    CONSTRAINT livros_pkey PRIMARY KEY (id),
    CONSTRAINT livros_isbn_key UNIQUE (isbn)
)

CREATE TABLE IF NOT EXISTS public.emprestimos
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    usuario_id integer NOT NULL,
    livro_id integer NOT NULL,
    data_emprestimo timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    data_devolucao character varying(50) COLLATE pg_catalog."default" DEFAULT 'aguardando'::character varying,
    CONSTRAINT emprestimos_pkey PRIMARY KEY (id),
    CONSTRAINT emprestimos_livro_id_fkey FOREIGN KEY (livro_id)
        REFERENCES public.livros (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT emprestimos_usuario_id_fkey FOREIGN KEY (usuario_id)
        REFERENCES public.usuarios (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)
