import sqlite3 

#conecta no banco
conexao = sqlite3.connect('example.db')

#é o que manda
cursor = conexao.cursor()

# Criar a tabela (execute apenas uma vez, pode causar erro se a tabela já existir)
try:
    cursor.execute('''CREATE TABLE Imagens
                   (id INTEGER PRIMARY KEY, nome TEXT, imagem BLOB)''')
except sqlite3.OperationalError:
    print("A tabela já existe!")

#mostrar a tabela
mostrar = conexao.execute("select * imagens").fetchall()
print(mostrar)

#Coloca os dados usando Insert Into
cursor.execute("INSERT INTO Imagens VALUES ()")

#vai fechar a conexão com o banco
conexao.close()
