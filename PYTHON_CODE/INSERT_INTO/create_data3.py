import sqlite3
from faker import Faker
import random
from datetime import date, timedelta

fake = Faker('pt_BR')  # Define a localidade para o Português (Brasil)

# Estabelece a conexão com o banco de dados SQLite  
conn = sqlite3.connect('bancodedados.db')
cursor = conn.cursor()

# Substitui 'preco_unit' pelo nome real do campo de preço na tabela 'produtos'
preco_unit_column = 'preco_unit'

# Obtém todos os IDs de produtos existentes no banco de dados
cursor.execute("SELECT id_produto FROM produtos")
produto_ids = [row[0] for row in cursor.fetchall()]

# Obtém todos os IDs de clientes existentes no banco de dados
cursor.execute("SELECT id_cliente FROM clientes")
cliente_ids = [row[0] for row in cursor.fetchall()]

for _ in range(100):
    id_produto = random.choice(produto_ids)  # Escolhe um ID de produto existente
    id_cliente = random.choice(cliente_ids)  # Escolhe um ID de cliente existente

    # Consulta para obter o nome_produto e preco_unit com base no id_produto
    cursor.execute(f"SELECT nome_produto, {preco_unit_column} FROM produtos WHERE id_produto = {id_produto}")
    nome_produto, preco_unit = cursor.fetchone()

    # Gera data de venda fictícia
    start_date = date(2018, 3, 21)
    end_date = date.today()
    data_venda = fake.date_between_dates(date_start=start_date, date_end=end_date).strftime('%Y-%m-%d')

    qtd_vendida = fake.random_int(min=1, max=10)  # Gera quantidades vendidas fictícias
    id_loja = fake.random_int(min=1, max=3)  # Gera IDs fictícios de lojas

    # Verifica se já existe um registro com os mesmos valores
    cursor.execute(f"SELECT 1 FROM vendas WHERE id_produto = {id_produto} AND id_cliente = {id_cliente} AND id_loja = {id_loja}")
    exists = cursor.fetchone()

    if not exists:
        total_venda = qtd_vendida * preco_unit  # Calcula o total_venda
        cursor.execute(f"INSERT INTO vendas (data_venda, id_produto, qtd_vendida, nome_produto, id_loja, id_cliente, total_venda) VALUES ('{data_venda}', {id_produto}, {qtd_vendida}, '{nome_produto}', {id_loja}, {id_cliente}, {total_venda})")

# Commit para salvar as alterações no banco de dados
conn.commit()

# Feche a conexão com o banco de dados
conn.close()


# Mensagem de saída
print("Inserções concluídas com sucesso.")