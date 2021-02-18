import sqlite3


class Connection_db:
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = self.create_connection()

    def create_connection(self):
        conn = None

        try:
            conn = sqlite3.connect(self.db_file)
        except ValueError as e:
            print('Erro ao conectar no banco ' + e)
        
        return conn

    def select_all_links(self):
        cur = self.conn.cursor()
        try:
            cur.execute("SELECT file_path FROM gazettes")
        except ValueError as e:
            print('Não foi possível buscar os dados ' + e)
        
        rows = cur.fetchall()

        self.close_bd()

        return rows

    def close_bd(self):
        self.conn.close()
