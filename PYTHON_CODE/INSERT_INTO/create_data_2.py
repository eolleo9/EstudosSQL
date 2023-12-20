from faker import Faker
import random
from datetime import date, timedelta
import sqlite3

fake = Faker('pt_BR')  # Define a localidade para o Português (Brasil)

# Conecta ao banco de dados
conn = sqlite3.connect('bancodedados.db')
cursor = conn.cursor()

# Inicia a transação
cursor.execute("BEGIN;")

start_date = date(2018, 3, 21)
end_date = date.today()

for _ in range(100):
    nome_func = fake.name()
    sexo_func = fake.random_element(elements=('M', 'F'))
    salario_func = round(random.uniform(2000, 4000), 2)  # Gera salários entre 2000 e 4000 com duas casas decimais
    contrato_func = fake.date_between_dates(date_start=start_date, date_end=end_date).strftime('%Y-%m-%d')  # Contratos a partir de '2018-03-21'
    id_loja = fake.random_int(min=1, max=3)  # Gera IDs de loja entre 1 e 3
    id_func = fake.random_int(min=200, max=300)  # Gera IDs de funcionário entre 200 e 300

    # Usa parâmetros para evitar injeção de SQL
    cursor.execute("INSERT INTO funcionarios (nome_func, sexo_func, salario_func, contrato_func, id_loja, id_func) VALUES (?, ?, ?, ?, ?, ?);",
                   (nome_func, sexo_func, salario_func, contrato_func, id_loja, id_func))

# Finaliza a transação
cursor.execute("COMMIT;")

# Fecha a conexão
conn.close()

# Imprime conclusão de inserção de dados

print("Inserção de dados de funcionários concluída.")
