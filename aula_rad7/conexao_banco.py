import pg8000

conexao = pg8000.connect(
    user="postgres",
    password="123456",
    host="localhost",
    database="aula_rad"
)

cursor = conexao.cursor()
cursor.execute("select * from alunos_matriculados")
for linha in cursor.fetchall():
    print(linha)

cursor.close()
conexao.close()