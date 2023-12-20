import sqlite3
from faker import Faker

fake = Faker('pt_BR')  # Define a localidade para o Português (Brasil)

# Conecta ao banco de dados SQLite
conn = sqlite3.connect('bancodedados.db')
cursor = conn.cursor()

try:
    for _ in range(101):
        dados = (
            fake.name(),
            fake.email(),
            fake.random_element(elements=('M', 'F')),
            fake.last_name(),
            fake.state_abbr()
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
