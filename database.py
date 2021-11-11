import sqlite3

class Database:
    def __init__(self, db_path):
        self.db_path = db_path
        self.db_connection = self.create_conn()
        self.cursor = self.create_cursor()
        self.status = True

    def create_conn(self):
        try:
            db_connection = sqlite3.connect(self.db_path)
            return db_connection
        except:
            self.status = False

    def create_cursor(self):
        try:
            cursor = self.db_connection.cursor()
            return cursor
        except:
            self.status = False
    
    def __repr__(self):
        return 'Conectado com sucesso' if self.status else 'Erro'

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS dolar (
                dolar_value FLOAT,
                scraped_at TEXT
            )
        ''')

    def insert_dollar_value(self, values_tuple):
        query = 'INSERT INTO dolar (dolar_value, scraped_at) VALUES (?, ?)'
        self.cursor.execute(query, values_tuple)
        self.db_connection.commit()
    
    def close_conn(self):
        self.db_connection.close()


def main():
    values_tuple = ('5.62', '28/10/2021')
    obj = Database('dolar.db')
    print(obj)
    obj.create_table()
    obj.insert_dollar_value(values_tuple)
    obj.close_conn()


if __name__ == '__main__':
    main()
