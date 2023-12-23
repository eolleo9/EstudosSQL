import sqlite3
from faker import Faker

fake = Faker('pt_BR')  # Define a localidade para o Português (Brasil)

# Lista de capitais do Brasil e suas UFs correspondentes
capitais_brasil = {
    'Brasília': 'DF',
    'São Paulo': 'SP',
    'Rio de Janeiro': 'RJ',
    'Belém': 'PA',
    'Fortaleza': 'CE',
    'Salvador': 'BA',
    'Belo Horizonte': 'MG',
    'Manaus': 'AM',
    'Curitiba': 'PR',
    'Recife': 'PE',
    'Goiânia': 'GO',
    'Belém': 'PA',
    'Porto Alegre': 'RS',
    'Florianópolis': 'SC',
    'Natal': 'RN',
    'Teresina': 'PI',
    'Campo Grande': 'MS',
    'João Pessoa': 'PB',
    'Cuiabá': 'MT',
    'Aracaju': 'SE',
    'Maceió': 'AL',
    'Macapá': 'AP',
    'Palmas': 'TO',
    'Boa Vista': 'RR',
    'Rio Branco': 'AC',
    'São Luís': 'MA',
}

# Conecta ao banco de dados SQLite
conn = sqlite3.connect('bancodedados.db')
cursor = conn.cursor()

try:
    for _ in range(112):

        cidade = fake.random_element(elements=list(capitais_brasil.keys()))
        uf = capitais_brasil[cidade]

        dados = (
            fake.name(),
            fake.email(),
            fake.random_element(elements=('M', 'F')),
            cidade,
            uf
        )

        # Insere dados no banco de dados
        cursor.execute('''
            INSERT INTO clientes (nome_cliente, email_cliente, sexo_cliente, cidade_cliente, estado_cliente)
            VALUES (?, ?, ?, ?, ?)
        ''', dados)

    # Confirma as alterações no banco de dados
    conn.commit()

    # Imprime mensagem de conclusão uma vez após o término do loop
    print("Inserções concluídas com sucesso.")

except Exception as e:
    print(f"Erro durante a inserção: {e}")

finally:
    # Fecha a conexão com o banco de dados
    conn.close()
