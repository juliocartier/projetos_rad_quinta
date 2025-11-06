import pg8000

DB_HOST = "localhost"
DB_NAME = "aula_rad"
DB_USER = "postgres"
DB_PASS = "123456"

def conexao_banco():
    return pg8000.connect(
        user=DB_USER,
        password=DB_PASS,
        host=DB_HOST,
        port=5432,
        database=DB_NAME
    )