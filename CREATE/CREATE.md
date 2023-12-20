# CREATE STATEMENT

Nesta seção haverá todos os comandos CREATE realizados no banco de dados.

📝 Não há os comandos de CREATE DATABASE nessa atividade pois o mesmo foi criado através de conexão local por meio do DBeaver.

# ✅ STATEMENTS

-- Creating table produtos and setting the attributes

CREATE TABLE produtos (
	id_produto INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
	custo_unit FLOAT NOT NULL,
	preco_unit FLOAT NOT NULL, 
	nome_produto VARCHAR(80),
	categoria VARCHAR(50)
	);
	
-- Creating table clientes and setting the attributes	

CREATE TABLE clientes (
	nome_cliente VARCHAR(80) NOT NULL,
	email_cliente VARCHAR(80) NOT NULL,
	id_cliente INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
	sexo_cliente VARCHAR(1), 
	cidade_cliente VARCHAR(50),
	estado_cliente VARCHAR(2)
);

-- Creating table gerentes and setting the attributes

CREATE TABLE gerentes (
	nome_gerente VARCHAR (80),
	sexo_gerente VARCHAR(1),
	id_gerente INTEGER NOT NULL PRIMARY KEY,
	salario_ger FLOAT,
	contrato_ger DATE
);

-- Creating table lojas and setting the attributes

CREATE TABLE lojas (
	id_loja INTEGER NOT NULL PRIMARY KEY,
	cidade_loja VARCHAR(50),
	estado_loja VARCHAR (2),
	id_gerente INT NOT NULL,
	FOREIGN KEY (id_gerente)
	REFERENCES gerentes(id_gerente)
	ON DELETE SET NULL
);

-- Creating table funcionarios and setting the attributes

CREATE TABLE funcionarios (
	nome_func VARCHAR(80),
	sexo_func VARCHAR (1),
	salario_func FLOAT,
	contrato_func DATE,
	id_func INTEGER NOT NULL,
	id_loja INTEGER NOT NULL,
	FOREIGN KEY (id_loja)
	REFERENCES lojas(id_loja)
	ON DELETE SET NULL
);

-- Creating table vendas, setting the attributes and defining foreign keys

CREATE TABLE vendas (
	data_venda DATE,
	id_produto INTEGER NOT NULL,
	qtd_vendida INTEGER NOT NULL,
	nome_produto VARCHAR(80),
	id_loja INTEGER NOT NULL,
	id_cliente INTEGER NOT NULL,
	total_venda FLOAT NOT NULL,
    	PRIMARY KEY (id_produto, id_cliente, id_loja),
 	FOREIGN KEY (id_produto) REFERENCES produtos(id_produto) ON DELETE CASCADE,
    	FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente) ON DELETE CASCADE,
    	FOREIGN KEY (id_loja) REFERENCES lojas(id_loja) ON DELETE CASCADE
);


