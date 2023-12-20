# ALTER STATEMENT

Nesta seção haverão os comandos ALTER realizados no banco de dados.

# ✅ STATEMENTS

CREATE TABLE vendas_nova (
    data_venda DATE,
    id_produto INTEGER,
    qtd_vendida INTEGER,
    nome_produto VARCHAR(80),
    id_loja INTEGER,
    id_cliente INTEGER,
    total_venda FLOAT,
    PRIMARY KEY (id_produto, id_cliente, id_loja),
    FOREIGN KEY (id_produto) REFERENCES produtos(id_produto) ON DELETE SET NULL,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente) ON DELETE SET NULL,
    FOREIGN KEY (id_loja) REFERENCES lojas(id_loja) ON DELETE SET NULL
);

INSERT INTO vendas_nova SELECT * FROM vendas;

ALTER TABLE vendas RENAME TO vendas_antiga;
ALTER TABLE vendas_nova RENAME TO vendas;

