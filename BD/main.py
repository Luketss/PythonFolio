import sqlite3 as sq

#Criando a conexão com o db clientes
conn = sq.connect('clientes.db')

#cursor: é um interador que permite navegar e manipular os registros do bd.
cursor = conn.cursor()

#criando uma table
def createTableClientes():
    cursor.execute("""
    CREATE TABLE clientes ( 
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(50) NOT NULL,
        idade INTEGER NOT NULL,
        cpf VARCHAR(11) NOT NULL,
        email TEXT NOT NULL,
        fone TEXT,
        cidade TEXT,
        criado_em DATE NOT NULL
    );
    """)

    print('Tabela criada com sucesso. ')

def insertDataInTable(nome, idade, cpf, email, fone, cidade, criado_em):
    cursor.execute("""
    INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, criado_em)
    VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}')
    """.format(nome, idade, cpf, email, fone, cidade, criado_em))

if __name__ == "__main__":
    insertDataInTable('Lucas', '22', '12468080645', 'lucassilluziogmail.com', '31984163014', 'BH', '2020-10-27')
conn.commit()
print('Dados inseridos com sucesso. ')
conn.close()

