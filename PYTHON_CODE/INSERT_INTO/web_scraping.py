import sqlite3
import requests
from bs4 import BeautifulSoup
import random

# Função para obter dados da página e inserir no banco de dados
def scrape_and_insert_data(url, categoria):
    # Realiza a requisição HTTP
    response = requests.get(url)

    # Verifica se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Parseia o conteúdo HTML da página
        soup = BeautifulSoup(response.text, 'html.parser')

        # Encontra todos os elementos de produto na página
        produtos = soup.find_all('a', class_='item-link')

        # Itera sobre cada produto e extrai os dados
        for produto in produtos:
            nome_produto = produto.find('div', class_='js-item-name').text.strip()
            preco_produto = float(produto.find('span', class_='js-price-display').text.replace('R$', '').replace(',', '.'))
            custo_unit = round(preco_produto * 0.5, 2)

            # Verifica se o produto já existe na tabela
            if not produto_existe(nome_produto):
                # Insere os dados no banco de dados
                inserir_dados_banco(nome_produto, custo_unit, preco_produto, categoria)
                print(f"Inserção bem-sucedida para o produto: {nome_produto}")
            else:
                print(f"Produto já existe na tabela: {nome_produto}")
    else:
        print(f"Falha na requisição. Status Code: {response.status_code}")

    print("Processo concluído com sucesso.")

# Função para verificar se o produto já existe na tabela
def produto_existe(nome_produto):
    # Conecta ao banco de dados
    conn = sqlite3.connect('bancodedados.db')
    cursor = conn.cursor()

    # Verifica se o produto já existe na tabela
    cursor.execute("SELECT * FROM produtos WHERE nome_produto=?", (nome_produto,))
    resultado = cursor.fetchone()

    # Fecha a conexão com o banco de dados
    conn.close()

    return resultado is not None

# Função para inserir dados no banco de dados
def inserir_dados_banco(nome_produto, custo_unit, preco_unit, categoria):
    # Conecta ao banco de dados
    conn = sqlite3.connect('bancodedados.db')
    cursor = conn.cursor()

    # Insere os dados na tabela
    cursor.execute("INSERT INTO produtos (nome_produto, custo_unit, preco_unit, categoria) VALUES (?, ?, ?, ?)",
                   (nome_produto, custo_unit, preco_unit, categoria))

    # Commit e fecha a conexão com o banco de dados
    conn.commit()
    conn.close()

# URL da página a ser extraída
url = 'https://sites.com.br'

# Categoria do produto (insira manualmente)
categoria_produto = 'ACESSÓRIOS'

# Chama a função para extrair dados e inserir no banco de dados
scrape_and_insert_data(url, categoria_produto)
